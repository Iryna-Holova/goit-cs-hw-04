from multiprocessing import Process, Queue
from typing import List
from helpers.get_files import get_files_in_directory
from helpers.search_keywords import search_keywords_in_files


# Function to split files between process and start searching
def split_files_to_process(
    file_paths: List[str],
    keywords: List[str],
    num_processes: int
) -> dict:
    """
    Split files using multiple process.

    :param file_paths: List of file paths.
    :param keywords: List of keywords to search for.
    :param num_threads: Number of threads to use.
    :return: Dictionary containing search results.
    """
    files_per_process = len(file_paths) // num_processes  # Files per process

    # Splitting files between processes
    processes = []
    result_queue = Queue()  # Queue to store results
    for i in range(num_processes):
        start_idx = i * files_per_process
        end_idx = (
            start_idx + files_per_process
            if i < num_processes - 1
            else len(file_paths)
        )
        process_files = file_paths[start_idx:end_idx]
        process = Process(
            target=search_keywords_in_files,
            args=(process_files, keywords, result_queue)
        )
        processes.append(process)
        process.start()

    # Waiting for all processes to finish
    for process in processes:
        process.join()

    # Collecting and printing results
    final_results = {keyword: [] for keyword in keywords}
    while not result_queue.empty():
        results = result_queue.get()
        for keyword in keywords:
            final_results[keyword].extend(results[keyword])

    return final_results


def main() -> None:
    directory = "./files"
    keywords = ["JavaScript", "Python", "HTML"]
    num_processes = 3  # Number of processes

    file_paths = get_files_in_directory(directory)
    final_results = split_files_to_process(file_paths, keywords, num_processes)
    print(final_results)


if __name__ == "__main__":
    main()
