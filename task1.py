from datetime import datetime, timedelta
import json
import random

def example():
    """crarete ajson file
    """
    data = {"user" : "sadas"}
    json_object = json.dumps(data, indent = 4)
    random_num = random.randint(1,100)
    fName = f"{random_num}.json"
    with open(fName, "w") as outfile:
        outfile.write(json_object)
    print("running queue")