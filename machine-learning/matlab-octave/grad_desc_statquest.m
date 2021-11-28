# GRADIENT DESCENT - STEP BY STEP
# Step 1: Calculate the 1st residual
x = 0.5;
y = 1.4;

gradient = delta(y) / delta(x);
gradient

# Using the following equation for linear regression:
y = mx + b;
y = predicted value;
m = slope, y / x = 0.64;
x = actual value, 0.5;
b = intercept, 0;
y_predicted = 0 + 0.64 * 0.5;
# given a value of x = 0.5
y_predicted = 0.32;
# now calculate the residual
residual = 1.4 - 0.32;
(residual)^2 = (1.4 - 0.32)^2;
