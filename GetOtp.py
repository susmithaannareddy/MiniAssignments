import requests
payload ={
    "phone": "9177095571"

}
resp=requests.post("https://hbs-ob-stage.herokuapp.com/get_register_otp", data=payload)
print(resp)
print(resp.json())