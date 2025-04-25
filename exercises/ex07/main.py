import sys
sys.path.append('../../')
from linear_algebra.vector import Vector
from linear_algebra.matrix import Matrix
from utils.colors import Colors
from utils.plotter import Plotter

def test_matrix_operations():
    print(f"{Colors.HEADER}\n=== Matrix Multiplication Tests ===\n{Colors.ENDC}")
    
    try:
        print(f"{Colors.BOLD}Test 1: Matrix-vector multiplication{Colors.ENDC}")
        mat = Matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        vec = Vector([1, 0, -1])
        print(f"{Colors.OKBLUE}{mat}\n{vec}{Colors.ENDC}")
        result = mat.mul_vec(vec)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Matrix (Test 1)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_vector([vec], labels=["Input Vector"], colors=["blue"], title="Vector (Test 1)")
        Plotter.wait_for_next(fig)
        
        fig = Plotter.plot_vector([vec, result], labels=["Input Vector", "Result"], colors=["blue", "green"], title="Resulting Vector (Test 1)")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 2: Matrix-matrix multiplication{Colors.ENDC}")
        mat1 = Matrix([
            [1, 2],
            [3, 4],
            [5, 6]
        ])
        mat2 = Matrix([
            [7, 8, 9],
            [10, 11, 12]
        ])
        print(f"{Colors.OKBLUE}{mat1}\n{mat2}{Colors.ENDC}")
        result = mat1.mul_mat(mat2)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat1, title="Matrix 1 (Test 2)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(mat2, title="Matrix 2 (Test 2)")
        Plotter.wait_for_next(fig)
        
        fig = Plotter.plot_matrix_wireframe(result, title="Resulting Matrix (Test 2)")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 3: Dimension mismatch for matrix-vector multiplication{Colors.ENDC}")
        mat = Matrix([
            [1, 2],
            [3, 4]
        ])
        vec = Vector([1, 2, 3])
        print(f"{Colors.OKBLUE}{mat}\n{vec}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for dimension mismatch.{Colors.ENDC}")
        
        result = mat.mul_vec(vec)
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 4: Dimension mismatch for matrix-matrix multiplication{Colors.ENDC}")
        mat1 = Matrix([
            [1, 2],
            [3, 4]
        ])
        mat2 = Matrix([
            [5, 6],
            [7, 8],
            [9, 10]
        ])
        print(f"{Colors.OKBLUE}{mat1}\n{mat2}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for dimension mismatch.{Colors.ENDC}")
        
        result = mat1.mul_mat(mat2)
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 5: Empty matrix multiplication{Colors.ENDC}")
        mat1 = Matrix([])
        mat2 = Matrix([])
        print(f"{Colors.OKBLUE}{mat1.__repr__()}\n{mat2.__repr__()}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for empty matrices.{Colors.ENDC}")
        
        result = mat1.mul_mat(mat2)
        print(f"{Colors.OKGREEN}Result: \n{result}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    test_matrix_operations()