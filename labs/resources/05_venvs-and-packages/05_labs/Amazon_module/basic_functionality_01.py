from amazon_paapi import AmazonAPI  # hypothetical wrapper

amazon = AmazonAPI(access_key, secret_key, partner_tag, region='us-east-1')

response = amazon.get_items(['B07N4M94CZ'])  # list of ASINs
for item in response.items:
    print(item.title, item.price, item.images)
