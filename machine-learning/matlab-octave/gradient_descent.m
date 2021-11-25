% Define variable x as a vector
x = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

% Based on a differentiable function (no vertical tangents)
y = (x + 5).^2
y

% Step 1 - Let's start from a 'random point', choosing any value within the dataset above
% x = -3;

% Find y:
% x = sqrt(y - 5);
for x in x():
    y = (x + 5).^2
x

% Plot the data variables
plot(x, y, 'r*')
axis([-10 10 0 150])
xlabel("time")
ylabel("price")
title("price over time")

% Then find the gradient of the function, or 1st order derivative w.r.t. the function
diff(y) / diff(x) = 2 * (x + 5);
gradient = diff(y) / diff(x);

% Step 2 - Move in the direction of the negative of the gradient (Descent)
% But how much do we move by? For that, we define a learning rate.
learning_rate = 0.01;

% Step 3 - perform 2 iterations of gradient descent
% i) Initialize Parameters:
x0 = -3;
dy/dx = 2*(x+5);
gradient = dy/dx;
gradient = diff(y)/diff(x);
learning_rate = 0.01;

% ii) Iteration 1:
x1 = x0 - learning_rate * gradient;
x1 = (-3) - (0.01) * (2 * (-3 + 5));
x1;

% iii) Iteration 2:
x2 = x1 - learning_rate * gradient;
x2 = (-3.04) - (0.01) * (2 * (-3.04 + 5));
x2;

% A better way to represent this
x_new = x+=1;
x_new = x - learning_rate * gradient;
