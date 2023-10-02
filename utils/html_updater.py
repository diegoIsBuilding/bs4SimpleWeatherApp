import json

def read_weather_data_from_json(filename="data/processed/weather_data.json"):
    """
    Read weather data from a JSON file.
    
    Args:
    - filename (str): Path to the JSON file containing weather data.
    
    Returns:
    - dict: Dictionary containing weather data.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def update_html_with_data(data, input_filename='templates/index.html', output_filename='templates/updated_index.html'):
    """
    Update the HTML with actual weather data.
    
    Args:
    - data (dict): Dictionary containing weather data.
    - input_filename (str): Path to the input HTML file with placeholders.
    - output_filename (str): Path to save the updated HTML file.
    """
    with open(input_filename, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Replace placeholders with actual data
    for key, value in data.items():
        html_content = html_content.replace(f'{{{{{key}}}}}', value)

    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(html_content)


if __name__ == "__main__":
    # Read the weather data from the JSON file
    weather_data = read_weather_data_from_json()

    # Update the HTML with the actual data
    update_html_with_data(weather_data)