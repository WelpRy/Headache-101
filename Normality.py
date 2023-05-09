import streamlit as st

st.set_page_config(page_title="Chemistry App", page_icon=":microscope:")

st.title("Chemistry App")

menu = ["Molarity Calculator", "Normality Calculator"]
choice = st.sidebar.selectbox("Select a tool", menu)

if choice == "Molarity Calculator":
    st.title("Molarity Calculator")

    volume = st.number_input("Enter the volume of the solution (in liters):", min_value=0.0, step=0.1)
    moles = st.number_input("Enter the number of moles of solute:", min_value=0.0, step=0.1)

    if st.button("Calculate"):
        molarity = moles / volume
        st.write(f"The molarity of the solution is {molarity:.2f} M")

elif choice == "Normality Calculator":
    st.title("Normality Calculator")

    # Input fields for molarity and valence
    molarity = st.number_input("Enter the molarity of the solution:", min_value=0.0, step=0.1)
    valence = st.number_input("Enter the valence of the solute:", min_value=1, step=1)

    # Calculate the normality based on the inputs
    normality = molarity * valence

    # Display the result
    if st.button("Calculate"):
        st.write(f"The normality of the solution is {normality:.2f} N")
