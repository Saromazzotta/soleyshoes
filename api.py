import requests

url = "https://sneaker-database-stockx.p.rapidapi.com/getproducts"

querystring = {"keywords":"jordan 1","limit":"5"}

headers = {
	"X-RapidAPI-Key": "56c2bc8b30msh20ce65860904590p11203bjsn1ce9c783dc28",
	"X-RapidAPI-Host": "sneaker-database-stockx.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())