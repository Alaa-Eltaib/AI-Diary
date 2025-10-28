import math 
 #setting
def sigmoid(x):
    return 1/(1+math.exp(-x))
def dreivaiveSigomid(y_hat):
    return y_hat*(1-y_hat)

x=2;y=1;w=0.5;b=0.2;alph=0.1

#froeard Pass

z=(w*x)+b
y_hat=sigmoid(z)
error=y_hat-y
print(error)
cost=0.5*(error**2)
print(cost) 
#backward pass  
 #chaineRule
gradCostyhat=error
gradyhatz=dreivaiveSigomid(y_hat)
gradzw=x
gradzb=1
gradCostW=gradCostyhat*gradyhatz*gradzw
gradCostb=gradCostyhat*gradyhatz*gradzb
w=w-(alph*gradCostW)
b=b-(alph*gradCostb)
print(f"Final w={w:.4f}, b={b:.4f}")

####################################################
# Using NumPy
print("Using NumPy")
import numpy as np
# --- Functions ---
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def derivativeSigmoid(y_hat):
    return y_hat * (1 - y_hat)

# --- Data ---
x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

# --- Network settings ---
inputNeurons = 2
hiddenNeurons = 2
outputNeurons = 1
alph = 0.1

# --- Weights & biases ---
w1 = np.random.randn(inputNeurons, hiddenNeurons)
w2 = np.random.randn(hiddenNeurons, outputNeurons)
b1 = np.random.randn(hiddenNeurons)
b2 = np.random.randn(outputNeurons)

# --- Training ---
for i in range(10000):
    # Forward pass
    z1 = np.dot(x, w1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, w2) + b2
    y_hat = sigmoid(z2)

    # Error & cost
    error = y_hat - y
    cost = 0.5 * np.sum(error**2)

    if i % 1000 == 0:
        print(f"Iteration {i}, Cost = {cost:.4f}")

    # Backward pass
    output_delta = error * derivativeSigmoid(y_hat)
    layer1_error = np.dot(output_delta, w2.T)
    layer1_delta = layer1_error * derivativeSigmoid(a1)

    grad_W2 = np.dot(a1.T, output_delta)
    grad_b2 = np.sum(output_delta, axis=0, keepdims=True)
    grad_W1 = np.dot(x.T, layer1_delta)
    grad_b1 = np.sum(layer1_delta, axis=0, keepdims=True)

    # Update weights
    w1 = w1 - alph * grad_W1
    b1 = b1 - alph * grad_b1
    w2 = w2 - alph * grad_W2
    b2 = b2 - alph * grad_b2

print("\nInputs (XOR):")
print(x)
print("Targets (Y):")
print(y)
print("\nPredictions after 10,000 training iterations:")
print(np.round(y_hat, 3))