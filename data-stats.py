# statistics and monthly breakdown
# --- Overall Statistics ---
total_flights = len(df)
total_duration_hours = df['duration_hours'].sum()
total_distance_km = df['tracklog_distance_km'].sum()
total_altitude_gain = df['altitude_gain'].sum()

print("--- Overall Statistics ---")
print(f"Total Flights: {total_flights}")
print(f"Total Flight Hours: {total_duration_hours:.2f}")
print(f"Total Flight Distance (Tracklog): {total_distance_km:.2f} km")
print(f"Total Altitude Gain: {total_altitude_gain:.0f} m")
print("-" * 25)


# --- Statistics per Glider ---
print("\n--- Statistics per Glider ---")
stats_per_glider = df.groupby('glider_name').agg(
    flight_count=('id', 'count'),
    total_duration_hours=('duration_hours', 'sum'),
    total_distance_km=('tracklog_distance_km', 'sum'),
    total_altitude_gain=('altitude_gain', 'sum')
).reset_index()
print(stats_per_glider.to_markdown(index=False))
print("-" * 25)


# --- Statistics per Flight Area ---
print("\n--- Statistics per Flight Area ---")
stats_per_area = df.groupby('takeoff_area').agg(
    flight_count=('id', 'count'),
    total_duration_hours=('duration_hours', 'sum'),
    total_distance_km=('tracklog_distance_km', 'sum'),
    total_altitude_gain=('altitude_gain', 'sum')
).reset_index()
print(stats_per_area.to_markdown(index=False))
print("-" * 25)

# --- Statistics per Country ---
print("\n--- Statistics per Country ---")
stats_per_country = df.groupby('country').agg(
    flight_count=('id', 'count'),
    total_duration_hours=('duration_hours', 'sum'),
    total_distance_km=('tracklog_distance_km', 'sum'),
    total_altitude_gain=('altitude_gain', 'sum')
).reset_index()
print(stats_per_country.to_markdown(index=False))
print("-" * 25)


# --- Monthly Breakdown ---
# Aggregate data by month and year
monthly_stats = df.groupby(['year', 'month']).agg(
    flight_count=('id', 'count'),
    total_duration_hours=('duration_hours', 'sum'),
    total_distance_km=('tracklog_distance_km', 'sum'),
    total_altitude_gain=('altitude_gain', 'sum')
).reset_index()

# Create a proper date for sorting/plotting (using the first day of the month)
monthly_stats['month_start_date'] = pd.to_datetime(monthly_stats['year'].astype(str) + '-' + monthly_stats['month'].astype(str) + '-01')
monthly_stats.sort_values('month_start_date', inplace=True)
# Create a Year-Month label for clearer plotting
monthly_stats['year_month'] = monthly_stats['month_start_date'].dt.strftime('%Y-%m')
