import sys
sys.path.append('../../')
from linear_algebra.matrix import Matrix
from utils.colors import Colors
from utils.plotter import Plotter

def test_determinant():
    print(f"{Colors.HEADER}\n=== Matrix Determinant Tests ===\n{Colors.ENDC}")
    
    try:
        print(f"{Colors.BOLD}Test 1: 1x1 Matrix{Colors.ENDC}")
        mat = Matrix([[5]])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.determinant()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")

        max_value = abs(mat.data[0][0])

        fig = Plotter.plot_matrix(mat, title=f"1x1 Matrix (Test 1)\nDeterminant: {result}", max_value=max_value)
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")

    try:
        print(f"\n{Colors.BOLD}Test 2: 2x2 Matrix{Colors.ENDC}")
        mat = Matrix([
            [1, 2],
            [3, 4]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.determinant()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title=f"2x2 Matrix (Test 2)\nDeterminant: {result}")
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
        result = mat.determinant()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title=f"3x3 Matrix (Test 3)\nDeterminant: {result}")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 4: 4x4 Matrix{Colors.ENDC}")
        mat = Matrix([
            [8., 5., -2., 4.],
            [4., 2.5, 20., 4.],
            [8., 5., 1., 4.],
            [28., -4., 17., 1.]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.determinant()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title=f"4x4 Matrix (Test 4)\nDeterminant: {result}")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 5: Non-Square Matrix{Colors.ENDC}")
        mat = Matrix([
            [1, 2, 3],
            [4, 5, 6]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for non-square matrices.{Colors.ENDC}")
        
        result = mat.determinant()
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 6: Empty Matrix{Colors.ENDC}")
        mat = Matrix([])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for empty matrices.{Colors.ENDC}")
        
        result = mat.determinant()
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    test_determinant()