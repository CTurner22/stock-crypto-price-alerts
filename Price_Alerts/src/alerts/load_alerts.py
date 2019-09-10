import json


class LoadAlerts:

    list_all = []

    def __init__(self, input_file='src/AlertSettings.json'):
        # open json and load the desired alerts
        with open(input_file) as json_file:
            data = json.load(json_file).get('alerts')

            # parse the json to save as alerts
            if data is not None:
                lenient_float = lambda string: float(string) if string.strip() else None

                for alert in data:
                    self.list_all.append(Alert(
                        ticker=alert.get('ticker'),
                        lower_bound=lenient_float(alert.get('lower_bound')),
                        upper_bound=lenient_float(alert.get('upper_bound'))
                    ))


class Alert:

    def __init__(self, ticker, lower_bound=None, upper_bound=None):
        self.ticker = ticker
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        response = self.ticker

        if self.lower_bound is not None and self.upper_bound is not None:
            response += ' falls below ' + str(self.lower_bound) + ' or breaks above ' + str(self.upper_bound) + ' (USD)'
            return response

        if self.lower_bound is not None:
            response += ' falls below ' + str(self.lower_bound) + ' (USD)'

        if self.upper_bound is not None:
            response += ' breaks above ' + str(self.upper_bound) + ' (USD)'

        return response

    def within_bounds(self, price):
        response = True

        if self.lower_bound is not None:
            response = (price > self.lower_bound)
        if self.upper_bound is not None and response:
            response = (price < self.upper_bound)

        return response
