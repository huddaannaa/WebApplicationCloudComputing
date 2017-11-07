# MULTI-SCALABLE-CLOUD-APPLICATION-VALUE-AT-RISK-VAR-
## This contains Frontt and Backend code for AWS LAMBDA. One can contact me for EC2's front and backend source because i will need to reconstruct and make amends to the source. This is because it entails a user to login with credentions for AWS, Keypairs and other security access keys source-code for the project (Scalable multi-Cloud application, that computes Value at Risk for some well-known companies listed on stock markets

### 1) Historical: This is calculated by finding the return series, using the adjacent close of a given company. The next step is to sort the values from largest profit to the largest loss, taking the total number of data points we calculate the 95 and 99 percentages to attain the VAR at 95 and 95 percentages 

### 2) Covariance: We compute the mean and standard deviation (stdev) to fit   the give formula with a set investment, where D is 1.65 at 95 and 2.33 at 99: −(𝑚𝑒𝑎𝑛 +(𝐷) ∗𝜎))∗𝐼𝑛𝑣𝑒𝑠𝑡𝑚𝑒𝑛𝑡 
 
### 3) Monte Carlo: Having the mean and stdev from the previous step, we use the python function “random. Gauss” to generate random number (q).  ‘q’ is then used together with the most recent price of the adjacent close from a given company (p) to fit the formula: 𝑛 = (1 +𝑞)∗𝑝 The resultant n produces a new price list, which is run through the historical step to attain VAR at 95 and 99 percentages. 
