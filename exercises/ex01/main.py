import sys
sys.path.append('../../')
from linear_algebra.vector import Vector
from utils.colors import Colors
from utils.plotter import Plotter

def test_linear_combination():
    print(f"{Colors.HEADER}\n=== Linear Combination Tests ===\n{Colors.ENDC}")
    
    try:
        print(f"{Colors.BOLD}Test 1: Valid input{Colors.ENDC}")
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        v3 = Vector([7, 8, 9])
        v4 = Vector([0, 10, -100])
        e1 = Vector([1, 0, 0])
        e2 = Vector([0, 1, 0])
        e3 = Vector([0, 0, 1])
        coefficients = [10, -2, 0.5]
        coefficients2 = [10, -2]
        print(f"{Colors.OKBLUE}Vectors: {v1}, {v2}, {v3}{Colors.ENDC}")
        print(f"{Colors.OKBLUE}Coefficients: {coefficients}{Colors.ENDC}")
        result = Vector.linear_combination([v1, v2, v3], coefficients)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
        
        print(f"{Colors.OKBLUE}Vectors: {e1}, {e2}, {e3}{Colors.ENDC}")
        print(f"{Colors.OKBLUE}Coefficients: {coefficients}{Colors.ENDC}")
        result = Vector.linear_combination([e1, e2, e3], coefficients)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
        
        print(f"{Colors.OKBLUE}Vectors: {v1}, {v2}{Colors.ENDC}")
        print(f"{Colors.OKBLUE}Coefficients: {coefficients2}{Colors.ENDC}")
        result = Vector.linear_combination([v1, v4], coefficients2)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
        
        fig = Plotter.plot_vector(
            [v1, v2, v3],
            labels=["v1", "v2", "v3"],
            colors=["red", "blue", "green"],
            title="Input Vectors"
        )
        Plotter.wait_for_next(fig)
        
        fig = Plotter.plot_vector(
            [v1, v2, v3, result],
            labels=["v1", "v2", "v3", "Result"],
            colors=["red", "blue", "green", "purple"],
            title="Linear Combination of Vectors"
        )
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 2: Empty vectors and coefficients{Colors.ENDC}")
        print(f"{Colors.OKBLUE}Vectors: []{Colors.ENDC}")
        print(f"{Colors.OKBLUE}Coefficients: []{Colors.ENDC}")
        result = Vector.linear_combination([], [])
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 3: Mismatched lengths of vectors and coefficients{Colors.ENDC}")
        v1 = Vector([1, 2])
        v2 = Vector([4, 5])
        coefficients = [2, 1, 5]
        print(f"{Colors.OKBLUE}Vectors: {v1}, {v2}{Colors.ENDC}")
        print(f"{Colors.OKBLUE}Coefficients: {coefficients}{Colors.ENDC}")
        result = Vector.linear_combination([v1, v2], coefficients)
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 4: Vectors with different sizes{Colors.ENDC}")
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5])
        coefficients = [2, 3]
        print(f"{Colors.OKBLUE}Vectors: {v1}, {v2}{Colors.ENDC}")
        print(f"{Colors.OKBLUE}Coefficients: {coefficients}{Colors.ENDC}")
        result = Vector.linear_combination([v1, v2], coefficients)
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 5: Non-numeric coefficients{Colors.ENDC}")
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        coefficients = [2, "a"]
        print(f"{Colors.OKBLUE}Vectors: {v1}, {v2}{Colors.ENDC}")
        print(f"{Colors.OKBLUE}Coefficients: {coefficients}{Colors.ENDC}")
        result = Vector.linear_combination([v1, v2], coefficients)
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except TypeError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 6: Zero-length vectors{Colors.ENDC}")
        v1 = Vector([])
        v2 = Vector([])
        coefficients = [2, 3]
        print(f"{Colors.OKBLUE}Vectors: {v1}, {v2}{Colors.ENDC}")
        print(f"{Colors.OKBLUE}Coefficients: {coefficients}{Colors.ENDC}")
        result = Vector.linear_combination([v1, v2], coefficients)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for zero-length vectors.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    test_linear_combination()