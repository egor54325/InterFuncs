# Contributing to InterFuncs

We welcome contributions! Please follow these guidelines to ensure smooth collaboration.

## Development Setup

### Prerequisites
- Python 3.9+
- pip 23.0+
- Git 2.30+

### Installation
1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/InterFuncs.git
   cd InterFuncs
   ```
3. Set up virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/MacOS
   .venv\Scripts\activate     # Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

## Code Style Guidelines

### General
- Follow PEP 8 conventions
- Use type hints for all new functions
- Maximum line length: 100 characters
- Use f-strings for string formatting
- Include docstrings using Google-style format

### CLI Specific
- Maintain consistent rich console formatting
- Use error codes from `src/errors.py` (create if missing)
- Keep menu options alphabetically ordered

## Pull Request Process

1. Create a feature branch:
   ```bash
   git checkout -b feat/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```
2. Implement your changes
3. Update documentation if applicable
4. Run basic checks:
   ```bash
   flake8 src/
   python -m pytest tests/
   ```
5. Push to your fork:
   ```bash
   git push origin your-branch-name
   ```
6. Open a Pull Request against `main` branch

## PR Requirements
- Reference related issues using #issue-number
- Include screenshots for UI changes
- Provide testing evidence in PR description:
  ```markdown
  ### Testing Performed
  - [ ] Tested on Windows 11
  - [ ] Tested on Ubuntu 22.04
  - [ ] Verified error handling
  ```

## Issue Reporting
When reporting bugs, include:
1. Environment details:
   ```bash
   python -c "import platform; print(platform.platform())"
   python -c "import sys; print(sys.version)"
   ```
2. Exact steps to reproduce
3. Expected vs actual behavior
4. Error logs (if applicable)

## Code of Conduct
All contributors must adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). Please report unacceptable behavior to [your-email@example.com].

## Documentation Standards
- Update `doc.md` for new features
- Add examples to `EXAMPLES.md`
- Keep CLI help texts current

## Testing Requirements
- New features require unit tests
- Use pytest framework
- Place tests in `tests/` directory
- Follow test naming convention: `test_feature_scenario.py`

## License Acknowledgement
By contributing, you agree to license your work under the MIT License. All changes must be compatible with this license.

Thank you for your interest in making InterFuncs better!
