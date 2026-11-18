# Function definition
def func(x):
    return x * x * x - x * x + 2

# Derivative of the function
def deriv(x):
    return 3 * x * x - 2 * x

def newton_raphson(x0, tol=1e-6, max_iter=100):
    xn = x0
    for i in range(max_iter):
        fx = func(xn)
        dfx = deriv(xn)
        
        # Check if we hit the root within tolerance
        if abs(fx) < tol:
            print(f"Root found after {i} iterations.")
            return xn
            
        # Prevent division by zero
        if dfx == 0:
            print("Derivative is zero. Method failed.")
            return None
            
        # Update guess using Newton-Raphson formula
        xn = xn - fx / dfx
        
    print("Maximum iterations reached without convergence.")
    return xn

# Driver code with an initial guess
initial_guess = -1.0
root = newton_raphson(initial_guess)

if root is not None:
    print("The value of root is :", "%.4f" % root)
