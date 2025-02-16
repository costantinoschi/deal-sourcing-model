# Deal Sourcing and Screening Model

## Overview
This project is a **Deal Sourcing and Screening Model** designed to automate the identification and evaluation of potential investment opportunities for private equity firms. The tool scrapes company data from publicly available sources, processes and scores the data based on predefined criteria, and provides an interactive dashboard for visualization and decision-making.

The project is built using Python and leverages libraries such as **Pandas**, **Streamlit**, and **Flask** for data processing, visualization, and deployment.

---

## Features
1. **Web Scraping**: Automatically collects company data from sources like Crunchbase.
2. **Data Processing**: Cleans and structures raw data into a usable format.
3. **Scoring System**: Ranks companies based on criteria such as revenue growth, profitability, and industry attractiveness.
4. **Interactive Dashboard**: Provides a user-friendly interface for exploring top-ranked companies and key metrics.
5. **Deployment**: Includes a Flask app for deploying the dashboard as a web application.

---

## Installation
To set up the project, follow these steps:

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/deal-sourcing-model.git
   cd deal-sourcing-model

2. Install the required dependencies:
    `pip install -r requirements.txt`

3. Run the project scripts:
    - **Web Scraping**:
        `python src/scraper.py`
    - **Data Processing**:
        `python src/processor.py`
    - **Scoring Algorithm**:
        `python src/scorer/py`
    - **Streamlit Dashboard**:
        `streamlit run src/dashboard.py`
    - **Flask App**:
        `python src/app.py`

## Project Structure
deal-sourcing-model/
│
├── data/                   # Folder for storing raw and processed data
│   └── companies.csv
│
├── src/                    # Folder for Python scripts
│   ├── scraper.py          # Web scraping script
│   ├── processor.py        # Data processing script
│   ├── scorer.py           # Scoring algorithm
│   ├── dashboard.py        # Streamlit dashboard
│   └── app.py              # Flask app for deployment
│
├── templates/              # Folder for Flask HTML templates
│   └── dashboard.html
│
├── .gitignore              # Files to ignore in Git
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies

# Usage

## Web Scraping
The `scraper.py` script collects company data from Crunchbase (or other sources) and saves it to `data/companies.csv`.

## Data Processing
The `processor.py` script cleans and processes the scraped data, adding dummy metrics like revenue growth and EBITDA margin. The processed data is saved to `data/processed_companies.csv`.

## Scoring Algorithm
The `scorer.py` script ranks companies based on predefined criteria and saves the results to `data/scored_companies.csv`.

## Interactive Dashboard
The `dashboard.py` script provides an interactive dashboard using Streamlit. Run it with:

bash
Copy
`streamlit run src/dashboard.py`

## Flask App
The `app.py` script deploys the dashboard as a web application using Flask. Run it with:

bash
Copy
`python src/app.py`

## Dependencies

The project relies on the following Python libraries:

### Pandas: Data manipulation and analysis.
### NumPy: Numerical computations.
### BeautifulSoup4: Web scraping.
### Requests: HTTP requests.
### Scrapy: Advanced web scraping.
### SpaCy: Natural language processing.
### Dash: Interactive web applications.
### Streamlit: Rapid dashboard development.
### Flask: Web application framework.
### python-dotenv: Environment variable management.

## Contributing

Contributions are welcome! If you’d like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to the branch.
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Crunchbase: For providing publicly available company data.

Python Community: For developing and maintaining the libraries used in this project.

## Contact
For questions or feedback, please contact:

**Costantinos C.** (author)

**Email**: cachiamba@gmail.com

**GitHub**: costantinoschi