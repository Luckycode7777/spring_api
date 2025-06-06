class Payloads:

    @staticmethod
    def json_create_new_place():
        json_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        return json_place

    @staticmethod
    def json_delete_place(place_id):
        json_del_place = {
            "place_id": place_id
        }
        return json_del_place
