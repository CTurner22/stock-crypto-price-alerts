#!/usr/bin/env python
from src.API.cryptoCompareAPI import CryptoCompareAPI
from src.API.twilioAPI import TwilioAPI
from src.alerts.load_alerts import LoadAlerts


def main():
    # first read in all alerts we need to check
    alerts = LoadAlerts().list_all

    # create list for alerts that require action
    action_required = []

    # check each alert
    for a in alerts:
        current_price = CryptoCompareAPI.get_current_price(a.ticker).get('USD')
        if not a.within_bounds(current_price):
            action_required.append({
                'alert': a,
                'current_price': current_price
            })

    # create message if action required
    if len(action_required) > 0:
        message = 'ALERT TRIGGERED:'
        for event in action_required:
            message += '\n' + str(event.get('alert')) + '..... Current Price is ' + str(event.get('current_price')) +\
                       ' (USD)'

        # send the text
        TwilioAPI.send_message(message)


        # todo: need to add logging and error handling for API calls


if __name__ == '__main__':
    main()
