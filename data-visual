# visualization based on outcome of data-stats
# --- Visualization ---
print("\n--- Generating Visualizations ---")

# Plot Flight Count per Month
fig_count = px.bar(monthly_stats, x='year_month', y='flight_count',
                   title='Number of Flights per Month',
                   labels={'year_month': 'Month', 'flight_count': 'Number of Flights'},
                   text_auto=True) # Display values on bars
fig_count.update_layout(xaxis_tickangle=-45)
fig_count.show()

# Plot Flight Duration per Month
fig_duration = px.bar(monthly_stats, x='year_month', y='total_duration_hours',
                      title='Total Flight Duration (Hours) per Month',
                      labels={'year_month': 'Month', 'total_duration_hours': 'Total Duration (Hours)'},
                      text_auto='.1f') # Display values with 1 decimal place
fig_duration.update_layout(xaxis_tickangle=-45)
fig_duration.show()

# Plot Flight Distance per Month
fig_distance = px.bar(monthly_stats, x='year_month', y='total_distance_km',
                      title='Total Flight Distance (km) per Month',
                      labels={'year_month': 'Month', 'total_distance_km': 'Total Distance (km)'},
                      text_auto='.1f')
fig_distance.update_layout(xaxis_tickangle=-45)
fig_distance.show()

# Plot Altitude Gain per Month
fig_altitude = px.bar(monthly_stats, x='year_month', y='total_altitude_gain',
                      title='Total Altitude Gain (m) per Month',
                      labels={'year_month': 'Month', 'total_altitude_gain': 'Total Altitude Gain (m)'},
                      text_auto='.0f') # Display integer values
fig_altitude.update_layout(xaxis_tickangle=-45)
fig_altitude.show()
