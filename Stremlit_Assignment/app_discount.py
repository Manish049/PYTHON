import streamlit as st

st.title("Price Calculator")

# Input: Product price
price = st.number_input("Enter product price:", min_value=0.0, step=1.0)

# Input: Discount percentage
discount = st.slider("Select discount percentage:", min_value=0, max_value=50, value=10)

if st.button("Calculate Discount"):
    final_price = price * (1 - discount / 100)
    st.success(f"Original Price: {price}\nDiscount: {discount}%\nFinal Price: {final_price}")
    # Optional: Show comparison table
    st.table([["Before", price], ["After", final_price]])
