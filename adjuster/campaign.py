import json


class Campaign:
    """
    {
        "advertiser": "Telemundo",
        "cpm": "$12.00",
        "endDate": "2018-06-28",
        "id": 4976875,
        "name": "cow-pox winos",
        "startDate": "2018-06-28"
    },
    """
    def __init__(self, campaign):
        self.id = campaign['id']
        self.startDate = campaign['startDate']
        self.name = campaign['name']
        self.cpm = campaign['cpm']
        self.endDate = campaign['endDate']
        self.advertiser = campaign['advertiser']
        self.impressions = 0
        self.views = 0
        self.clicks = 0

    def json(self):
        return json.dumps(self)
