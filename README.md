# Streamlit YFinance App

This is a simple Streamlit app that fetches stock market data using the `yfinance` library.

## Features

- Search stock ticker symbols
- Fetch historical stock price data
- View recent market data in a table
- Visualize closing prices with a chart

## Tech Stack

- Python
- Streamlit
- yfinance
- pandas
- plotly

## Project Files

- `app.py` – main Streamlit app
- `requirements.txt` – required Python libraries
- `README.md` – project documentation

## How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/streamlit-yfinance-app.git
   ```

2. Move into the project folder:
   ```bash
   cd streamlit-yfinance-app
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Deployment

This app is intended to be deployed using Streamlit Community Cloud by connecting this GitHub repository and selecting `app.py` as the main file. Streamlit Community Cloud supports deploying apps directly from GitHub repositories. [web:13][web:19]

## Example Tickers

You can try these ticker symbols:

- AAPL
- MSFT
- GOOGL
- TSLA
- RELIANCE.NS
- TCS.NS

## Notes

Market data is fetched through the `yfinance` Python library, which is commonly used to access Yahoo Finance data in Streamlit stock apps. [web:20][web:17]
