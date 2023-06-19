import streamlit as st
from streamlit.components.v1 import html

# Set page configuration
st.set_page_config(
    page_title="30A Bramble Beach Rental",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Section 1: About the Space
st.title("30A Bramble Beach Rental!")
st.markdown("ℹ️ *3 bedrooms, pool, and close to the beach!*")

# Description of the house
st.subheader("About the House")
st.markdown("Our beach house is located in the beautiful 30A area of Florida. It offers the following amenities:")
st.markdown("🏖️ 3 bedrooms")
st.markdown("🏊 Private pool")
st.markdown("🎥 Major streaming services: Hulu Live, Netflix, Peacock")
st.markdown("🚶‍♂️ Just 0.25 miles from public beach access")
st.markdown("🍽️ Walking distance to restaurants and rental shops (bikes, golf carts, etc.)")

# Section 2: Book a Date to Visit the Beach
st.title("Book Your Stay")
st.markdown("🗓️ *Select the week you'd like to stay*")

# Display a calendar for selecting dates
selected_date = st.date_input("Select a week", help="Choose the starting date of your stay.")

# Section 3: Take Payments via Stripe
st.title("Payment")

# Stripe payment integration
stripe_js = """
<script async src="https://js.stripe.com/v3/buy-button.js"></script>
<stripe-buy-button
  buy-button-id="buy_btn_1NKjSSBY7L5WREAJ0wKVXsQB"
  publishable-key="pk_test_51IhaciBY7L5WREAJwVMBrcxv5kBExAigZ1Ajl8yCSjyTdP3lAhhZ6BsAUAImY9rCrklgbyV6Gj86qHXnSlY3F8l500KHDNOg3s"
></stripe-buy-button>
"""

html(stripe_js)
st.write("""""")
st.image("beach_payment.png", caption="Scan the QR code to pay")
