import sys
sys.path.append('../../')
from linear_algebra.matrix import Matrix
from utils.colors import Colors
from utils.plotter import Plotter

def test_row_echelon():
    print(f"{Colors.HEADER}\n=== Row-Echelon Form Tests ===\n{Colors.ENDC}")
    
    try:
        print(f"{Colors.BOLD}Test 1: Square matrix{Colors.ENDC}")
        mat = Matrix([
            [2, 4, -2],
            [4, 9, -3],
            [-2, -3, 7]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.row_echelon()
        print(f"{Colors.OKGREEN}Result:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 1)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(result, title="Row-Echelon Form (Test 1)")
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
        result = mat.row_echelon()
        print(f"{Colors.OKGREEN}Result:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 2)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(result, title="Row-Echelon Form (Test 2)")
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
        result = mat.row_echelon()
        print(f"{Colors.OKGREEN}Result:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 3)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(result, title="Row-Echelon Form (Test 3)")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 4: Zero matrix{Colors.ENDC}")
        mat = Matrix([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.row_echelon()
        print(f"{Colors.OKGREEN}Result:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 4)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(result, title="Row-Echelon Form (Test 4)")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 5: Empty matrix{Colors.ENDC}")
        mat = Matrix([])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for empty matrices.{Colors.ENDC}")
        
        result = mat.row_echelon()
        print(f"{Colors.OKGREEN}Result:\n{result}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
        
    try:
        print(f"{Colors.BOLD}Test 6: General matrix{Colors.ENDC}")
        mat = Matrix([
            [8., 5., -2., 4., 28.],
            [4., 2.5, 20., 4., -4.],
            [8., 5., 1., 4., 17.],
        ])
        print(f"{Colors.OKBLUE}{mat}{Colors.ENDC}")
        result = mat.row_echelon()
        print(f"{Colors.OKGREEN}Result:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 6)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(result, title="Row-Echelon Form (Test 6)")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    test_row_echelon()