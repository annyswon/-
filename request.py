import requests
res=requests.get('http://localhost:5000/user_id/Smirnov')
print(res.text)
