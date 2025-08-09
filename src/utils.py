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
            # macOS or native Linux path — normalize slashes only
            return path.replace('\\', '/')
    else:
        # Windows: just normalize slashes
        return path.replace('\\', '/')