from flask import Flask, request, jsonify  # Import necessary modules from Flask
import requests  # Import the requests library to make HTTP requests

# Initialize Flask
app = Flask(__name__)  # Create a Flask application instance

# API Key and Base URL for GNews
API_KEY = 'f2a2e7e8828f903b5619f211c89f7c3c'  # Replace this with your actual API Key
BASE_URL = 'https://gnews.io/api/v4/'  # Base URL for the GNews API

@app.route('/news', methods=['GET'])  # Define a route for the '/news' endpoint, accepting only GET requests
def get_news():
    """Fetch news articles"""
    # Get the 'query' parameter from the request, or use 'news' as the default value
    query = request.args.get('query', 'news')
    
    # Get the 'max_results' parameter from the request, or use 10 as the default value
    max_results = request.args.get('max_results', 10)

    # Build the URL to make a request to the GNews API
    url = f"{BASE_URL}search?q={query}&token={API_KEY}&max={max_results}"
    
    # Make an HTTP GET request to the GNews API
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Return the JSON data received from the GNews API
        return jsonify(response.json())
    else:
        # Return an error message and the response's status code if the request fails
        return jsonify({'error': 'Error fetching news'}), response.status_code

# Run the Flask server if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask server in debug mode
