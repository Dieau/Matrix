import sys
sys.path.append('../../')
from linear_algebra.vector import Vector
from utils.colors import Colors
from utils.plotter import Plotter

def test_angle_cos():
    print(f"{Colors.HEADER}\n=== Angle Cosine Tests ===\n{Colors.ENDC}")
    
    try:
        print(f"{Colors.BOLD}Test 1: Orthogonal vectors{Colors.ENDC}")
        v1 = Vector([1, 0])
        v2 = Vector([0, 1])
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}{Colors.ENDC}")
        result = Vector.angle_cos(v1, v2)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
        
        fig = Plotter.plot_angle_between_vectors(v1, v2, result, title="Orthogonal Vectors (Test 1)")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 2: Parallel vectors{Colors.ENDC}")
        v1 = Vector([1, 1])
        v2 = Vector([2, 2])
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}{Colors.ENDC}")
        result = Vector.angle_cos(v1, v2)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
        
        fig = Plotter.plot_angle_between_vectors(v1, v2, result, title="Parallel Vectors (Test 2)")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 3: Opposite vectors{Colors.ENDC}")
        v1 = Vector([1, 0])
        v2 = Vector([-1, 0])
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}{Colors.ENDC}")
        result = Vector.angle_cos(v1, v2)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
        
        fig = Plotter.plot_angle_between_vectors(v1, v2, result, title="Opposite Vectors (Test 3)")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 4: Zero vector{Colors.ENDC}")
        v1 = Vector([0, 0])
        v2 = Vector([1, 1])
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for zero vectors.{Colors.ENDC}")
        
        result = Vector.angle_cos(v1, v2)
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 5: Empty vectors{Colors.ENDC}")
        v1 = Vector([])
        v2 = Vector([])
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for empty vectors.{Colors.ENDC}")
        
        result = Vector.angle_cos(v1, v2)
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    test_angle_cos()