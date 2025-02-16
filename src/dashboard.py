  # Streamlit dashboard
import streamlit as st
import pandas as pd

def load_data():
    return pd.read_csv('data/scored_companies.csv')

def main():
    st.title('Deal Sourcing Dashboard')
    df = load_data()
    st.write("Top Companies:")
    st.write(df)

if __name__ == "__main__":
    main()