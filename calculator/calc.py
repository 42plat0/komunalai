import datetime

utils = {
    "electricity": {"from": "10866", "to": "10946.3", "rate": "0.214", "fixed": None},
    "gas": {"from": "1496", "to": "1498.6", "rate": "1.4", "fixed": "0.56"},
    "hot_h2o": {"from": "627", "to": "629", "rate": None, "fixed": None},
    "cold_h2o": {"from": "551", "to": "557", "rate": None, "fixed": None},
    "date": datetime.datetime.today(),
}


def get_util(util_from, util_to, util_rate, util_fixed):
    util = {
        "from": util_from,
        "to": util_to,
        "rate": util_rate,
        "fixed": util_fixed,
    }

    return util


def calc_util_price(util):
    diff = float(util["to"]) - float(util["from"])

    if util["rate"]: pay_value = diff * float(util["rate"])
    else:            
        return None
    if util["fixed"]: pay_value += float(util["fixed"])

    return round(pay_value, 2)


prices = {
    "el": 0,
    "ga": 0,
    "hh2": 0,
    "ch2": 0,
}

el = utils["electricity"]
gas = utils["gas"]
hot = utils["hot_h2o"]
cold = utils["cold_h2o"]

print(
    "electricity", calc_util_price(el),
    "gas: ", calc_util_price(gas),
    "hot", calc_util_price(hot),
    "cold: ", calc_util_price(cold)
)