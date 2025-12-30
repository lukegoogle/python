def simplifyPath(path: str) -> str:
    """Simplifies a Unix-style absolute path to its canonical form.

    Args:
        path: A string representing the absolute path to be simplified.

    Returns:
        A string representing the simplified canonical path.
    """
    # Split the path by slashes; this handles multiple slashes automatically
    parts = path.split("/")
    stack = []

    for portion in parts:
        if portion == "..":
            if stack:
                stack.pop()
        elif portion == "." or not portion:
            # "." means current directory, and empty strings 
            # result from "//", so we skip both.
            continue
        else:
            # It's a valid directory or file name
            stack.append(portion)

    return "/" + "/".join(stack)