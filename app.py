import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📊 Company Financials AI Agent")

company = st.text_input("Enter company ticker (e.g., MSFT, RELIANCE.NS):")

if company:
    stock = yf.Ticker(company)
    info = stock.info
    
    data = {
        "Company": info.get("longName"),
        "Market Cap": info.get("marketCap"),
        "Revenue": info.get("totalRevenue"),
        "Net Income": info.get("netIncomeToCommon"),
        "EPS": info.get("trailingEps"),
        "Debt/Equity": info.get("debtToEquity"),
        "CEO": info.get("companyOfficers")[0]["name"] if info.get("companyOfficers") else None
    }
    
    df = pd.DataFrame(data.items(), columns=["Metric", "Value"])
    st.table(df)
