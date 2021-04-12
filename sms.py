import requests
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=test&language=english&route=p&numbers=9999988888"

# Have to add numbers and apk key
headers = {
  'authorization': "",
  'Content-Type': "application/x-www-form-urlencoded",
  'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)