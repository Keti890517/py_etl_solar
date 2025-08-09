def windows_to_wsl_path(windows_path: str) -> str:
    """
    Convert a Windows path like 'C:\\Users\\User\\Downloads\\jsons'
    to WSL path like '/mnt/c/Users/User/Downloads/jsons'.
    If already WSL-style, return unchanged.
    """
    if ':' not in windows_path:
        return windows_path  # already WSL-style
    drive, rest = windows_path.split(':')
    return f"/mnt/{drive.lower()}{rest.replace('\\', '/')}"