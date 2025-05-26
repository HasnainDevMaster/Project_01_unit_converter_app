# Unit Converter Application

A simple and interactive web application for converting values between different units of Length, Weight, Temperature, Volume, Speed, Time, and Energy. Built with [Streamlit](https://streamlit.io/) for a fast and user-friendly experience.

## Features

- Convert between a wide range of units in 7 categories:
  - Length (meters, kilometers, miles, etc.)
  - Weight (kilograms, pounds, ounces, etc.)
  - Temperature (Celsius, Fahrenheit, Kelvin)
  - Volume (liters, gallons, cups, etc.)
  - Speed (meters/second, miles/hour, knots, etc.)
  - Time (seconds, minutes, hours, days)
  - Energy (joules, calories, watt-hours, etc.)
- Input validation and error handling
- Copy conversion results to clipboard with one click

## Project Structure

```
main.py
unit_converter_utils.py
requirements.txt
__pycache__/
```

- **main.py**: Streamlit app UI and logic
- **unit_converter_utils.py**: Conversion logic and unit definitions
- **requirements.txt**: Python dependencies

## Installation

1. **Clone the repository** (or download the files):

   ```sh
   git clone https://github.com/HasnainDevMaster/Project_01_unit_converter_app
   cd Project_01_unit_converter_app
   ```

2. **Create and activate a virtual environment** (recommended):

   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app**:

   ```sh
   streamlit run main.py
   ```

2. **Open your browser** to the local URL provided by Streamlit (usually http://localhost:8501).

3. **Select a conversion category**, choose units, enter a value, and click "Convert".

4. **Copy the result** to your clipboard using the "📋 Copy to Clipboard" button.

## Notes

- The app uses [pyperclip](https://pypi.org/project/pyperclip/) for clipboard functionality. On some systems, you may need to install additional clipboard support (see [pyperclip documentation](https://pyperclip.readthedocs.io/en/latest/)).
- Negative values are not allowed for categories where they don't make sense (e.g., Length, Weight).
- The conversion logic is implemented in [`unit_converter_utils.py`](unit_converter_utils.py).

---
