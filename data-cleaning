# Code by Gemini2.5Pro - import the data and analyze

import json
import pandas as pd
from datetime import timedelta
import re
import plotly.express as px
import plotly.graph_objects as go

# Load the JSON data
file_path = 'data2024.json'
with open(file_path, 'r') as f:
    data = json.load(f)

# Extract flight items
flights = data.get('items', [])

# Helper function to parse ISO 8601 duration (PTnHnMnS)
def parse_duration(duration_str):
    if not isinstance(duration_str, str) or not duration_str.startswith('PT'):
        return timedelta(0) # Return zero duration for invalid formats or None

    # Adjusted regex to handle optional hours, minutes, seconds and potential decimals
    match = re.match(r'PT(?:(\d+(?:\.\d+)?)H)?(?:(\d+(?:\.\d+)?)M)?(?:(\d+(?:\.\d+)?)S)?', duration_str)
    if not match:
        return timedelta(0) # Return zero if regex doesn't match

    hours, minutes, seconds = match.groups()
    total_seconds = 0
    if hours:
        total_seconds += float(hours) * 3600
    if minutes:
        total_seconds += float(minutes) * 60
    if seconds:
        total_seconds += float(seconds)

    return timedelta(seconds=total_seconds)


# Extract relevant data into a list of dictionaries
flight_data = []
for flight in flights:
    stats = flight.get('stats', {})
    glider = flight.get('glider', {})
    takeoff = flight.get('takeoff', {})
    point_start = flight.get('pointStart', {})
    countries = flight.get('countries', [])
    country = countries[0] if countries else None # Take the first country if available

    duration_td = parse_duration(stats.get('duration'))
    duration_hours = duration_td.total_seconds() / 3600 if duration_td else 0

    flight_data.append({
        'id': flight.get('id'),
        'date': pd.to_datetime(point_start.get('time')).date() if point_start.get('time') else None,
        'month': pd.to_datetime(point_start.get('time')).month if point_start.get('time') else None,
        'year': pd.to_datetime(point_start.get('time')).year if point_start.get('time') else None,
        'duration_str': stats.get('duration'),
        'duration_hours': duration_hours,
        'altitude_gain': stats.get('altitudeGain'),
        'tracklog_distance_m': stats.get('distanceTracklog'), # Assuming meters
        'glider_name': glider.get('nameCompact'),
        'takeoff_area': takeoff.get('name'),
        'country': takeoff.get('countryName') # Use country name from takeoff info
    })

# Create DataFrame
df = pd.DataFrame(flight_data)

# --- Data Cleaning & Preparation ---
# Convert distance to km
df['tracklog_distance_km'] = df['tracklog_distance_m'] / 1000.0

# Handle potential missing values (e.g., fill NaN in numerical columns with 0 if appropriate)
df['altitude_gain'].fillna(0, inplace=True)
df['tracklog_distance_km'].fillna(0, inplace=True)
df['duration_hours'].fillna(0, inplace=True)
# Fill missing categorical data with 'Unknown'
df['glider_name'].fillna('Unknown', inplace=True)
df['takeoff_area'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)

# Ensure date column is datetime type for proper sorting/filtering if needed later
df['date'] = pd.to_datetime(df['date'])
# Filter out entries without a valid date as they cause issues with monthly aggregation
df.dropna(subset=['date', 'month', 'year'], inplace=True)
df['month'] = df['month'].astype(int) # Ensure month is integer for plotting
df['year'] = df['year'].astype(int) # Ensure year is integer for plotting

