import sys
sys.path.append('../../')
from linear_algebra.matrix import Matrix
from utils.colors import Colors
from utils.plotter import Plotter

def test_trace():
    print(f"{Colors.HEADER}\n=== Matrix Trace Tests ===\n{Colors.ENDC}")
    
    try:
        print(f"{Colors.BOLD}Test 1: Square matrix{Colors.ENDC}")
        mat = Matrix([
            [-2, -8, 4],
            [1, -23, 4],
            [0, 6, 4]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.trace()
        print(f"{Colors.OKGREEN}Trace: {result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title=f"Square Matrix (Test 1)\nTrace: {result}")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 2: Diagonal matrix{Colors.ENDC}")
        mat = Matrix([
            [1, 0, 0],
            [0, 5, 0],
            [0, 0, 9]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.trace()
        print(f"{Colors.OKGREEN}Trace: {result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title=f"Diagonal Matrix (Test 2)\nTrace: {result}")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 3: Non-square matrix{Colors.ENDC}")
        mat = Matrix([
            [1, 2, 3],
            [4, 5, 6]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for non-square matrices.{Colors.ENDC}")
        
        result = mat.trace()
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 4: Empty matrix{Colors.ENDC}")
        mat = Matrix([])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for empty matrices.{Colors.ENDC}")
        
        result = mat.trace()
        print(f"{Colors.OKGREEN}Trace: {result}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 5: Matrix with negative and floating-point values{Colors.ENDC}")
        mat = Matrix([
            [-1.5, 2.3, 3.1],
            [4.2, 5.5, 6.6],
            [7.7, 8.8, -9.9]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.trace()
        print(f"{Colors.OKGREEN}Trace: {result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title=f"Matrix with Negative and Floating-Point Values (Test 5)\nTrace: {result}")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    test_trace()