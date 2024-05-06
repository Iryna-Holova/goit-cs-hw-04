import threading
from queue import Queue
from typing import List
from helpers.get_files import get_files_in_directory
from helpers.search_keywords import search_keywords_in_files


# Function to split files between threads and start searching
def process_files_with_threads(
    file_paths: List[str],
    keywords: List[str],
    num_threads: int
) -> dict:
    """
    Process files using multiple threads.

    :param file_paths: List of file paths.
    :param keywords: List of keywords to search for.
    :param num_threads: Number of threads to use.
    :return: Dictionary containing search results.
    """
    results = {keyword: [] for keyword in keywords}
    result_queue = Queue()  # Queue to store results

    # Splitting files between threads
    files_per_thread = len(file_paths) // num_threads
    threads = []
    for i in range(num_threads):
        start_idx = i * files_per_thread
        end_idx = (
            start_idx + files_per_thread
            if i < num_threads - 1
            else len(file_paths)
        )
        thread_files = file_paths[start_idx:end_idx]
        thread = threading.Thread(
            target=search_keywords_in_files,
            args=(thread_files, keywords, result_queue)
        )
        threads.append(thread)
        thread.start()

    # Waiting for all threads to finish
    for thread in threads:
        thread.join()

    # Collecting results from the queue
    while not result_queue.empty():
        thread_results = result_queue.get()
        for keyword in keywords:
            results[keyword].extend(thread_results[keyword])

    return results


def main() -> None:
    directory = "./files"
    keywords = ["JavaScript", "Python", "HTML"]
    num_threads = 3  # Number of threads

    file_paths = get_files_in_directory(directory)
    results = process_files_with_threads(file_paths, keywords, num_threads)
    print(results)


if __name__ == "__main__":
    main()
