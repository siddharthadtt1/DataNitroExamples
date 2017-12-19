# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 18:29:17 2017

@author: sd835979
"""

class class_flow_series(object):
    """
        Class to model a cash flow series
        
        Attributes
        ==========
        name : string
            name of the object
        cash_flows : list/array-like
            list of (positive) year fractions
        time_list : list/array-like
            corresponding list of cash flow values
        short_rate : instance of short_rate class 
            short rate object used for discounting
            
        Methods
        =======
        present_value_list :
            returns an array with present values
        net_present_value :
            returns NPV for cash flow series
            
    """
    def __init__(self, name, cash_flows, time_list, short_rate):
        self.name = name
        self.cash_flows = cash_flows
        self.time_list = time_list
        self.short_rate = short_rate
    
    def present_value_list(self):
        df = self.short_rate.get_discount_factors(self.time_list)
        return np.array(self.cash_flows) * df
        
    def net_present_value(self):
        return np.sum(self.present_value_list())
    

        
        