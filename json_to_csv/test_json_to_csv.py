from json_csv import JsonToCsv


json_file = 'sample.json'
csv_file = 'output.csv'

# Create an instance of the class
converter = JsonToCsv(json_file, csv_file)

try:
    converter.load_json()
    print("JSON data loaded successfully.")
    print(converter.json_data)
except Exception as e:
    print(f"An error occurred during conversion: {e}")