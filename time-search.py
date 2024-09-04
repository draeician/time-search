#!/usr/bin/env python3

import os
import sys
import argparse
from datetime import datetime, timedelta
import magic  # For file type detection

def search_files(time_unit, value, file_type=None, verbose=False, base_only=False, max_depth=None):
    # Calculate the cutoff time
    now = datetime.now()
    # Ensure the time_unit is plural
    time_unit_plural = time_unit if time_unit.endswith('s') else f"{time_unit}s"
    cutoff = now - timedelta(**{time_unit_plural: value})

    if verbose:
        print(f"Searching for files modified after: {cutoff}")
        print(f"Time unit: {time_unit}")
        print(f"Value: {value}")
        if file_type:
            print(f"File type filter: {file_type}")
        if max_depth is not None:
            print(f"Maximum depth: {max_depth}")
        print("Starting search...")

    base_dirs = set()

    # Walk through the current directory and its subdirectories
    for root, _, files in os.walk('.', followlinks=False):
        # Check the current depth
        current_depth = root.count(os.sep)
        if max_depth is not None and current_depth > max_depth:
            continue

        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                
                if file_mtime >= cutoff:
                    if file_type:
                        try:
                            mime = magic.Magic(mime=True)
                            file_mime = mime.from_file(file_path)
                            if file_type in file_mime:
                                if base_only:
                                    base_dir = root.split(os.sep)[1] if len(root.split(os.sep)) > 1 else ''
                                    if base_dir and base_dir not in ('.', '..'):
                                        base_dirs.add(base_dir)
                                else:
                                    print(file_path)
                                    if verbose:
                                        print(f"  Modified: {file_mtime}")
                                        print(f"  MIME type: {file_mime}")
                        except IOError:
                            if verbose:
                                print(f"Warning: Unable to determine MIME type for {file_path}")
                    else:
                        if base_only:
                            base_dir = root.split(os.sep)[1] if len(root.split(os.sep)) > 1 else ''
                            if base_dir and base_dir not in ('.', '..'):
                                base_dirs.add(base_dir)
                        else:
                            print(file_path)
                            if verbose:
                                print(f"  Modified: {file_mtime}")
            except (FileNotFoundError, PermissionError) as e:
                if verbose:
                    print(f"Warning: Unable to access {file_path}: {e}")

    if base_only:
        for dir in sorted(base_dirs):
            print(dir)

    if verbose:
        print("Search completed.")

def main():
    parser = argparse.ArgumentParser(description="Search for recently modified files.")
    parser.add_argument('value', type=int, help="Time value")
    parser.add_argument('-t', '--type', help="File type filter")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose output")
    parser.add_argument("--base", action="store_true", help="List only base directories containing changes")
    parser.add_argument('-d', '--depth', type=int, help="Maximum depth for recursive search")
    args = parser.parse_args()

    time_unit = os.path.basename(sys.argv[0]).rstrip('s')
    search_files(time_unit, args.value, args.type, args.verbose, args.base, args.depth)

if __name__ == "__main__":
    main()
