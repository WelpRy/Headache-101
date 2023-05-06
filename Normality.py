import streamlit as st

def calculate_normality(volume, molarity, factor):
    """
    Calculates the normality of a chemical solution.
    """
    normality = molarity * factor / volume
    return normality

# Create the Streamlit app
st.title("Normality Calculator")
st.write("Enter the volume, molarity, and factor of the chemical solution to calculate its normality.")
volume = st.number_input("Volume (in liters)", min_value=0.0, step=0.1)
molarity = st.number_input("Molarity", min_value=0.0, step=0.1)
factor = st.number_input("Factor", min_value=0.0, step=0.1)
if st.button("Calculate"):
    normality = calculate_normality(volume, molarity, factor)
    st.write(f"The normality of the solution is {normality:.2f} N")
