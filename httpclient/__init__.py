import urllib.request
import urllib.parse

class PayloadFormatException(Exception):
    pass

class HttpClient:

    @staticmethod
    def parse_payload(payload):
        if not type(payload) is dict:
            raise PayloadFormatException('payload must be {required} not {type}'.format(required=type({}),type=type(payload)))
        payload_parsed=urllib.parse.urlencode(payload)
        return payload_parsed
    @staticmethod
    def encode_payload(payload,charset='ascii'):
        payload_parsed=HttpClient.parse_payload(payload)
        payload_encoded=payload_parsed.encode(charset)
        return payload_encoded

    def __init__(self,base_url,timeout=15):
        self.base_url=base_url
        self.timeout=timeout
    
    def post(self,payload={},charset='utf-8'):
        payload_encoded=HttpClient.encode_payload(payload)
        response=urllib.request.urlopen(self.base_url,payload_encoded,timeout=self.timeout)
        response_data=response.read()
        response_decoded=response_data.decode(charset)
        return response_decoded
    
    def get(self,payload={},charset='utf-8'):
        payload_parsed=HttpClient.parse_payload(payload)
        response=urllib.request.urlopen(self.base_url+'?'+payload_parsed,timeout=self.timeout)
        response_data=response.read()
        response_decoded=response_data.decode(charset)
        return response_decoded