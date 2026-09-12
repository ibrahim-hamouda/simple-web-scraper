# Book Data Web Scraper

A robust Python-based web scraper built to extract product data from [Books to Scrape](https://books.toscrape.com/). This project efficiently scrapes book titles and prices, cleans text encoding anomalies, securely stores the information into a relational database, and exports it for data analysis.

## 🚀 Features

- **Data Extraction:** Navigates and parses HTML structures using `requests` and `BeautifulSoup4`.
- **Data Cleaning:** Automatically handles and resolves UTF-8 encoding issues (e.g., formatting the `£` symbol correctly) to ensure clean data extraction.
- **Robust Error Handling:** Utilizes `try-except` blocks and assertions to prevent runtime crashes if target HTML elements are missing.
- **Database Integration:** Dynamically creates and populates a SQLite database (`books.db`) using secure parameterized queries (placeholders) to store scraped data.
- **Data Export:** Leverages `pandas` to generate a clean, Excel-compatible CSV file (`books_data.csv`).

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** `requests`, `bs4` (BeautifulSoup), `sqlite3`, `pandas`

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install required dependencies:**
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

3. **Run the scraper:**
   ```bash
   python main.py
   ```

## 📁 Output Files

Upon successful execution, the script generates two files:
- `books.db`: A SQLite database containing a `books` table with `title` and `price` columns.
- `books_data.csv`: A formatted CSV file ready for data analysis.

## 👨‍💻 Author

**Ibrahim Alaa El-Din**  
*Communication Engineering Student at the Egyptian Chinese College for Applied Technology*  
[LinkedIn Profile](https://www.linkedin.com/in/your-profile-link) | [GitHub](https://github.com/your-username)