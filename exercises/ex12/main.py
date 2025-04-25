import sys
sys.path.append('../../')
from linear_algebra.matrix import Matrix
from utils.colors import Colors
from utils.plotter import Plotter

def test_inverse():
    print(f"{Colors.HEADER}\n=== Matrix Inverse Tests ===\n{Colors.ENDC}")
    
    try:
        print(f"{Colors.BOLD}Test 1: 1x1 Matrix{Colors.ENDC}")
        mat = Matrix([[5]])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.inverse()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        max_value = max(abs(mat.data[0][0]), abs(result.data[0][0]))
        
        fig = Plotter.plot_matrix(mat, title="Original Matrix (Test 1)", max_value=max_value)
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix(result, title="Inverse Matrix (Test 1)", max_value=max_value)
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 2: 2x2 Matrix{Colors.ENDC}")
        mat = Matrix([
            [4, 7],
            [2, 6]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.inverse()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 2)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(result, title="Inverse Matrix (Test 2)")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 3: 3x3 Matrix{Colors.ENDC}")
        mat = Matrix([
            [8., 5., -2.],
            [4., 7., 20.],
            [7., 6., 1.]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.inverse()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 3)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(result, title="Inverse Matrix (Test 3)")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 4: Singular Matrix{Colors.ENDC}")
        mat = Matrix([
            [1, 2],
            [2, 4]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for singular matrices.{Colors.ENDC}")
        
        result = mat.inverse()
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 5: Non-Square Matrix{Colors.ENDC}")
        mat = Matrix([
            [1, 2, 3],
            [4, 5, 6]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for non-square matrices.{Colors.ENDC}")
        
        result = mat.inverse()
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 6: Empty Matrix{Colors.ENDC}")
        mat = Matrix([])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for empty matrices.{Colors.ENDC}")
        
        result = mat.inverse()
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    test_inverse()