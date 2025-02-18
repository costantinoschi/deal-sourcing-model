 # Flask app for deployment
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('data/scored_companies.csv')
    return render_template('dashboard.html', data=df.to_html())

if __name__ == "__main__":
    app.run(debug=True)