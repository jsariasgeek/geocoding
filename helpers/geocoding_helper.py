import os
import json
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
            'formatted':result['formatted'],
            'geometry':result['geometry']
        }

    def query_api(self, query):
        uri = self._get_full_uri(query)
        response = requests.get(uri)
        results = response.json()['results']
        formatted_results = [self._extract_info_from_result(result) for result in results]
        return json.dumps(formatted_results)

    def get_place_by_coordenates(self, lat, lng):
        """
        :param lat: latitud
        :param lng: longitud
        :return: the list or place or places associated with those coordenates
        """
        query = lat + '+' + lng
        results = self.query_api(query)
        return results

    def get_distance_between_two_places(self, first_place, second_place):
        """
        :param first_place:
        :param second_place:
        :return:
        """
        pass






