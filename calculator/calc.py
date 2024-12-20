from datetime import datetime

class UtilitiesCalc:
    def __init__(self, tenn_count):
        self.num_of_tenn = tenn_count
        self.utils = {}

    def add_util(
        self, u_name, u_from=None, u_to=None, u_rate=None, u_fxd=None, u_pay_val=None
    ):
        self.u_name = u_name

        util = {
            "from":u_from,
            "to": u_to,
            "rate": u_rate,
            "fixed":u_fxd,
            "pay_val":u_pay_val,
            "diff": None
        }

        self._add_to_utils(util, u_name)

    def _add_to_utils(self, util, name):
        self._update_vals(util)
        self.utils[name] = util

    def _update_vals(self, util):
        if not util["pay_val"]: 
            util["pay_val"] = self._calc_pay_val(util)
        else:
            util["pay_val"] = float(util["pay_val"])
            if util["from"] and util["to"]:
                util["diff"] = float(util["to"]) - float(util["from"])

    def _calc_pay_val(self, util):
        util["diff"] = float(util["to"]) - float(util["from"])

        if util["rate"]:
            pay_value = util["diff"] * float(util["rate"])
        if util["fixed"]:
            pay_value += float(util["fixed"])

        util["diff"] = round(util["diff"], 2)

        return round(pay_value, 2)

    def _set_for_each(self):
        self.total_for_each = self.total / self.num_of_tenn

    def get_for_each(self):
        self._set_for_each()
        return self.total_for_each

    def _set_total(self):
        self.total = 0
        for util in self.utils.values():
            self.total += util["pay_val"]

    def get_total(self):
        self._set_total()
        return self.total

    # Used to save info in json
    def get_saveable_dict(self):
        save_dct = dict(self.utils)
        save_dct["total"] = self.get_total()
        save_dct["each"] = self.get_for_each()
        now = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

        return {now: save_dct}