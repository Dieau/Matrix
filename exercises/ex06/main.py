import sys
sys.path.append('../../')
from linear_algebra.vector import Vector
from utils.colors import Colors
from utils.plotter import Plotter

def test_cross_product():
    print(f"{Colors.HEADER}\n=== Cross Product Tests ===\n{Colors.ENDC}")
    
    try:
        print(f"{Colors.BOLD}Test 1: Perpendicular vectors{Colors.ENDC}")
        v1 = Vector([1, 0, 0])
        v2 = Vector([0, 1, 0])
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}{Colors.ENDC}")
        result = Vector.cross_product(v1, v2)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
        
        fig = Plotter.plot_vector(
            [v1, v2, result],
            labels=["v1", "v2", "Cross Product"],
            colors=["red", "blue", "green"],
            title="Perpendicular Vectors (Test 1)"
        )
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 2: Parallel vectors{Colors.ENDC}")
        v1 = Vector([1, 1, 1])
        v2 = Vector([2, 2, 2])
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}{Colors.ENDC}")
        result = Vector.cross_product(v1, v2)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for parallel vectors (cross product is zero).{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 3: Zero vector{Colors.ENDC}")
        v1 = Vector([0, 0, 0])
        v2 = Vector([1, 2, 3])
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for zero vectors.{Colors.ENDC}")
        
        result = Vector.cross_product(v1, v2)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 4: General 3D vectors{Colors.ENDC}")
        v1 = Vector([4, 2, -3])
        v2 = Vector([-2, -5, 4])
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}{Colors.ENDC}")
        result = Vector.cross_product(v1, v2)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
        
        fig = Plotter.plot_vector(
            [v1, v2, result],
            labels=["v1", "v2", "Cross Product"],
            colors=["red", "blue", "green"],
            title="General 3D Vectors (Test 4)"
        )
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 5: Non-3D vectors{Colors.ENDC}")
        v1 = Vector([1, 2])
        v2 = Vector([3, 4])
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for non-3D vectors.{Colors.ENDC}")
        
        result = Vector.cross_product(v1, v2)
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    test_cross_product()