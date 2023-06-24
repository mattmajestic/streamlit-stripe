import streamlit as st
from streamlit.components.v1 import html
from datetime import timedelta
import webbrowser

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

    # Define a boolean variable to track the checkbox state
    terms_accepted = False

    # Render the checkbox for terms and conditions
    terms_accepted = st.checkbox("I agree to the Terms and Conditions")

    # Render the confirm button
    confirm_button = st.button("Confirm & Pay", disabled=not terms_accepted)

    # Show the modal with the legal terms when the terms button is clicked
    if terms_accepted:
        st.info(terms_and_conditions)
        confirm_button
    # Show the modal with the legal terms when the terms button is clicked
    if confirm_button:
        st.title("Payment")

        webbrowser.open_new_tab(stripe_checkout_url)
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
