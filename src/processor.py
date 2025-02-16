 # Data processing script
import pandas as pd

def process_data():
    df = pd.read_csv('data/companies.csv')
    # Add dummy data for demonstration
    df['Revenue Growth (%)'] = [20, 15, 10]
    df['EBITDA Margin (%)'] = [25, 30, 20]
    df.to_csv('data/processed_companies.csv', index=False)
    print("Processed data saved to data/processed_companies.csv")

if __name__ == "__main__":
    process_data()