# Gradient Descent: Predictions can be made for Theta
predicted_value = intercept + slope * actual_value
y = intercept + slope * x
# Once we understand how Gradient Descent works we'll use it to solve for the intercept and slope
# We'd like to see how well a line fits the data with the SSR
y = 0 + 0.64(x)
# So using Ordinary Least Squares (OLS) we can find the slope is 0.64
# The SSR is the Loss Function, or Cost Function which will be used for gradient descent in this step-by-step model
# Hypothesis:
h_theta(x) = theta0 + theta1(x)
# Parameters:
theta0, theta1
# Cost Function:
J(theta0,theta1) = (1 / 2*m) * sum(h_theta(x - y))^2
# Goal:
min(J(theta0,theta1))

# 1. Compute the Gradient (slope) - the 1st order derivative
dy / dx = f'(x)

# 2. Move in the direction opposite to the gradient
# Opposite direction of the slope increase from current point by alpha times the gradient at that point
# The Gradient Descent Algorithm must be repeated until convergence on the local/global minimum


# Iterative Gradient Descent from Machine Learning by Stanford Online
function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);
sumError = zeros(length(theta), 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCostMulti) and gradient here.
    %

    h = X * theta;
    
    for i=1:length(theta)
        sumError(i) = sum((h - y) .* X(:,i));
    end

    theta = theta - (alpha/m) * sumError;
    

    % ============================================================

    % Save the cost J in every iteration    
    J_history = computeCostMulti(X, y, theta);

end

end

