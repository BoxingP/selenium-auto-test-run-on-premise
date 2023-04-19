import json
import urllib.request


class API(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54",
            "Accept": "application/json"
        }

    def send_request(self, url, headers=None):
        if headers is not None:
            self.headers.update(headers)
        try:
            req = urllib.request.Request(url=url, headers=self.headers)
            resp = urllib.request.urlopen(req)
            resp = resp.read().decode()
            if resp != '':
                data = json.loads(resp)
                return data
        except Exception as error:
            print(f"Error: {str(error)}")
        return None
