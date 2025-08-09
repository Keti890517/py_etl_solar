import os

def windows_to_wsl_path(path: str) -> str:
    """
    Convert Windows path to WSL path if on WSL/Linux.
    On macOS or Windows, returns path with normalized slashes.
    """
    if os.name == "posix":
        # On Linux/WSL: convert if looks like Windows path
        if ':' in path:
            drive, rest = path.split(':', 1)
            rest = rest.lstrip('\\').replace('\\', '/')
            return f"/mnt/{drive.lower()}/{rest}"
    else:
        # Windows, macOS or native Linux, return original path
        return path