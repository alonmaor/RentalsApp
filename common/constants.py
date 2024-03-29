from urllib.parse import quote_plus

MAPQUEST_APIKEY_NAME = "MAPQUEST_APIKEY"
MAPQUEST_ENDPOINT_NAME = "MAPQUEST_ENDPOINT"
POSITIONSTACK_APIKEY_NAME = "POSITIONSTACK_APIKEY"
POSITIONSTACK_ENDPOINT_NAME = "POSITIONSTACK_ENDPOINT"
MONGO_URI = "mongodb+srv://alonm91:" + quote_plus("DkbVpsGniJYoVgJE") + "@cluster0.ygbbobb.mongodb.net" \
                                                                                     "/?retryWrites=true&w=majority" \
                                                                                     "&authSource=admin"
MONGO_DB_NAME = "mydatabase"
OPENAI_APIKEY_NAME = 'OPENAI_APIKEY'
OPENAI_PROMPT = 'Given the apartment rental below can you provide the following details ONLY in a JSON object ' \
                '(dont ignore newlines): street address (if no exact address then which streets crossing in english in this format: Street name-Street name), ' \
                'neighborhood, price (only number), number of rooms, number of bathrooms (if exists), size(without balcony), elevator , furnished, pets allowed, ' \
                 'date of move-in(date format day/month), which floor, mediation, roomates, sublet and sublease date ' \
                '(if applicable)?\n{}\nThe resulting JSON should be in this format: {{"streetAddress":"string"(english), ' \
                '"neighborhood":string, "price":number, "rooms":number, "bathrooms":number "moveInDate":"string", "floor":number, "petsAllowed":boolean, ' \
                '"elevator":boolean, "mediation":boolean, "roomates":boolean, "sublet":boolean, "subletDates":string}} without any notes'

FB_ACCESS_TOKEN_NAME = 'FB_ACCESS_TOKEN'
FB_GROUP_ID_NAME = 'FB_GROUP_ID'
