import requests
payload ={
    "name": "Susmitha",
    "phone": "+9177095571",
    "email": "asusmitha@hashedin.com",
    "password": "admin",
    "otp": 329785

}
resp=requests.post("https://hbs-ob-stage.herokuapp.com/user", data=payload)
print(resp)
print(resp.json())