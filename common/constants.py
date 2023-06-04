import urllib

POSITIONSTACK_APIKEY = "7dfab93e584588c05b49a91c5e6460a9"
POSITIONSTACK_ENDPOINT = "http://api.positionstack.com/v1/forward"
MONGO_URI = "mongodb+srv://alonm91:" + urllib.parse.quote_plus("DkbVpsGniJYoVgJE") + "@cluster0.ygbbobb.mongodb.net" \
                                                                               "/?retryWrites=true&w=majority&authSource=admin"
MONGO_DB_NAME = "mydatabase"
OPENAI_APIKEY = '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'
OPENAI_PROMPT = 'Given the apartment rental below can you provide the following details in a JSON object (dont ignore newlines):' \
                 ' address (as a string in english), price (only number), number of rooms, elevator, pets allowed, ' \
                 'date of move-in(date format), which floor, mediation?\n{}\nThe resulting JSON should be in this format: ' \
                 '{{"address":"string"(english),"price":number, "rooms":number, "moveInDate":"string", "floor":number, ' \
                 '"petsAllowed":boolean, "elevator":boolean, "mediation":boolean}} without any notes'