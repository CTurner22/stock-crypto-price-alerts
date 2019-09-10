# Price alerts description

This project will check an api for crypto prices and then check `AlertSetting.json` to 
see if the prices set off any alerts. If so, it will format a custom sms message to alert 
you.

I wrote it because I hate missing big jumps in the market or a price move Ive been waiting
for. Similar stuff I found online was either via email or you had to buy a subscription. 


# Implementation
I added this to my cron table to run every 30 minutes.

`chmod u+x /path/to/script.py
`

`crontab -e `

add
`*/30 * * * * /path/to/script.py `

Note: You could also just loop it in a bash script with a pause.

I used the free api for crypto compare and twilio. Make sure to update the API keys in
the respectful classes for the APIs to work. 