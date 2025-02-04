import pandas as pd
import re

# Map textual ratings to numeric values
RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

def clean_price(price_str):
    # Remove currency symbol and convert to float
    price = re.sub(r"[^0-9.]", "", price_str)
    try:
        return float(price)
    except:
        return None

def clean_data(input_file="raw_books.csv", output_file="clean_books.csv"):
    df = pd.read_csv(input_file)
    
    # Clean price column
    df["price"] = df["price"].apply(clean_price)
    
    # Map ratings to numeric values
    df["rating_num"] = df["rating"].map(RATING_MAP)
    
    # Clean availability text (optional: extract number if available)
    df["availability"] = df["availability"].str.strip()
    
    # Remove any rows with missing price or rating
    df = df.dropna(subset=["price", "rating_num"])
    
    df.to_csv(output_file, index=False)
    print(f"Clean data saved to {output_file}")

if __name__ == "__main__":
    clean_data()