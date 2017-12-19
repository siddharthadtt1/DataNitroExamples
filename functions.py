# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:36:13 2017

@author: sd835979
"""

#
# Valuation of Euorpean call options in BSM model
# for use with DataNitro and Excel spreadsheets
# functions.py
#
#

# analytical Black-Scholes-Merton (BSM) formula 

def bsm_call_option_value(S0, K, T, r, sigma):
    """
        Parameters
        ============
        S0 : float
            initial stock/index level
        K : float
            strike price
        T : float
            time-to-maturity (for t=0)
        r : float
            constant risk-free short rate
        sigma : float
                volatility factor in diffusion term
        
        Returns
        ========
        value : float
                present value of the European call option
    
    """
    from math import log, exp, sqrt
    import scipy.stats as stats
    
    S0 = float(S0)
    d1 = (log(S0 / K) + ((r + (0.5 * sigma ** 2))/T))/ (sigma * sqrt(T))
    d2 = (log(S0 / K) + ((r - (0.5 * sigma ** 2))/T))/ (sigma * sqrt(T))
    
    value = (S0 * stats.norm.cdf(d1, 0.0, 1.0)) - (
            K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))
    return value.round(2)
    
S0 = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

value = bsm_call_option_value(S0, K, T, r, sigma)
print 'BSM put value option : ' + str(value)  

