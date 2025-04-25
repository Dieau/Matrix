import sys
sys.path.append('../../')
from linear_algebra.matrix import Matrix
from utils.colors import Colors
from utils.plotter import Plotter

def test_rank():
    print(f"{Colors.HEADER}\n=== Matrix Rank Tests ===\n{Colors.ENDC}")
    
    try:
        print(f"{Colors.BOLD}Test 1: Zero Matrix{Colors.ENDC}")
        mat = Matrix([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])
        print(f"{Colors.OKBLUE}Matrix: {mat}{Colors.ENDC}")
        rref = mat.row_echelon()
        print(f"{Colors.OKCYAN}\nRow-Echelon Form:\n{rref}{Colors.ENDC}")
        result = mat.rank()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 1)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(rref, title=f"Row-Echelon Form (Test 1)\nRank: {result}")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 2: Full-Rank Square Matrix{Colors.ENDC}")
        mat = Matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 10]
        ])
        print(f"{Colors.OKBLUE}Matrix: {mat}{Colors.ENDC}")
        rref = mat.row_echelon()
        print(f"{Colors.OKCYAN}\nRow-Echelon Form:\n{rref}{Colors.ENDC}")
        result = mat.rank()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 2)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(rref, title=f"Row-Echelon Form (Test 2)\nRank: {result}")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 3: Rectangular Matrix (More Rows than Columns){Colors.ENDC}")
        mat = Matrix([
            [1, 2],
            [3, 4],
            [5, 6]
        ])
        print(f"{Colors.OKBLUE}Matrix: {mat}{Colors.ENDC}")
        rref = mat.row_echelon()
        print(f"{Colors.OKCYAN}\nRow-Echelon Form:\n{rref}{Colors.ENDC}")
        result = mat.rank()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 3)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(rref, title=f"Row-Echelon Form (Test 3)\nRank: {result}")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 4: Rectangular Matrix (More Columns than Rows){Colors.ENDC}")
        mat = Matrix([
            [1, 2, 3],
            [4, 5, 6]
        ])
        print(f"{Colors.OKBLUE}Matrix: {mat}{Colors.ENDC}")
        rref = mat.row_echelon()
        print(f"{Colors.OKCYAN}\nRow-Echelon Form:\n{rref}{Colors.ENDC}")
        result = mat.rank()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 4)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(rref, title=f"Row-Echelon Form (Test 4)\nRank: {result}")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 5: Singular Matrix{Colors.ENDC}")
        mat = Matrix([
            [1, 2, 3],
            [2, 4, 6],
            [3, 6, 9]
        ])
        print(f"{Colors.OKBLUE}Matrix: {mat}{Colors.ENDC}")
        rref = mat.row_echelon()
        print(f"{Colors.OKCYAN}\nRow-Echelon Form:\n{rref}{Colors.ENDC}")
        result = mat.rank()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
        
        fig = Plotter.plot_matrix_wireframe(mat, title="Original Matrix (Test 5)")
        Plotter.wait_for_next(fig)
        fig = Plotter.plot_matrix_wireframe(rref, title=f"Row-Echelon Form (Test 5)\nRank: {result}")
        Plotter.wait_for_next(fig)
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 6: Empty Matrix{Colors.ENDC}")
        mat = Matrix([])
        print(f"{Colors.OKBLUE}Matrix: {mat}{Colors.ENDC}")
        
        print(f"{Colors.WARNING}Skipping plotting for empty matrices.{Colors.ENDC}")
        
        rref = mat.row_echelon()
        print(f"{Colors.OKCYAN}\nRow-Echelon Form:\n{rref}{Colors.ENDC}")
        result = mat.rank()
        print(f"{Colors.OKGREEN}\nResult:\n{result}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    test_rank()