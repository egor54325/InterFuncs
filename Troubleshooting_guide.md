# Troubleshooting Guide

## Common Issues and Solutions

### 1. Installation Issues
**Symptoms**: Errors during `pip install` or missing dependencies  
**Solutions**:
- Ensure Python 3.6+ is installed
- Update pip: `python -m pip install --upgrade pip`
- Install requirements from project root: `pip install -r requirements.txt`

### 2. Dependency Issues
**Symptoms**: Import errors or missing modules  
**Solutions**:
- Verify all dependencies are installed:
  ```bash
  pip install art requests rich beautifulsoup4 pyexecjs
  ```
- Check Python environment matches project requirements

### 3. Configuration Issues
**Symptoms**: Missing config files or invalid JSON  
**Solutions**:
- Ensure `config` directory contains:
  - `cookies.json`
  - `params.json` 
  - `config.json`
- Validate JSON syntax in configuration files
- Reset to default configs using menu options 12/13 if needed

### 4. Network-related Issues
**Symptoms**: Connection errors or timeout  
**Solutions**:
- Verify internet connection
- Check URL formatting (include http:// or https://)
- Temporarily disable firewall/antivirus
- Try different network configuration

### 5. Runtime Errors
**Symptoms**: Unexpected crashes or error messages  
**Solutions**:
- Check error message details
- Ensure cookies/params are properly formatted JSON
- Verify website availability manually
- Report issue with reproduction steps
