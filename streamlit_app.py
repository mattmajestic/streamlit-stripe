import streamlit as st

# Add CSS styles
st.markdown(
    """
    <style>
    .stApp {
        max-width: 800px;
        margin: 0 auto;
        padding-top: 2em;
        padding-bottom: 2em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Centered container
st.markdown('<div class="stApp">', unsafe_allow_html=True)

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
st.markdown("💳 *Enter your payment details to secure your reservation*")

# Stripe payment integration can be added here

# Display success message after payment
if st.button("Confirm Payment"):
    st.success("Payment successful! Your reservation is confirmed.")

# End of centered container
st.markdown('</div>', unsafe_allow_html=True)