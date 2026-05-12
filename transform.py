import pandas as pd
from datetime import datetime


def validate_data(df):
    if df.empty:
        raise ValueError("DataFrame is empty.")
    if not df["temperature"].between(-60, 60).all():
        raise ValueError("Temperature values are out of realistic range.")
    if df["city"].isnull().any():
        raise ValueError("City name cannot be null.")
    return True # If all checks pass, return True


def clean_weather_data(json_data):
    clean_data = {
        "city": json_data["name"],
        "temperature": json_data["main"]["temp"],
        "condition": json_data["weather"][0]["description"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    df =  pd.DataFrame([clean_data])

    # Return only if validation passes, otherwise raise an error
    if validate_data(df):
        return df
    else:
        raise ValueError("Data validation failed.")