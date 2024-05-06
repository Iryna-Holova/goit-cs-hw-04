# Computer Systems hw-04

This repository contains Python scripts for parallel processing and analysis of text files to search for specified keywords. The program is designed to operate in two modes: **multithreading** and **multiprocessing**.

1. [Multithreaded Text File Processing](threads.py): This script implements the multithreaded approach using the threading module. It splits the list of files among different threads, with each thread searching for specified keywords in its assigned files.

2. [Multiprocessing Text File Processing](process.py): This script utilizes the multiprocessing approach using the multiprocessing module. It divides the list of files among different processes, with each process responsible for processing its set of files and searching for the specified keywords.

## Usage

Clone the repository to your local machine.

```bash
git clone https://github.com/Iryna-Holova/goit-cs-hw-04
```

Navigate to the repository directory.

```bash
cd goit-cs-hw-04
```

Run the desired Python script based on your processing requirements.

```bash
python threads.py
{'JavaScript': ['text_1.txt', 'text_6.txt', 'text_3.txt', 'text_4.txt'], 'Python': ['text_2.txt', 'text_5.txt'], 'HTML': ['text_6.txt', 'text_3.txt']}
```

or

```bash
python process.py
{'JavaScript': ['text_3.txt', 'text_4.txt', 'text_1.txt', 'text_6.txt'], 'Python': ['text_2.txt', 'text_5.txt'], 'HTML': ['text_3.txt', 'text_6.txt']}
```

## Dependencies

Python 3.x
