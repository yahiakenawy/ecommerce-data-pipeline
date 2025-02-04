# E-Commerce Data Pipeline & Analysis

This repository contains a project that demonstrates a complete data pipeline. The project includes:

- **Scraping:** Extracts data from [Books to Scrape](http://books.toscrape.com/) using Python and BeautifulSoup.
- **Data Cleaning:** Processes and cleans the scraped data using Pandas.
- **Database Integration:** Inserts the clean data into a SQLite database using SQLAlchemy.
- **Visualization:** Uses Streamlit to create an interactive dashboard to visualize the data.

## Project Overview

This project is designed to showcase an end-to-end data pipeline for an e-commerce use case. It is ideal for demonstrating your skills in web scraping, data processing, database management, and interactive data visualization.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Project Structure
ecommerce-data-pipeline/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── scraper.py
├── data_cleaning.py
├── database_setup.py
└── dashboard.py


## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ecommerce-data-pipeline.git
   cd ecommerce-data-pipeline
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate      # On Windows: env\Scripts\activate
3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

4. **Run the Pipeline**
  Scrape the data, clean it, set up the database, and launch the dashboard with a single bash snippet:

    ```bash
    python scraper.py         # Scrapes the data and generates raw_books.csv.
    python data_cleaning.py   # Cleans the data and creates clean_books.csv.
    python database_setup.py  # Sets up the database by creating books.db.
    streamlit run dashboard.py  # Launches the Streamlit dashboard.
  Simply copy and paste these commands into your terminal (or save them in a bash script) to run the entire pipeline.











