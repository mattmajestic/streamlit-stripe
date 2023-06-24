import streamlit as st
from streamlit.components.v1 import html
from datetime import timedelta

# Read the CSS file
css_file = open("styles.css", "r")
css_styles = css_file.read()
css_file.close()

# Set page configuration
st.set_page_config(
    page_title="30A Bramble Beach Rental",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("About", "Booking and Payment"))

# About page
if page == "About":
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

# Booking and Payment page
elif page == "Booking and Payment":
    st.title("Book Your Stay")
    st.markdown("🗓️ *Select the week you'd like to stay*")

    # Display a calendar for selecting the start date of the week
    selected_start_date = st.date_input("Select the start date", help="Choose the starting date of your stay.")

    # Calculate the end date as one week from the start date
    selected_end_date = selected_start_date + timedelta(days=6)

    # Display the selected week range
    st.markdown(f"Selected Week: {selected_start_date} to {selected_end_date}")

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
