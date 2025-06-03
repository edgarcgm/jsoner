import json
from datetime import datetime

# Load the JSON data from a file
with open('total_data_tester.json', 'r') as file:
	data = json.load(file)


#########CUT####################
# Define the cutoff date
cutoff_date = datetime.strptime("2025-01-30", "%Y-%m-%d")

# Filter the data
filtered_data = [entry for entry in data if datetime.strptime(entry["DATE"], "%Y-%m-%d %H:%M") > cutoff_date]
#######CUT######################

#######INVERSE######################
'''
filtered_data = data[::-1]
'''
#######INVERSE######################

# Save the filtered data back to a JSON file
with open('total_data_tester.json', 'w') as file:
	json.dump(filtered_data, file, indent= 4, ensure_ascii = False)

print("Filtered data has been saved to 'filtered_data.json'.")
