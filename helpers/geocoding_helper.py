import os
import math
import requests


class GeoCodingAPIHelper:
    """
    This class enables us to get info from the open cage api
    https://opencagedata.com/api
    """
    API_KEY = os.environ.get('OPEN_CAGE_API_KEY')
    OPEN_CAGE_API_BASE_URL = 'https://api.opencagedata.com/geocode/v1/json?q='

    def __init__(self):
        if not self.API_KEY:
            raise Exception('An open cage api key was not found in the environment')

    def _get_full_uri(self, query):
        return self.OPEN_CAGE_API_BASE_URL + query + '&key=' + self.API_KEY

    def _extract_info_from_result(self, result):
        return {
            'formatted': result['formatted'],
            'geometry': result['geometry']
        }

    def query_api(self, query):
        uri = self._get_full_uri(query)
        response = requests.get(uri)
        results = response.json()['results']
        formatted_results = [self._extract_info_from_result(result) for result in results]
        return formatted_results

    def get_place_by_coordenates(self, lat, lng):
        """
        :param lat: latitud
        :param lng: longitud
        :return: the list or place or places associated with those coordenates
        """
        query = lat + '+' + lng
        results = self.query_api(query)
        return results

    def get_distance_between_two_places(self, lat1, lng1, lat2, lng2):
        """
        :param lat1: latitude in start_place
        :param lng1: longitude in start_place
        :param lat2: latitude in end_place
        :param lng2: longitude in end_place
        :return: the distance between the two points
        """
        EARTH_RADIO = 6373  # km
        lat1_rads = math.radians(lat1)
        lng1_rads = math.radians(lng1)
        lat2_rads = math.radians(lat2)
        lng2_rads = math.radians(lng2)

        diff_long = lng2_rads - lng1_rads
        diff_lat = lat2_rads - lat1_rads

        a = math.sin(diff_lat / 2) ** 2 + math.cos(lat1_rads) * math.cos(lat2_rads) * \
            math.sin(diff_long / 2) ** 2  # haversine formule

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = EARTH_RADIO * c
        return distance