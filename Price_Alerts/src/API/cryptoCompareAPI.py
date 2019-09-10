import urllib.request
import json


class CryptoCompareAPI:

    # todo: make environment variable like so..
    # API_KEY_CRYPCOMP = os.environ['API_KEY_CRYPCOMP']

    API_KEY_CRYPCOMP = 'YOUR API KEY'

    @staticmethod
    def get_current_price(from_currency, to_currency='USD'):
        url = 'https://min-api.cryptocompare.com/data/price?fsym=' + from_currency + '&tsyms=' + to_currency\
              + '&api_key=' + CryptoCompareAPI.API_KEY_CRYPCOMP

        fp = urllib.request.urlopen(url)
        js = fp.read()
        fp.close()
        parsed_data = json.loads(js)

        return parsed_data
