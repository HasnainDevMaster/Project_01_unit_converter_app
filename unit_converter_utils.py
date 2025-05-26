def convert_units(value, from_unit, to_unit, category):
    conversions = {
        "Length": {
            "meters": 1,
            "kilometers": 1000,
            "centimeters": 0.01,
            "millimeters": 0.001,
            "miles": 1609.34,
            "yards": 0.9144,
            "feet": 0.3048,
            "inches": 0.0254,
        },
        "Weight": {
            "kilograms": 1,
            "grams": 0.001,
            "milligrams": 0.000001,
            "pounds": 0.453592,
            "ounces": 0.0283495,
        },
        "Temperature": {
            "Celsius": "C",
            "Fahrenheit": "F",
            "Kelvin": "K",
        },
        "Volume": {
            "liters": 1,
            "milliliters": 0.001,
            "gallons": 3.78541,
            "quarts": 0.946353,
            "pints": 0.473176,
            "cups": 0.24,
            "fluid ounces": 0.0295735,
        },
        "Speed": {
            "meters/second": 1,
            "kilometers/hour": 0.277778,
            "miles/hour": 0.44704,
            "feet/second": 0.3048,
            "knots": 0.514444,
        },
        "Time": {
            "seconds": 1,
            "minutes": 60,
            "hours": 3600,
            "days": 86400,
        },
        "Energy": {
            "joules": 1,
            "kilojoules": 1000,
            "calories": 4.184,
            "kilocalories": 4184,
            "watt-hours": 3600,
            "kilowatt-hours": 3600000,
        },
    }

    if category == "Temperature":
        if from_unit == to_unit:
            return value
        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return value * 9/5 + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32

    else:
        base_unit = conversions[category][from_unit]
        target_unit = conversions[category][to_unit]
        return value * base_unit / target_unit

def get_units(category):
    return list({
        "Length": [
            "meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"
        ],
        "Weight": [
            "kilograms", "grams", "milligrams", "pounds", "ounces"
        ],
        "Temperature": [
            "Celsius", "Fahrenheit", "Kelvin"
        ],
        "Volume": [
            "liters", "milliliters", "gallons", "quarts", "pints", "cups", "fluid ounces"
        ],
        "Speed": [
            "meters/second", "kilometers/hour", "miles/hour", "feet/second", "knots"
        ],
        "Time": [
            "seconds", "minutes", "hours", "days"
        ],
        "Energy": [
            "joules", "kilojoules", "calories", "kilocalories", "watt-hours", "kilowatt-hours"
        ]
    }[category])
