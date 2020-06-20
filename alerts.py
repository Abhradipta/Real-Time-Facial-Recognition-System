import requests

def alert(x):

    url = "https://www.fast2sms.com/dev/bulk"

    payload = "sender_id=FSTSMS&message=Unidentified tried to access system&language=english&route=p&numbers="+x

    headers = {
    'authorization': "3BxnvGSzYmNQETVsZ1k9uOAFHryIKqL4562ghtJfMoe8aiXWwcVIdS9iP705WC8LDEAzenRjYgO1tQpJ",
    'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache",}

    response = requests.request("POST", url, data=payload, headers=headers)
