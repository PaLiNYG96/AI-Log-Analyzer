def extract_failure_lines(log_text):
    """
    Extract lines related to test failures and ignore PowerShell or other shell lines.
    """
    lines = log_text.splitlines()
    failure_lines = [
        line for line in lines 
        if 'FAIL' in line or 'Error' in line or 'Timeout' in line or 'AssertionError' in line
    ]
    return "\n".join(failure_lines)