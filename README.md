# BookBot - Text Analysis Tool

BookBot is a command-line application designed to analyze text files (e.g., books) and provide insights such as word counts and character frequency statistics. It consists of two main components: `stats.py` and `main.py`.

---

## Components

### `stats.py` - Text Analysis Utilities

The `stats.py` module provides utility functions for analyzing and summarizing textual data. These functions form the backbone of the BookBot application:

1. **Word Count Analysis**  
    - **Function:** `get_word_count(text)`  
    - **Description:** Calculates the total number of words in the provided text by splitting it into individual words. Returns the count as a formatted string.

2. **Character Frequency Analysis**  
    - **Function:** `get_a_character_count(text, chars)`  
    - **Description:** Computes the frequency of specific characters in the text. Accepts a list of characters (`chars`) and counts their occurrences, ignoring case sensitivity. Returns a dictionary where keys are characters and values are their counts.

3. **Character Count Reporting**  
    - **Function:** `report_stats(dic)`  
    - **Description:** Generates a detailed report of character frequencies from a dictionary. Sorts characters by frequency in descending order and filters out non-alphabetic characters. Outputs a clean, human-readable report.

---

### `main.py` - Book Analysis Script

The `main.py` script serves as the entry point for BookBot. It integrates the utility functions from `stats.py` and provides a user-friendly command-line interface for text analysis. Key features include:

1. **Command-Line Interface**  
    - Accepts two arguments:
      - `<path_to_book>`: Path to the text file to analyze.
      - `<chars>`: A string of characters to analyze for frequency.
    - Displays usage instructions if arguments are missing.

2. **Book Text Retrieval**  
    - **Function:** `get_book_text(filepath)`  
    - **Description:** Reads the content of the specified text file. Handles file-not-found errors gracefully by displaying an error message and exiting.

3. **Text Analysis Workflow**  
    - **Function:** `main(filepath, char_list)`  
    - **Description:** Orchestrates the text analysis process:
      - Displays a header for the analysis.
      - Reads the book text from the file.
      - Calculates the word count using `get_word_count` from `stats.py`.
      - Computes character frequencies using `get_a_character_count` from `stats.py`.
      - Outputs the word count and a detailed character frequency report using `report_stats` from `stats.py`.

4. **Error Handling**  
    - Ensures robust error handling for missing arguments and file-related errors.

---

## Usage

1. Ensure Python 3 is installed on your system.
2. Run the script from the command line using the following format:
    ```bash
    ./main.py <path_to_book> <chars>
    ```
    - Replace `<path_to_book>` with the path to the text file you want to analyze.
    - Replace `<chars>` with the characters you want to analyze (e.g., `"aeiou"` for vowels).

3. Example:
    ```bash
    ./main.py book.txt abcdef
    ```
    This command analyzes the file `book.txt` and provides a word count along with the frequency of the characters `a`, `b`, `c`, `d`, `e`, and `f`.

---

## About

BookBot is a simple yet powerful tool for text analysis, ideal for processing books, articles, or any other textual data. Its modular design and robust error handling make it a reliable choice for text processing tasks.