import os

def leibniz_formula(iterations):
    result = 0.0
    for k in range(iterations):
        result += ((-1) ** k) / (2 * k + 1)
    return result * 4 

if __name__ == "__main__":
    iterations = int(os.getenv("N", 1000))
    pi_approximation = leibniz_formula(iterations)
    print(pi_approximation)
