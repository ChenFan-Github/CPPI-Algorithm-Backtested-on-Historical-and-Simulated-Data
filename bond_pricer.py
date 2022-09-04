import pandas as pd
import numpy as np
    
class bond():
    def bond_price(self, maturity, principal=100, coupon_rate=0.03, coupons_per_year=2, discount_rate=0.03):
        """
        Conpute the price of a bond that pays regular coupons until maturity at which time the principal and the final coupon is returned.
        """
        if isinstance(discount_rate, pd.DataFrame):
            pricing_dates = discount_rate.index
            prices = pd.DataFrame(index=pricing_dates, columns=discount_rate.columns)
            for t in pricing_dates:
                prices.loc[t] = self.bond_price(maturity, principal, coupon_rate, coupons_per_year, discount_rate.loc[t])
            return prices
        else: 
            cash_flows = self.bond_cash_flows(maturity, principal, coupon_rate, coupons_per_year)
            return self.pv(cash_flows, discount_rate/coupons_per_year)


    def pv(self, flows, r):
        """
        Compute Present Value of a sequence of cash flow.
        flows: indexed by the maturity periods of assets/liabilities.
        """    
        date = flows.index
        if isinstance(r,pd.Series):
            discounts= self.discount(date,r)
            # get discounts as pd.DataFrame, so need to change discount()
            return discounts.multiply(flows,axis='index').sum()
        else: 
            discounts = self.discount(date,r)
            return (flows*discounts).sum()


    def discount(self, t,r):
        """
        Compute discount factors, given discounted rate and periods.
        """
        if isinstance(r,pd.Series):
            discounts = pd.DataFrame([(1+r)**(-i) for i in t])
            discounts.index=t
            return discounts
        else:
            return ((1+r)**(-t))


    def bond_cash_flows(self, maturity, principal=100, coupon_rate=0.03, coupons_per_year=12):
        """
        Returns a series of cash flows generated by a bond indexed by a coupon number.
        """
        n_coupons = round(maturity*coupons_per_year)
        coupon_amt = principal*coupon_rate/coupons_per_year 
        coupon_times = np.arange(1, n_coupons+1) 

        cash_flows = pd.Series(data=coupon_amt, index=coupon_times)
        cash_flows.iloc[-1] += principal
        return cash_flows