# Profit-Price-Analysis-Dashboard-for-Tesla-and-GameStop-Stocks


## Overview

This project analyzes historical stock prices and revenue data of a given company (Tesla and GameStop). It fetches the stock price data from Yahoo Finance and scrapes revenue data from a specified URL. Both data sets are then visualized using interactive graphs with Plotly to provide insights into the company's performance over time.

## Technologies Used

- **Python**: The programming language used for data collection, processing, and visualization.
- **yfinance**: A library for downloading Yahoo Finance data.
- **pandas**: Used for data manipulation and cleaning.
- **requests & BeautifulSoup**: For scraping revenue data from a webpage.
- **Plotly**: A graphing library for creating interactive charts.

## Requirements

To run this project, you'll need to install the following Python libraries:

- yfinance
- pandas
- requests
- beautifulsoup4
- plotly

You can install these libraries by running:

```
pip install yfinance pandas requests beautifulsoup4 plotly
```

## Setup Instructions

1. **Clone this repository**:
   ```
   git clone https://github.com/Sayandip2005/Profit-Price-Analysis-Dashboard-for-Tesla-and-GameStop-Stocks.git
   cd Profit-Price-Analysis-Dashboard-for-Tesla-and-GameStop-Stocks
   ```

2. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run the script**:
   After setting up the environment and installing the dependencies, run the Python script to fetch the data and display the interactive plots:
   ```
   python stock_analysis.py
   ```

## Code Explanation

1. **Fetching Stock Data**:  
   The script uses the `yfinance` library to fetch historical stock data from Yahoo Finance for a given company. The stock data includes information like the closing price and date.

2. **Scraping Revenue Data**:  
   Revenue data is scraped from a specified URL using `requests` and `BeautifulSoup`. The revenue is cleaned and formatted before being merged with the stock data.

3. **Plotting the Data**:  
   The `plotly.graph_objects` library is used to create a subplot with two charts:
   - **Stock Price vs Date**: A plot showing the historical closing stock prices of the company.
   - **Revenue vs Date**: A plot showing the historical revenue data of the company.
   These two charts are displayed in one figure, and the user can interact with the plots.

## Usage

Once the script is run, it will display an interactive plot with the following:

- **Share Price vs Date**: A plot showing the historical closing share prices of the company.
- **Revenue vs Date**: A plot showing the historical revenue data of the company.

The x-axis represents the dates, and the y-axis represents the price (in USD) and revenue (in USD millions) for the stock price and revenue, respectively.



## Author

[Sayandip Sen]
 

---
