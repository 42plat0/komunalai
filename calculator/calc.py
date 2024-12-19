
class UtilitiesCalc():
    def __init__(self, tenn_count): 
        self.num_of_tenn = tenn_count
        self.utils = {}

    def add_util(self, u_name, u_from=None, u_to=None, u_rate=None, u_fxd=None, u_pay_val=None):
        self.u_name = u_name
       
        util = {
            "from": u_from,
            "to": u_to,
            "rate": u_rate,
            "fixed": u_fxd,
            "pay_val": u_pay_val,
        }

        self._add_to_utils(util, u_name)

    def _add_to_utils(self, util, name):
        self.utils[name] = util
        self._update_util_pay_vals()
    
    def _update_util_pay_vals(self):
        for u_name, u_vals in self.utils.items():
            self._update_vals(u_name, u_vals)

    def _update_vals(self, name, util):
        if util["pay_val"] is None:
            util["pay_val"] = self._calc_pay_val(util) 

            self._update_pay_val(name,util)        
        else:
            util["pay_val"] = float(util["pay_val"])

    def _calc_pay_val(self, util):
        if util["rate"] is None:
            return util["pay_val"]

        diff = float(util["to"]) - float(util["from"])

        if util["rate"]: pay_value = diff * float(util["rate"])
        if util["fixed"]: pay_value += float(util["fixed"])

        return round(pay_value, 2)

    def _update_pay_val(self, u_name, u_vals):
        self.utils[u_name] = u_vals

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



#utils = {
    #"electricity": {"from": "10866", "to": "10946.3", "rate": "0.214", "fixed": None},
    #"gas": {"from": "1496", "to": "1498.6", "rate": "1.4", "fixed": "0.56"},
    #"hot_h2o": {"from": "627", "to": "629", "rate": None, "fixed": None},
    #"cold_h2o": {"from": "551", "to": "557", "rate": None, "fixed": None},
#}

#uc = UtilitiesCalc(2)

#uc.add_util("el", "10866", "10946.3", "0.214")
#uc.add_util("gas", "1496", "1498.6", "1.4", "0.56")
#uc.add_util("hot_h2o", "627", "629", u_pay_val="31.9")
#uc.add_util("cold_h2o", "551", "557", u_pay_val="11.15")
#uc.add_util("laiptine", u_pay_val="28.87" )
#uc.add_util("rent", u_pay_val="350" )

#print(uc.get_total())
#print(uc.get_for_each())