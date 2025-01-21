import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.content 

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)