import sys

def leibniz_formula(iterations):
    result = 0.0
    for k in range(iterations):
        result += ((-1) ** k) / (2 * k + 1)
    return result * 4 

if __name__ == "__main__":
    if len(sys.argv) >= 1:
        iterations = sys.argv[1]
    else:
        iterations = "1000" 
    try:
        pi_approximation = leibniz_formula(int(iterations))
        print(pi_approximation)
    except ValueError:
        print("Bad argument")
        
