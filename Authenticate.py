import requests

payload ={
    "phone": "+9177095571",
    "LoginType": "Passwrd",
    "password": "admin",

}
resp=requests.post("https://hbs-ob-stage.herokuapp.com/user")
print(resp)