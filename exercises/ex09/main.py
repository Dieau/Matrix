import sys
sys.path.append('../../')
from linear_algebra.matrix import Matrix
from utils.colors import Colors
from utils.plotter import Plotter

def test_transpose():
    print(f"{Colors.HEADER}\n=== Matrix Transpose Tests ===\n{Colors.ENDC}")
    
    try:
        print(f"{Colors.BOLD}Test 1: Square matrix{Colors.ENDC}")
        mat = Matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.transpose()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 1)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(result, title="Transposed Matrix (Test 1)")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 2: Rectangular matrix (+rows){Colors.ENDC}")
        mat = Matrix([
            [1, 2],
            [3, 4],
            [5, 6]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.transpose()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 2)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(result, title="Transposed Matrix (Test 2)")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 3: Rectangular matrix (+columns){Colors.ENDC}")
        mat = Matrix([
            [1, 2, 3],
            [4, 5, 6]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.transpose()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 3)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(result, title="Transposed Matrix (Test 3)")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 4: Empty matrix{Colors.ENDC}")
        mat = Matrix([])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for empty matrices.{Colors.ENDC}")
        
        result = mat.transpose()
        print(f"{Colors.OKGREEN}Result:\n{result}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 5: Single row matrix{Colors.ENDC}")
        mat = Matrix([[1, 2, 3]])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.transpose()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 5)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(result, title="Transposed Matrix (Test 5)")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 6: Single column matrix{Colors.ENDC}")
        mat = Matrix([
            [1],
            [2],
            [3]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.transpose()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 6)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(result, title="Transposed Matrix (Test 6)")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    test_transpose()