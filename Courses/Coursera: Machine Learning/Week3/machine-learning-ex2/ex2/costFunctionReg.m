function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples
s = size(theta);
% You need to return the following variables correctly 
z = X * theta;
y_1 = -y.*log(sigmoid(z));
y_0 = -(1-y).*log(1-sigmoid(z));
J = 1/m*sum(y_1+y_0) + lambda/2*m .* sum(theta(2:s(1)) .^ 2);
temp = 1/m*sum((sigmoid(z)-y).*X(:,1));
grad = 1/m*sum((sigmoid(z)-y).*X);
grad(1) = temp;
% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta






% =============================================================

end
