# Document Crawler

This project is a Python script that crawls and extracts content from a specified website.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Setting Up the Environment

1. Install Python:
   - Download and install Python from [python.org](https://www.python.org/downloads/)
   - Ensure that Python and pip are added to your system's PATH

2. Install virtualenv:
   ```
   pip install virtualenv
   ```

3. Clone the repository or download the 'doc_crawler.py' file:
   ```
   git clone https://github.com/yourusername/doc-crawler.git
   cd doc-crawler
   ```

4. Create a virtual environment:
   ```
   python -m venv venv
   ```

5. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

6. Install the required libraries:
   ```
   pip install requests beautifulsoup4
   ```

## Running the Crawler

1. Ensure your virtual environment is activated.

2. Run the script:
   ```
   python doc_crawler.py
   ```

3. When prompted, enter the URL of the website you want to crawl.

4. The extracted documents will be saved in the 'crawled_docs' directory.

## Deactivating the Virtual Environment

When you're done, you can deactivate the virtual environment:
```
deactivate
```

## Precautions

- This crawler can put significant load on websites. Use it responsibly.
- The current version does not respect robots.txt. Consider legal and ethical implications before use.
- The code may need modification for different website structures.

## Troubleshooting

If you encounter any issues:
1. Ensure Python is correctly installed and added to PATH.
2. Verify that you've activated the virtual environment before running the script.
3. Check your internet connection.
4. If you get a "ModuleNotFoundError", ensure you've installed all required libraries.

## License

This project is under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/doc-crawler/issues) if you want to contribute.