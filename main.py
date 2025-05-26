import streamlit as st
import pyperclip
from unit_converter_utils import convert_units, get_units

# --- Streamlit Page Config ---
st.set_page_config(page_title="🔄 Unit Converter Application", layout="centered")

# --- App Title ---
st.title("🔄 Unit Converter Application")

# --- Category Selection ---
st.markdown("### Select Conversion Category")
categories = ["Length", "Weight", "Temperature", "Volume", "Speed", "Time", "Energy"]
category = st.selectbox("Category", categories)

# --- Units ---
units = get_units(category)
from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)
value = st.number_input("Enter Value", value=0.0, format="%f")

# --- Convert Button ---
if st.button("Convert"):
    try:
        # Ensure a valid value is entered
        if value == 0.0:
            st.error("Please enter a value greater than 0 for conversion.")
        else:
            # Validate and convert
            result = convert_units(value, from_unit, to_unit, category)
            output_text = f"{value} {from_unit} = {round(result, 4)} {to_unit}"
            st.session_state["output_text"] = output_text  # Store result in session state
            st.success(output_text)

    except ValueError as ve:
        st.error(f"Validation Error: {str(ve)}")
    except Exception as e:
        st.error(f"Conversion Error: {str(e)}")

# --- Copy to Clipboard ---
if "output_text" in st.session_state and st.button("📋 Copy to Clipboard"):
    try:
        pyperclip.copy(st.session_state["output_text"])
        st.toast("Copied to clipboard!")
    except pyperclip.PyperclipException:
        st.error("Clipboard functionality is not available.")

# --- Input Validation ---
def validate_input(value, from_unit, to_unit, category):
    if not isinstance(value, (int, float)) or value is None:
        raise ValueError("Value must be a valid number.")
    if value < 0 and category in ["Length", "Weight", "Volume", "Speed", "Energy"]:
        raise ValueError("Value cannot be negative for the selected category.")
    if from_unit == to_unit:
        raise ValueError("From Unit and To Unit cannot be the same.")
    return True

# --- Result Generation ---
def generate_result(value, from_unit, to_unit, category):
    validate_input(value, from_unit, to_unit, category)
    return convert_units(value, from_unit, to_unit, category)
