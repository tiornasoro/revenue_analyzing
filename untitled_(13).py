# -*- coding: utf-8 -*-
"""Untitled (13).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c3G7xMf9gLTDKsM6NKBZ96sHVWh9A2oj
"""

!pip install yfinance==0.1.67
!pip install pandas==1.3.3
!pip install requests==2.26.0
!mamba install bs4==4.10.0 -y
!pip install plotly==5.3.1
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y
!pip install lxml==4.6.4
!pip install nbformat==4.2.0
!pip install --upgrade nbformat
!pip install plotly==5.3.1

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

"""First Question"""

tesla=yf.Ticker('TSLA')
tesla_data=tesla.history(period='max')
tesla_data.head()

tesla_data.reset_index(inplace=True)
#tesla_data.head()

"""Second Question

Save the text of the response as a variable named html_data.
"""

#!mamba install html5lib==1.1 -y

url=" https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue. "
html_data = requests.get(url).text

"""Parsing the html data using beautiful_soup."""

soup = BeautifulSoup(html_data, "html.parser")

import pandas as pd
tesla_revenue  =pd.DataFrame(columns=["Date","Revenue"])
for row in soup.find("tbody").find_all('tr'):
    col=row.find_all("td")
    date=col[0].text
    revenue=col[1].text
    
    tesla_revenue=tesla_revenue.append({"Date":date,"Revenue":revenue},ignore_index=True)
    
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue.reset_index(inplace=True)
#tesla_revenue.shape
tesla_revenue.tail()

#!pip install nbformat==4.2.0
#tesla_data.plot(x="Date", y="Volume")

"""GME_data"""

gme=yf.Ticker('GME')
gme_data=gme.history(period='max')
gme_data.reset_index(inplace=True)
gme_data.head()

gme_data.reset_index(inplace=True)
#tesla_data.plot(x="Date", y="Volume")

"""GME_Revenue"""

#url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_datas = requests.get(url).text
soup = BeautifulSoup(html_datas, "html.parser")

#import pandas as pd
gme_revenue  =pd.DataFrame(columns=["Date","Revenue"])
for row in soup.find("tbody").find_all('tr'):
    col=row.find_all("td")
    date=col[0].text
    revenue=col[1].text
    gme_revenue=tesla_revenue.append({"Date":date,"Revenue":revenue},ignore_index=True)
    
    
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")
gme_revenue.dropna(inplace=True)

gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

gme_revenue.tail()

#!pip install nbformat==4.2.0
#!pip install --upgrade nbformat

#def make_graph(stock_data, revenue_data, stock):
def make_graph(tesla_data, tesla_revenue, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    tesla_data_specific = tesla_data[tesla_data.Date <= '2021--06-14']
    tesla_revenue_specific = tesla_revenue[tesla_revenue.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(tesla_data_specific.Date, infer_datetime_format=True), y=tesla_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(tesla_revenue_specific.Date, infer_datetime_format=True), y=tesla_revenue_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
    
make_graph(tesla_data, tesla_revenue, 'stock')

def make_graph(gme_data, gme_revenue, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    gme_data_specific = gme_data[gme_data.Date <= '2021--06-14']
    gme_revenue_specific = gme_revenue[gme_revenue.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(gme_data_specific.Date, infer_datetime_format=True), y=gme_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(gme_revenue_specific.Date, infer_datetime_format=True), y=gme_revenue_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
    
make_graph(gme_data, gme_revenue, 'stock')