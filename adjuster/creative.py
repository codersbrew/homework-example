import json


class Creative:
    """
    {
    "clicks": 1930,
    "conversions": 187,
    "id": 32360,
    "impressions": 13296,
    "name": "cow-pox winos esterase",
    "parentId": 4976875,
    "views": 2209
    },
    """
    def __init__(self, creative):
        self.id = creative['id']
        self.parentId = creative['parentId']
        self.name = creative['name']
        self.clicks = creative['clicks']
        self.conversions = creative['conversions']
        self.views = creative['views']
        self.impressions = creative['impressions']

    def json(self):
        return json.dumps(self)
