import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

DATABASE_URI = "sqlite:///books.db"

def load_data():
    engine = create_engine(DATABASE_URI)
    df = pd.read_sql("SELECT * FROM books", con=engine)
    return df

def main():
    st.title("E-Commerce Data Pipeline Dashboard")
    
    df = load_data()
    st.write("### Raw Data", df)
    
    st.write("### Price Distribution")
    fig, ax = plt.subplots()
    ax.hist(df["price"], bins=20, color="skyblue", edgecolor="black")
    ax.set_xlabel("Price")
    ax.set_ylabel("Number of Books")
    st.pyplot(fig)
    
    st.write("### Rating Distribution")
    rating_counts = df["rating"].value_counts()
    st.bar_chart(rating_counts)
    
    st.write("### Top 10 Most Expensive Books")
    top10 = df.sort_values(by="price", ascending=False).head(10)
    st.table(top10[["title", "price", "rating", "availability"]])

if __name__ == "__main__":
    main()