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
# print("-" * 25)

# --- Additional Analysis Ideas (Output as text) ---
# print("\n--- My records ---")
# Longest flight by duration
longest_flight_dur = df.loc[df['duration_hours'].idxmax()]
print(f"\nLongest Flight (Duration): {longest_flight_dur['duration_hours']:.2f} hours on {longest_flight_dur['date'].strftime('%Y-%m-%d')} from {longest_flight_dur['takeoff_area']}")

# Longest flight by distance
longest_flight_dist = df.loc[df['tracklog_distance_km'].idxmax()]
print(f"Longest Flight (Distance): {longest_flight_dist['tracklog_distance_km']:.2f} km on {longest_flight_dist['date'].strftime('%Y-%m-%d')} from {longest_flight_dist['takeoff_area']}")

# Highest Altitude Gain in a single flight
highest_gain = df.loc[df['altitude_gain'].idxmax()]
print(f"Highest Altitude Gain (Single Flight): {highest_gain['altitude_gain']:.0f} m on {highest_gain['date'].strftime('%Y-%m-%d')} from {highest_gain['takeoff_area']}")

# Average stats per flight
avg_duration = df['duration_hours'].mean()
avg_distance = df['tracklog_distance_km'].mean()
avg_altitude_gain = df['altitude_gain'].mean()
print(f"\nAverage Flight Duration: {avg_duration:.2f} hours")
print(f"Average Flight Distance: {avg_distance:.2f} km")
print(f"Average Altitude Gain: {avg_altitude_gain:.0f} m")

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


# export the above output as a text file

with open('drive/MyDrive/p-log/'+ filename + '-stats.txt', 'w') as f: #file name 変えたい
    # Redirect stdout to the file
    import sys
    original_stdout = sys.stdout
    sys.stdout = f

    # Your print statements here
    print("--- Overall Statistics ---")
    print(f"Total Flights: {total_flights}")
    print(f"Total Flight Hours: {total_duration_hours:.2f}")
    print(f"Total Flight Distance (Tracklog): {total_distance_km:.2f} km")
    print(f"Total Altitude Gain: {total_altitude_gain:.0f} m")
    # print("-" * 25)

    # --- Additional Analysis Ideas (Output as text) ---
    # print("\n--- My records ---")
    # Longest flight by duration
    longest_flight_dur = df.loc[df['duration_hours'].idxmax()]
    print(f"\nLongest Flight (Duration): {longest_flight_dur['duration_hours']:.2f} hours on {longest_flight_dur['date'].strftime('%Y-%m-%d')} from {longest_flight_dur['takeoff_area']}")

    # Longest flight by distance
    longest_flight_dist = df.loc[df['tracklog_distance_km'].idxmax()]
    print(f"Longest Flight (Distance): {longest_flight_dist['tracklog_distance_km']:.2f} km on {longest_flight_dist['date'].strftime('%Y-%m-%d')} from {longest_flight_dist['takeoff_area']}")

    # Highest Altitude Gain in a single flight
    highest_gain = df.loc[df['altitude_gain'].idxmax()]
    print(f"Highest Altitude Gain (Single Flight): {highest_gain['altitude_gain']:.0f} m on {highest_gain['date'].strftime('%Y-%m-%d')} from {highest_gain['takeoff_area']}")

    # Average stats per flight
    avg_duration = df['duration_hours'].mean()
    avg_distance = df['tracklog_distance_km'].mean()
    avg_altitude_gain = df['altitude_gain'].mean()
    print(f"\nAverage Flight Duration: {avg_duration:.2f} hours")
    print(f"Average Flight Distance: {avg_distance:.2f} km")
    print(f"Average Altitude Gain: {avg_altitude_gain:.0f} m")

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

    # Restore stdout
    sys.stdout = original_stdout
