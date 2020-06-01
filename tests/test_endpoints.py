import json

from conftest import MockResponse

class TestEndpoints:

    def test_geocoding_by_place_name(self, client, mock_response):
        url = '/geocoding_by_place_name'
        response = client.get(url)
        assert response.status_code == 400  # we send the query with no parameters

        response = client.get(url+'?place_name=testing')
        assert response.status_code == 200
        assert json.loads(response.data) == MockResponse.json()

    def test_get_place_name_by_coordenates(self, client, mock_response):
        url = '/geocoding_by_coordenates'
        response = client.get(url)
        assert response.status_code == 400  # we send the query witn no parameters

        response = client.get(url+'?lat=5.456456&lng=72.5465487')

        assert response.status_code == 200

        assert json.loads(response.data) == MockResponse.json()


    def test_get_distance(self, client):
        url = '/get_distance'
        response = client.get(url)
        assert response.status_code == 400

        response = client.get(
            url+'?lat_start_place=4.807186&lng_start_place=-75.6965098&lat_end_place=5.6613634&lng_end_place=-74'
                '.7683831')

        expected_response = {
          "result": 139.98408523428216
        }

        assert response.status_code == 200

        assert json.loads(response.data) == expected_response
