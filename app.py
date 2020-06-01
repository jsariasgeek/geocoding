import json

from flask import Flask, request

from helpers.geocoding_helper import GeoCodingAPIHelper

app = Flask(__name__)

geocoding_helper = GeoCodingAPIHelper()

@app.route('/geocoding_by_place_name')
def geocoding_by_place_name():
    """
       :return: Coordenates Given A Place Name or Address
       """
    place_name = request.args.get('place_name')
    if not place_name:
        return ('You need to pass the place name as parameter', 400)

    results = geocoding_helper.query_api(place_name)
    return json.dumps({
        'results':results
    })

@app.route('/geocoding_by_coordenate')
def get_place_name_by_coordenates():
    """
    lat:latitude,
    lng:longitude
    :return:Place name by coordenates
    """
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    if not lat or not lng:
        return "You need to pass the lat and lng args", 400
    results = geocoding_helper.get_place_by_coordenates(lat, lng)
    return {
        'results':results
    }

@app.route('/get_distance')
def get_distance_between_two_places():
    lat_start_place = float(request.args.get('lat_start_place'))
    lng_start_place = float(request.args.get('lng_start_place'))
    lat_end_place = float(request.args.get('lat_end_place'))
    lng_end_place = float(request.args.get('lng_end_place'))
    """
    :return: This endpoint returns the distance between two places
    """
    parameters_are_valid = lat_start_place and lng_start_place and lat_end_place and lng_end_place

    if not parameters_are_valid:
        return "Please verify if you're sending all the required parameters", 400

    return json.dumps({
        'result': geocoding_helper.get_distance_between_two_places(
            lat_start_place,
            lng_start_place,
            lat_end_place,
            lng_end_place
        )
    })

if __name__ == "__main__":
    app.run('0.0.0.0')