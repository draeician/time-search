#!/usr/bin/env python3

import os
import sys
from time_search.main import search_files

def cli():
    """
    CLI entry point that extracts the time unit from the command name
    and passes it to the search_files function.
    """
    try:
        # Get the base command name (e.g., 'hour', 'day', 'week', etc.)
        command_name = os.path.basename(sys.argv[0])
        time_unit = command_name.rstrip('s')
        
        # Remove the command name from sys.argv to make it compatible with the main function
        sys.argv[0] = 'time-search'
        
        # Import and run the main function
        from time_search.main import main
        main()
    except KeyboardInterrupt:
        print("\nOperation interrupted by user. Exiting gracefully.")
        sys.exit(0)

if __name__ == "__main__":
    cli() 