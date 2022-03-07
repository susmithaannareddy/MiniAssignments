import requests
payload={
    "phone": "9177095571",
}
resp=requests.post("https://hbs-ob-stage.herokuapp.com/get_otp")
print(resp)