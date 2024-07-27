# Multi-Scalable Cloud Application Value at Risk (VaR)

This document details a multi-scalable cloud application designed to compute Value at Risk (VaR) for well-known companies listed on stock markets. The application employs a combination of front-end and back-end code for AWS Lambda, with additional components running on Amazon EC2. For the EC2 source code, please contact me directly as it requires reconstruction and amendments. This application involves user authentication with AWS credentials, key pairs, and other security access keys.

## Introduction

Value at Risk (VaR) is a statistical technique used to measure the risk of an investment. It quantifies the potential loss in value of an investment portfolio over a defined period for a given confidence interval. Due to the computational expense, power requirements, and the use of large random values, this application leverages a multi-cloud architecture and scalable services. It utilizes three VaR calculation methods: historical, covariance, and Monte Carlo.

## Architecture

The proposed system integrates public cloud providers Amazon Web Services (AWS) and Google App Engine (GAE). These services offer on-demand self-service, broad network access, rapid elasticity, measured service, and resource pooling in accordance with NIST standards. 

### Google App Engine (GAE)

GAE is a public cloud service managed by Google, falling into the Platform as a Service (PaaS) category. It supports various programming languages, including Python. The front-end source code runs on GAE, taking specific inputs and displaying outputs to the user.

### AWS Lambda

AWS Lambda is a cloud computing service that allows users to run code or scripts to perform certain tasks or functions. It is also categorized as PaaS, similar to GAE.

## VaR Calculation Methods

### 1. Historical Method

The historical method calculates VaR by analyzing the return series using the adjacent closing prices of a given company. The steps are as follows:

1. Find the return series.
2. Sort the values from the largest profit to the largest loss.
3. Calculate the total number of data points.
4. Determine the 95th and 99th percentiles to obtain VaR at 95% and 99% confidence levels.

### 2. Covariance Method

The covariance method involves computing the mean and standard deviation (stdev) to fit the VaR formula with a set investment. The formula used is:
\[ \text{VaR} = -(\text{mean} + D \times \sigma) \times \text{Investment} \]
Where \( D \) is 1.65 for 95% confidence and 2.33 for 99% confidence.

### 3. Monte Carlo Method

The Monte Carlo method uses the mean and stdev from the covariance method. The steps include:

1. Use the Python function `random.gauss` to generate random numbers (\( q \)).
2. Apply \( q \) with the most recent adjacent closing price (\( p \)) of a given company to the formula:
\[ n = (1 + q) \times p \]
3. Generate a new price list, which is then processed through the historical method to obtain VaR at 95% and 99% confidence levels.

## Conclusion

This multi-scalable cloud application efficiently computes VaR using a combination of AWS Lambda and Google App Engine. By leveraging the strengths of these platforms, the application ensures rapid and reliable computations essential for assessing investment risk.

For more information or to access the EC2 source code, please contact me directly.
