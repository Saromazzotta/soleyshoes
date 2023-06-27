import requests


# url = "https://sneaker-database-stockx.p.rapidapi.com/getproducts"

# querystring = {"keywords":"yeezy ","limit":"5"}

# headers = {
# 	"X-RapidAPI-Key": "56c2bc8b30msh20ce65860904590p11203bjsn1ce9c783dc28",
# 	"X-RapidAPI-Host": "sneaker-database-stockx.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())

url = "https://the-sneaker-database.p.rapidapi.com/sneakers"

querystring = {"limit":"10"}

headers = {
	"X-RapidAPI-Key": "56c2bc8b30msh20ce65860904590p11203bjsn1ce9c783dc28",
	"X-RapidAPI-Host": "the-sneaker-database.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

def get_shoes():
    url = "https://the-sneaker-database.p.rapidapi.com/sneakers"

    querystring = {"limit":"20"}

    headers = {
	"X-RapidAPI-Key": "56c2bc8b30msh20ce65860904590p11203bjsn1ce9c783dc28",
	"X-RapidAPI-Host": "the-sneaker-database.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

    # shoes = []
    # for i in range(0,10,1):

    #     shoe = {
    #         'id': response.json()['results'][i]['id'],
    #         # 'brand': response.json()['results'][i]['brand'],
    #         # 'colorway': response.json()['results'][i]['colorway'],
    #         # 'marketValue': response.json()['results'][i]['estimatedMarketValue']
    #     }
    #     shoes.append(shoe)
    # return shoes

print(get_shoes())