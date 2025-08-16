
# Unit Converter Application

An **interactive Streamlit-powered unit converter** that makes converting between various units effortless. Handle conversions across **7 categories** with intuitive UI, robust validation, and handy clipboard support.

---

## Features

* **Seven conversion categories**:
  Length, Weight, Temperature, Volume, Speed, Time, and Energy
  Examples include meters/kilometers/miles, kilograms/pounds/ounces, Celsius/Fahrenheit/Kelvin, liters/gallons/cups, m/s–mph–knots, seconds/minutes/hours/days, joules/calories/watt-hours .

* **Input validation and error handling**:
  Ensures meaningful conversions by preventing invalid input such as negative values where inappropriate or selecting identical units .

* **One-click copy to clipboard**:
  Effortlessly copy conversion results using `pyperclip` (note: some platforms may require additional clipboard support) .

* **Session state management**:
  Retains previous conversion results for seamless interactions .

---

## Project Structure

```
Project_01_unit_converter_app/
│
├── main.py               # Streamlit UI and app logic  
├── unit_converter_utils.py  # Underlying conversion logic & unit definitions  
├── requirements.txt      # Python dependencies  
└── __pycache__/          # Cache directory
```



---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/HasnainDevMaster/Project_01_unit_converter_app.git
   cd Project_01_unit_converter_app
   ```

2. **(Optional) Create and activate a virtual environment**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```



---

## Usage

1. Launch the app:

   ```bash
   streamlit run main.py
   ```

2. Open the local Streamlit URL (typically `http://localhost:8501`).

3. In the interface, select:

   * A conversion **category**
   * **From** and **To** units
   * A **value** to convert

4. Click **Convert** to display the result — then optionally use the **“Copy to Clipboard”** button to copy it .

---

## Notes / Troubleshooting

* Clipboard support leverages `pyperclip`. Some operating systems may lack native support; consult the [pyperclip documentation](https://pyperclip.readthedocs.io) for platform-specific instructions .

* Negative values are prohibited for categories where they don't logically apply (e.g., Length, Weight) .

* Conversion logic and unit definitions are maintained in `unit_converter_utils.py` for easy updates and expansions .

---

## Contributing

Contributions are welcome! Suggestions include:

* Adding more unit categories or unit types
* Improving validation and error-handling
* UI/UX enhancements and additional features

Feel free to open issues or submit PRs.

---

## License

This project is open-sourced under the **MIT License**.

---

### Summary

This Streamlit Unit Converter offers a clean, user-friendly interface for quick and precise unit conversions across multiple categories. It balances functionality with simplicity — perfect for both casual users and developers alike.
