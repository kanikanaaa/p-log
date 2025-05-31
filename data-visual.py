
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
                      text_auto='.1f', # Display values with 1 decimal place
                      color_discrete_sequence =['forestgreen']) #change color
fig_duration.update_layout(xaxis_tickangle=-45)
fig_duration.show()

# Plot Flight Distance per Month
#fig_distance = px.bar(monthly_stats, x='year_month', y='total_distance_km',
#                      title='Total Flight Distance (km) per Month',
#                      labels={'year_month': 'Month', 'total_distance_km': 'Total Distance (km)'},
#                      text_auto='.1f',
#                      color_discrete_sequence =['lightpink'])
#fig_distance.update_layout(xaxis_tickangle=-45)
#fig_distance.show()

# Plot Altitude Gain per Month
# fig_altitude = px.bar(monthly_stats, x='year_month', y='total_altitude_gain',
#                      title='Total Altitude Gain (m) per Month',
#                      labels={'year_month': 'Month', 'total_altitude_gain': 'Total Altitude Gain (m)'},
#                      text_auto='.0f', # Display integer values
#                      color_discrete_sequence =['lightpink'])
#fig_altitude.update_layout(xaxis_tickangle=-45)
#fig_altitude.show()


# export the above visualization as an image file
!pip install -U kaleido

import os

# Export visualizations as image files
fig_count.write_image('flights_per_month.png')
fig_duration.write_image('duration_per_month.png')
print("Visualizations exported as PNG images.")

# export all the visualizations as one image file

from PIL import Image

# Define the paths to the saved image files
image_paths = [
    'flights_per_month.png',
    'duration_per_month.png',
]

# Define the output image path
output_image_path = 'drive/MyDrive/p-log/'+ filename +'-all_visualizations.png'

# Open the images
images = [Image.open(img_path) for img_path in image_paths]

# Calculate the total width and height for the combined image
# We'll stack them vertically
total_width = max(img.width for img in images)
total_height = sum(img.height for img in images)

# Create a new blank image with the calculated dimensions
combined_image = Image.new('RGB', (total_width, total_height), color = (255, 255, 255)) # White background

# Paste the images into the combined image, stacking them vertically
y_offset = 0
for img in images:
    combined_image.paste(img, (0, y_offset))
    y_offset += img.height

# Save the combined image
combined_image.save(output_image_path)

print(f"\nAll visualizations exported as a single image: {output_image_path}")

# Optional: Display the combined image (won't work directly in Colab output,
# but the file is saved)
# from IPython.display import display
# display(combined_image)
