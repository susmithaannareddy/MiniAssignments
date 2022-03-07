import requests

payload={
    "phone": "9177095571",
    "otp": 646038
}
resp=requests.delete("https://hbs-ob-stage.herokuapp.com/user")
print(resp)