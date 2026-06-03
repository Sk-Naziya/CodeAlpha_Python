import streamlit as st

st.set_page_config(
    page_title="Stock Portfolio Tracker",
    page_icon="📈",
    layout="centered"
)

st.title("📈 Stock Portfolio Tracker")

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 200
}

st.subheader("Enter Stock Details")

total_value = 0

for stock, price in stock_prices.items():

    qty = st.number_input(
        f"{stock} (${price})",
        min_value=0,
        step=1
    )

    total_value += qty * price

st.markdown("---")

st.metric(
    "Total Investment Value",
    f"${total_value}"
)

if st.button("Generate Report"):

    report = f"Total Investment Value: ${total_value}"

    with open(
        "portfolio_report.txt",
        "w"
    ) as file:

        file.write(report)

    st.success(
        "Report Saved Successfully!"
    )