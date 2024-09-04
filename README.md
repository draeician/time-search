# Time Search

Time Search is a utility that allows you to quickly find recently modified files based on a specified time range. It supports searching by hours or days and includes optional file type filtering.

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/draeician/time-search.git
   cd time-search
   ```

2. Install the required dependencies:
   ```
   pip install python-magic
   ```

3. Make the script executable:
   ```
   chmod +x timesearch.py
   ```

4. Create symbolic links for different time units:
   ```
   ln -s timesearch.py hours
   ln -s timesearch.py days
   ```

## Usage

The basic syntax is:

```
./<time_unit> <value> [options]
```

Where:
- `<time_unit>` is either `hours` or `days`
- `<value>` is the number of hours or days to search back
- `[options]` are optional flags

### Options

- `-t` or `--type`: Filter by file type
- `-v` or `--verbose`: Enable verbose output

## Examples

1. Find files modified in the last 6 hours:
   ```
   ./hours 6
   ```

2. Find files modified in the last 2 days:
   ```
   ./days 2
   ```

3. Find text files modified in the last 12 hours:
   ```
   ./hours 12 -t text
   ```

4. Find files modified in the last 3 days with verbose output:
   ```
   ./days 3 -v
   ```

5. Find image files modified in the last 24 hours with verbose output:
   ```
   ./hours 24 -t image -v
   ```

## Notes

- The script searches in the current directory and all its subdirectories.
- File type filtering uses MIME types for more accurate results.
- Verbose mode provides additional information about the search process and results.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements or encounter any bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2023 draeician

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.