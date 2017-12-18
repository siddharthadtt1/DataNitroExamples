# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 22:22:17 2017

@author: sid
"""

def bsm_put_option_value(S0, K, T, r, sigma):
    """
        Valuation of European call option in BSM model
        Analytical formula
        
        Parameters
        ===========
        S0 : float
            initial stock/index level
        K : float
            strike price
        T : float
            time to maturity (for t = 0)
        r : float
            constant risk free short rate
        sigma : float
                volatility factor in diffusion term
        
        Returns 
        ========
        value: float
                present value of the European put option
    
    """
    
    from math import log, exp, sqrt
    from scipy import stats
    
    S0 = float(S0)
    d1 = (log(S0 / K)  + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = (log(S0 / K)  + (r - 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    value = (S0 * stats.norm.cdf(d1, 0.0, 1.0) - 
            K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))
    return value