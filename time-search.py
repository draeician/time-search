#!/usr/bin/env python3

import os
import sys
import argparse
from datetime import datetime, timedelta
import magic  # For file type detection

def search_files(time_unit, value, file_type=None, verbose=False, base_only=False):
    # Calculate the cutoff time
    now = datetime.now()
    if time_unit == 'hours':
        cutoff = now - timedelta(hours=value)
    elif time_unit == 'days':
        cutoff = now - timedelta(days=value)
    else:
        print(f"Unsupported time unit: {time_unit}")
        sys.exit(1)

    if verbose:
        print(f"Searching for files modified after: {cutoff}")
        print(f"Time unit: {time_unit}")
        print(f"Value: {value}")
        if file_type:
            print(f"File type filter: {file_type}")
        print("Starting search...")

    base_dirs = set()

    # Walk through the current directory and its subdirectories
    for root, _, files in os.walk('.', followlinks=False):
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
                                    base_dirs.add(root.split(os.sep)[1])
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
                            base_dirs.add(root.split(os.sep)[1])
                        else:
                            print(file_path)
                            if verbose:
                                print(f"  Modified: {file_mtime}")
            except (FileNotFoundError, PermissionError) as e:
                if verbose:
                    print(f"Warning: Unable to access {file_path}: {e}")

    if base_only:
        for dir in sorted(base_dirs):
            if dir:  # Avoid printing an empty string for the current directory
                print(os.path.join('.', dir))

    if verbose:
        print("Search completed.")

def main():
    parser = argparse.ArgumentParser(description="Search for recently modified files.")
    parser.add_argument('value', type=int, help="Time value")
    parser.add_argument('-t', '--type', help="File type filter")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose output")
    parser.add_argument("--base", action="store_true", help="List only base directories containing changes")
    args = parser.parse_args()

    time_unit = os.path.basename(sys.argv[0])
    search_files(time_unit, args.value, args.type, args.verbose, args.base)

if __name__ == "__main__":
    main()
