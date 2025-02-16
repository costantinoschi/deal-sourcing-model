 # Scoring algorithm
import pandas as pd

def calculate_score(row):
    return (row['Revenue Growth (%)'] * 0.6) + (row['EBITDA Margin (%)'] * 0.4)

def score_companies():
    df = pd.read_csv('data/processed_companies.csv')
    df['Score'] = df.apply(calculate_score, axis=1)
    df = df.sort_values(by='Score', ascending=False)
    df.to_csv('data/scored_companies.csv', index=False)
    print("Scored data saved to data/scored_companies.csv")

if __name__ == "__main__":
    score_companies()