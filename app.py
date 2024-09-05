from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Nominatim API for geocoding
NOMINATIM_API_URL = 'https://nominatim.openstreetmap.org/search'
NOMINATIM_REVERSE_API_URL = 'https://nominatim.openstreetmap.org/reverse'

@app.route('/')
def index():
    return render_template('map.html')

# Geocoding route to convert address to lat/lon
@app.route('/geocode', methods=['GET', 'POST'])
def geocode():
    if request.method == 'POST':
        address = request.form.get('address')
    else:
        address = request.args.get('address')  # For GET requests, you would retrieve the query parameter

    params = {
        'q': address,
        'format': 'json'
    }
    response = requests.get(NOMINATIM_API_URL, params=params)
    return response.json()


# Reverse Geocoding route to convert lat/lon to address
@app.route('/reverse_geocode', methods=['POST'])
def reverse_geocode():
    lat = request.form.get('lat')
    lon = request.form.get('lon')
    params = {
        'lat': lat,
        'lon': lon,
        'format': 'json'
    }
    response = requests.get(NOMINATIM_REVERSE_API_URL, params=params)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
