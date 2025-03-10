import re
import streamlit as st

st.markdown(
    """
    <style>
   .stApp{
    background-color:#B0E0E6;} 
  h1 {
    color: #f63366;

    font-weight: bold;
}
    .stButton {
    color: #f63366;}

    [data-testid="stTextInput"] svg {
  
    color: #f63366 !important;
   
   
}



    </style>
    
""" ,
 unsafe_allow_html=True
)

st.title("🔐 Password Strength Checker")
st.write("Enter your password to check its strength.")
st.write("Password should be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character.")
st.write("Special characters include: !@#$%^&*")
def check_password_strength(password):
    score = 0
    feed_back   =  []
   
   
    if len(password) >= 8:
        score += 1
    else:
       feed_back.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feed_back.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feed_back.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feed_back.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
       st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
       st.error("❌ Weak Password - Improve it using the suggestions above.")

    if feed_back:
        for feedback in feed_back:
            st.write(feedback)
# Get user input
password = st.text_input("Enter your password:", type="password")
# check_password_strength(password)

# Button Click Handling
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

if st.button("Check Strength"):
    st.session_state.button_clicked = True

# Only run function when button is clicked
if st.session_state.button_clicked and password:
    check_password_strength(password)
elif st.session_state.button_clicked and not password:
    st.warning("⚠️ Please enter a password.")
    