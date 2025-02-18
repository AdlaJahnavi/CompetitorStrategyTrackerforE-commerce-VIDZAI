from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/weather/<city>')
def get_weather(city):
    # Mock data for demonstration
    weather_data = {
        "New York": {"temperature": 15, "condition": "Cloudy"},
        "Los Angeles": {"temperature": 25, "condition": "Sunny"},
        "Chicago": {"temperature": 10, "condition": "Rainy"},
        "Mumbai": {"temperature": 30, "condition": "Humid"}
    }
    
    city = city.title()  # Capitalize city names to match keys
    if city in weather_data:
        return jsonify({"city": city, "weather": weather_data[city]})
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
