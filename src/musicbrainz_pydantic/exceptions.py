import requests


class MBRequestError(Exception):
    def __init__(self, response: requests.Response):
        self.response = response
        response_dict = {"help": "", "error": response.text}
        try:
            response_dict.update(response.json())
        except Exception:
            pass
        self.help = response_dict["help"]
        self.error = response_dict["error"]
        self.status_code = response.status_code
        self.url = response.url
        super().__init__(response_dict["error"])
