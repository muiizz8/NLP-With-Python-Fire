# Wikipedia Noun Phrase Extractor

This project is a command-line tool that summarizes a Wikipedia page and extracts the noun phrases from the summary. It uses the `wikipedia` and `textblob` libraries to accomplish this.

## Setup

1.  **Install dependencies:**
    ```bash
    make install
    ```
    This will install the required Python packages and download the necessary NLTK corpora for `textblob`.

2.  **Activate your virtual environment if you are using one.**

## Usage

To use the tool, run the `wikiphrases.py` script with the name of the Wikipedia page you want to summarize as an argument.

```bash
python wikiphrases.py "Python (programming language)"
```

The script will then print a list of noun phrases found in the summary of the Wikipedia page.

## Development

This project uses the following tools for development:

*   `pytest` for testing
*   `pylint` for linting
*   `black` for code formatting

The following `make` commands are available:

*   `make install`: Install dependencies.
*   `make test`: Run tests.
*   `make lint`: Run the linter.
*   `make format`: Format the code.
*   `make all`: Run `install`, `lint`, and `test` in that order.

## How it Works

The script takes a search term for a Wikipedia page as input. It then uses the `wikipedia` library to find the page and get a summary of it. The summary is then passed to `textblob`, which is used to extract the noun phrases. The list of noun phrases is then printed to the console.
