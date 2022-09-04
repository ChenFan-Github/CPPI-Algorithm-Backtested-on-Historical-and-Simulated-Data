# CPPI-Algorithm-Backtested-on-Historical-and-Simulated-Data

Built a CPPI algorithm which is available for absolute wealth protection and maximum drawdown restriction.

  - Backtested the algorithm on historical data where the risky account of CPPI was constructed by Risky Parity Portfolio with three stocks that were loaded through APIs and the safe account as deposits assuming flat interest rates. 
  - Backtested on Monte Carlo Simulation where equities as risky assets of CPPI and the simulated data was generated by Geometric Brownian Motion. Safe assets of CPPI were assumed to be bonds, and the bond data were calculated through a bond pricing algorithm where the interest rate was simulated through CIR Model.
  - Visualised results to show value growth of simulated portfolios and histogram of current wealth, which was left-skewed.
