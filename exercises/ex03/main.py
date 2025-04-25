import sys
sys.path.append('../../')
from linear_algebra.vector import Vector
from utils.colors import Colors
from utils.plotter import Plotter

def test_dot_product():
    print(f"{Colors.HEADER}\n=== Dot Product Tests ===\n{Colors.ENDC}")
    
    try:
        print(f"{Colors.BOLD}Test 1: Valid dot product{Colors.ENDC}")
        v1 = Vector([-1, 6, 4])
        v2 = Vector([3, 2, 5])
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}{Colors.ENDC}")
        
        fig = Plotter.plot_vector([v1, v2], labels=["v1", "v2"], colors=["red", "blue"], title="Initial Vectors (Test 1)")
        Plotter.wait_for_next(fig)
        
        result = Vector.dot(v1, v2)
        print(f"{Colors.OKGREEN}Dot Product Result: {result}{Colors.ENDC}")
        
        v2_magnitude_squared = Vector.dot(v2, v2)
        if v2_magnitude_squared != 0:
            projection = v2.scl(Vector.dot(v1, v2) / v2_magnitude_squared)
            print(f"{Colors.OKGREEN}Projection of v1 onto v2: {projection}{Colors.ENDC}")
            
            fig = Plotter.plot_vector([v1, v2, projection], labels=["v1", "v2", "Projection"], colors=["red", "blue", "green"], title="Dot Product Visualization (Test 1)")
            Plotter.wait_for_next(fig)
        else:
            print(f"{Colors.WARNING}Cannot compute projection: v2 is a zero vector.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 2: Dot product of zero vectors{Colors.ENDC}")
        v1 = Vector([0, 0, 0])
        v2 = Vector([0, 0, 0])
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}{Colors.ENDC}")
                
        result = Vector.dot(v1, v2)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 3: Dot product of empty vectors{Colors.ENDC}")
        v1 = Vector([])
        v2 = Vector([])
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for empty vectors.{Colors.ENDC}")
        
        result = Vector.dot(v1, v2)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 4: Mismatched dimensions{Colors.ENDC}")
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5])
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}{Colors.ENDC}")
        
        result = Vector.dot(v1, v2)
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 5: Dot product with negative numbers{Colors.ENDC}")
        v1 = Vector([-1, -2, -3])
        v2 = Vector([4, 5, 6])
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}{Colors.ENDC}")
        
        fig = Plotter.plot_vector([v1, v2], labels=["v1", "v2"], colors=["red", "blue"], title="Initial Vectors (Test 5)")
        Plotter.wait_for_next(fig)
        
        result = Vector.dot(v1, v2)
        print(f"{Colors.OKGREEN}Dot Product Result: {result}{Colors.ENDC}")
        
        v2_magnitude_squared = Vector.dot(v2, v2)
        if v2_magnitude_squared != 0:
            projection = v2.scl(Vector.dot(v1, v2) / v2_magnitude_squared)
            print(f"{Colors.OKGREEN}Projection of v1 onto v2: {projection}{Colors.ENDC}")
            
            fig = Plotter.plot_vector([v1, v2, projection], labels=["v1", "v2", "Projection"], colors=["red", "blue", "green"], title="Dot Product Visualization (Test 5)")
            Plotter.wait_for_next(fig)
        else:
            print(f"{Colors.WARNING}Cannot compute projection: v2 is a zero vector.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    test_dot_product()