import streamlit as st

# Function to format numbers to Indonesian Rupiah format
def to_rupiah(number):
    rupiah_format = "Rp {:,.0f}".format(number).replace(",", ".")
    return rupiah_format

# Function to calculate monthly profit
def calculate_monthly_profit(initial_capital, annual_interest_rate, reinvest_threshold=1000000, months=12):
    capital = initial_capital  # Capital in regular units
    monthly_interest_rate = annual_interest_rate / 12 / 100  # Convert annual interest to monthly
    monthly_profits = []
    total_interest_accumulated = 0  # Accumulated interest

    results = []  # To store the monthly results for display

    for month in range(1, months + 1):
        # Calculate interest
        interest = capital * monthly_interest_rate
        total_interest_accumulated += interest

        # Reinvest if accumulated interest reaches or exceeds 1,000,000
        if total_interest_accumulated >= reinvest_threshold:
            reinvestment_units = total_interest_accumulated // reinvest_threshold  # Full units of 1,000,000 to reinvest
            capital += reinvestment_units * reinvest_threshold  # Add the full units of 1,000,000 to capital
            total_interest_accumulated -= reinvestment_units * reinvest_threshold  # Subtract the reinvested interest

        monthly_profits.append(interest)
        
        # Append formatted results
        results.append(f"Month {month}: Interest = {to_rupiah(interest)}, Capital = {to_rupiah(capital)}, Accumulated Interest = {to_rupiah(total_interest_accumulated)}")

    return results

# Streamlit App Interface
st.title("Investment Profit Calculator")

# Input fields for capital, months, and interest rate
capital = st.number_input("Initial Capital (Rp)", min_value=1000000, step=1000000, value=1000000)
months = st.number_input("Number of Months", min_value=1, step=1, value=12)
interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, step=0.1, value=6.5)

# Button to trigger the calculation
if st.button("Calculate"):
    results = calculate_monthly_profit(initial_capital=capital, annual_interest_rate=interest_rate, months=months)
    
    # Display the results
    st.subheader("Monthly Profit Breakdown")
    for result in results:
        st.write(result)
