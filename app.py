import streamlit as st
from streamlit.components.v1 import html
from datetime import timedelta, datetime
import sqlite3
import os


# Get the Stripe publishable key from the environment variable
stripe_publishable_key = os.environ.get("STRIPE_KEY")

terms_and_conditions = '''
Beach House Rental Terms and Conditions:

1. Liability: The owners of the beach house shall not be held liable for any accidents, injuries, or losses incurred during the rental period. Guests assume full responsibility for their well-being and the well-being of their invitees.

2. Property Care: Guests are expected to treat the beach house and its contents with care and respect. Any damages caused by guests or their invitees will be the responsibility of the guests. Damages will be assessed and repaired at the guest's expense.

3. Damages and Invoicing: In the event of any damages to the property or its contents, guests will be invoiced for the repair or replacement costs. The invoiced amount will include a 15% markup on the actual cost of repair or replacement. Guests agree to promptly settle the invoice within the specified timeframe.

4. Pool Usage: If the beach house includes a pool, guests acknowledge that they assume all risks associated with pool usage. Guests must adhere to any pool safety rules and guidelines provided. The owners of the beach house shall not be held liable for any accidents or injuries related to pool usage.

5. Indemnification: Guests agree to indemnify and hold harmless the owners of the beach house from any claims, damages, or liabilities arising from the use of the property during the rental period.

Please read these terms and conditions carefully before confirming your reservation. By accepting the rental agreement, you acknowledge that you have read, understood, and agreed to abide by these terms and conditions.

If you have any questions or concerns regarding these terms, please contact us before confirming your reservation.
'''

stripe_checkout_url = "https://checkout.stripe.com/c/pay/cs_test_a1Gz1WBGJfRzECuAYa0YByCHyemYJqzQLUYrBuB4Z23nZbX64QQDfHBhF3#fidkdWxOYHwnPyd1blpxYHZxWjA0TG1kZmxHXDJJMFJXQERPclNIR3dmfXMwbkdAfURsYl80RG9pPXxGVm98UWFVNmlEbW1fM0d2RFBETGhcPHdGd25pYmd8UzNCbz0zdE1da1ZpXDZDPWkwNTVOTUFLSmI2dicpJ3VpbGtuQH11anZgYUxhJz8ncWB2cVo0MW41NmRiaUZgY3I0aVZhVFYnKSd3YGNgd3dgd0p3bGJsayc%2FJ21xcXV2Pyoqb3YrdnF3bHVgK2ZqaConKSdpamZkaWAnPydgaycpJ2BoZ2BhVmpwd2ZgJz8nZ3B8Wmdxa1o0S05vVlZHXDJJMFJXQERPNXJOU112VEcneCUl"

# Connect to the SQLite database
conn = sqlite3.connect('bookings.db')
c = conn.cursor()

# Create a table to store the booking dates if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                start_date TEXT,
                end_date TEXT,
                email TEXT,
                time TEXT
            )''')

terms_state = False

# Set page configuration
st.set_page_config(
    page_title="Streamlit Stripe Demo",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("About", "Booking and Payment","Terms & Conditions"))

# About page
if page == "About":
    st.title("30A Bramble Beach Rental")
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
    # Divide the page into two columns
    col1, col2 = st.columns(2)


    with col1:
        st.markdown("🗓️ *Select the week you'd like to stay*")
        # Display a calendar for selecting the start date of the week
        selected_start_date = st.date_input("Select the start date", help="Choose the starting date of your stay.")
        # Calculate the end date as one week from the start date
        selected_end_date = selected_start_date + timedelta(days=6)
        email = st.text_input("Email", "@your-email.com")
        # Display the selected week range
        st.markdown(f"Selected Week: {selected_start_date} to {selected_end_date}")
        # Render the checkbox for terms and conditions

    with col2:
        st.expander("View & Confirm Agreement")
        st.write(terms_and_conditions)
        if st.checkbox("I agree to the Terms and Conditions", value=terms_state):
            terms_state = True


    # Show the modal with the legal terms when the terms button is clicked
    if terms_state:
        with col1:
            confirm_button = st.button("Confirm & Pay", disabled=not terms_state)
        # Show the modal with the legal terms when the terms button is clicked
        if confirm_button:
            terms_state = False
            confirm_time = datetime.now().strftime("%H:%M:%S")
            c.execute("INSERT INTO bookings (start_date, end_date,email,time) VALUES (?, ?,?,?)",
                    (str(selected_start_date), str(selected_end_date), email, confirm_time))
            conn.commit()
            conn.close()
            stripe_js = """	
            <script async src="https://js.stripe.com/v3/buy-button.js"></script>	
            <stripe-buy-button	
            buy-button-id="buy_btn_1NKjSSBY7L5WREAJ0wKVXsQB"	
            publishable-key="{}"
            ></stripe-buy-button>	
            """.format(stripe_publishable_key)
            with col1:
                st.write("Thanks for confirming the terms and conditions!")
                st.write("""""")	
                st.title("Payment")
                html(stripe_js)
                st.image("beach_payment.png", caption="Scan the QR code to pay")
                url = "https://mainnet.demo.btcpayserver.org/api/v1/invoices?storeId=4r8DKKKMkxGPVKcW9TXB2eta7PTVzzs192TWM3KuY52e&price=100&currency=USD&defaultPaymentMethod=BTC"
                link='Pay wit BTC [via this link](https://mainnet.demo.btcpayserver.org/api/v1/invoices?storeId=4r8DKKKMkxGPVKcW9TXB2eta7PTVzzs192TWM3KuY52e&price=100&currency=USD&defaultPaymentMethod=BTC)'
                st.markdown(link,unsafe_allow_html=True)
                components.iframe(url,width = 300,height = 500, scrolling=True)
# Terms & Conditions page
if page == "Terms & Conditions":
        st.info(terms_and_conditions)