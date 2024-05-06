import os
from queue import Queue
from typing import List


# Function to search for keywords in a list of files
def search_keywords_in_files(
    files: List[str],
    keywords: List[str],
    result_queue: Queue
) -> None:
    """
    Search for keywords in a list of files.

    :param files: List of file paths.
    :param keywords: List of keywords to search for.
    :param result_queue: Queue to store search results.
    """
    results = {keyword: [] for keyword in keywords}
    for file_path in files:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                for keyword in keywords:
                    if keyword in content:
                        results[keyword].append(os.path.basename(file_path))
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")
    result_queue.put(results)
