import os
from typing import List


# Function to get a list of files in a directory
def get_files_in_directory(directory: str) -> List[str]:
    """
    Get a list of files in a directory.

    :param directory: Directory path.
    :return: List of file paths.
    """
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files
