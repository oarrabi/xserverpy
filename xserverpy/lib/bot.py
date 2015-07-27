class Bot():

    @staticmethod
    def from_json(json):
        return Bot(name=json.get("name", ""),
                   id=json["_id"],
                   integration_counter=json.get("integration_counter", ""))

    def __init__(self, **args):
        self.name = args["name"]
        self.id = args["id"]
        self.integration_counter = args["integration_counter"]

    def __repr__(self):
        return self.__dict__.__str__()
