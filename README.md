# IMDb Top Rated Movie Scraper

This is a Python script that scrapes data from IMDb's Top Rated Movies list and displays details of a randomly selected movie. It utilizes the BeautifulSoup library for web scraping and requests library for making HTTP requests.

## Prerequisites

- Python 3.8 or higher
- Pip package manager

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. Change into the project directory:

   ```bash
   cd your-repository
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install beautifulsoup4 requests
   ```

## Usage

1. Open the `main.py` file and modify the URL variable if you want to scrape a different IMDb page.

2. Run the script:

   ```bash
   python main.py
   ```

   The script will fetch the IMDb page, extract movie details such as title, rating, year, and actors, and randomly select a movie to display its details.

   Example output:

   ```
   The Shawshank Redemption (1994) Rating: 9.2 Starring: Tim Robbins, Morgan Freeman, Bob Gunton
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Library for parsing HTML and XML documents.
- [Requests](https://docs.python-requests.org/en/latest/) - Library for making HTTP requests.
- [IMDb](http://www.imdb.com/chart/top) - Source of the movie data.

Feel free to modify and enhance the script according to your needs!
