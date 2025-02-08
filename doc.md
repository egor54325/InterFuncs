# InterFuncs Documentation

## Overview
InterFuncs is a CLI tool for web interaction and diagnostics, providing:
- Website status checking
- Content analysis
- Network diagnostics
- JavaScript execution
- Configuration management

## Features

### Core Functionality
1. **Network Diagnostics**: Ping servers, check availability
2. **Content Inspection**: Get HTML/JSON, headers, CSS
3. **Script Execution**: Run JavaScript code
4. **Session Management**: Manage cookies and parameters

### Menu Options
| #  | Functionality                  | Description                          |
|----|--------------------------------|--------------------------------------|
| 2  | Ping                          | ICMP ping to specified IP           |
| 3  | Get site status code          | HTTP status code retrieval          |
| 4  | Get site text                 | Save and display page content       |
| 7  | Get site JSON                 | Parse and display JSON responses    |
| 14 | Get CSS on site               | Extract CSS stylesheets             |
| 15 | Execute JavaScript code       | Run JS code in Node.js environment  |

## Configuration
### Configuration Files
- `config.json`: UI/behavior settings
- `cookies.json`: Session cookies storage
- `params.json`: Request parameters

### Managing Configurations
Use menu options 10-13 to:
- Update request parameters
- Modify session cookies
- Reset configurations to defaults

## Dependencies
- Python 3.6+
- Required packages:
  - `requests`: HTTP requests
  - `rich`: Terminal formatting
  - `beautifulsoup4`: HTML parsing
  - `art`: ASCII art generation
  - `pyexecjs`: JavaScript execution

## Usage Examples
1. Check website availability:
   ```bash
   python main.py
   > 8
   > https://example.com
   ```

2. Analyze site CSS:
   ```bash
   python main.py
   > 14
   > https://example.com
   ```

3. Execute JavaScript:
   ```bash
   python main.py
   > 15
   > Enter code: console.log(2+2)
   ```

## Contribution
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Follow the MIT license terms when forking or modifying the code.
