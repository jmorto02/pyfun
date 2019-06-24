import requests


class Wikipedia(object):
    def __init__(self):
        self.base_url = "http://en.wikipedia.org/w/api.php"

    def get_wiki_information(self, search_criteria):
        params = {"action": "query",
                  "titles": search_criteria,
                  "format": "json",
                  "prop": "extracts",
                  "exintro": "explaintext"}

        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Response was not 200, was actually {response.status_code}.")
            return None


if __name__ == "__main__":
    w = Wikipedia()
    data = w.get_wiki_information("ramen")
    print(data)
