import datetime

utils = {
    "electricity": {
        "from": "0010697.0",
        "to":   "0010739.0",
        "rate": "0.214",
        "fixed": None
    },

    "gas": {
        "from": "01488000",
        "to" :  "01490457",
        "rate": "1.4",
        "fixed": "0.56"
    },

    "hot_h2o": {
        "from": "0622000",
        "to":   "0622895",
        "rate": None,
        "fixed": None
    },

    "cold_h2o": {
        "from": "05360000",
        "to":   "05399999",
        "rate": None,
        "fixed": None
    },
    
    "date": datetime.datetime.today()
}

prices = {
        "el" : 0,
        "ga" : 0,
        "hh2": 0,
        "ch2": 0,
        }

utils["electricity"]["from"] = 10866
utils["electricity"]["to"] = 10946.3

el = utils["electricity"]

diff = float(el["to"]) - float(el["from"])

price = diff * float(el["rate"])

print("Elektros kaina: ",price)

def calculate_utils(utils):
   pass 
    
