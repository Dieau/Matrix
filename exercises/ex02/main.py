import sys
sys.path.append('../../')
from linear_algebra.vector import Vector
from linear_algebra.matrix import Matrix
from utils.colors import Colors
from utils.plotter import Plotter

def test_lerp():
    print(f"{Colors.HEADER}\n=== Vector Linear Interpolation ===\n{Colors.ENDC}")
    
    try:
        print(f"{Colors.BOLD}Test 1: Scalar interpolation{Colors.ENDC}")
        u, v, t = 21.0, 42.0, 0.3
        print(f"{Colors.OKBLUE}u: {u}, v: {v}, t: {t}{Colors.ENDC}")
        result = Vector.lerp(u, v, t)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 2: Vector interpolation{Colors.ENDC}")
        v1 = Vector([2, 1, 3])
        v2 = Vector([4, 2, 6])
        t = 0.3
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}, t: {t}{Colors.ENDC}")
        
        fig = Plotter.plot_vector([v1, v2], labels=["v1", "v2"], colors=["red", "blue"], title="Initial Vectors")

        Plotter.wait_for_next(fig)
        
        result = Vector.lerp(v1, v2, t)
        print(f"{Colors.OKGREEN}Result: {result}{Colors.ENDC}")
        
        fig = Plotter.plot_vector([v1, v2, result], labels=["v1", "v2", "Result"], colors=["red", "blue", "green"], title="Vector Interpolation")

        Plotter.wait_for_next(fig)
        
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 3: Vector interpolation with mismatched sizes{Colors.ENDC}")
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5])
        t = 0.5
        print(f"{Colors.OKBLUE}v1: {v1}, v2: {v2}, t: {t}{Colors.ENDC}")
        result = Vector.lerp(v1, v2, t)
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")
        
    try:
        print(f"\n{Colors.BOLD}Test 4: Scalar interpolation with invalid types{Colors.ENDC}")
        u, v, t = "a", 3.0, 0.5
        print(f"{Colors.OKBLUE}u: {u}, v: {v}, t: {t}{Colors.ENDC}")
        result = Vector.lerp(u, v, t)
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except TypeError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")
        
    print(f"{Colors.HEADER}\n=== Matrix Linear Interpolation ===\n{Colors.ENDC}")
    
    try:
        print(f"{Colors.BOLD}Test 5: Matrix interpolation{Colors.ENDC}")
        m1 = Matrix([
            [2, 1],
            [3, 4]
        ])
        m2 = Matrix([
            [20, 10],
            [30, 40]
        ])
        t = 0.5
        print(f"{Colors.OKBLUE}m1: {m1.__repr__()}\nm2: {m2.__repr__()}\nt: {t}{Colors.ENDC}")
        
        result = Matrix.lerp(m1, m2, t)
        print(f"{Colors.OKGREEN}Result:\n{result}{Colors.ENDC}")
        
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 6: Matrix interpolation with mismatched dimensions{Colors.ENDC}")
        m1 = Matrix([
            [1, 2],
            [3, 4]
        ])
        m2 = Matrix([
            [5, 6, 7],
            [8, 9, 10]
        ])
        t = 0.5
        print(f"{Colors.OKBLUE}m1: {m1.__repr__()}\nm2: {m2.__repr__()}\nt: {t}{Colors.ENDC}")
        result = Matrix.lerp(m1, m2, t)
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except ValueError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 7: Matrix interpolation with invalid types{Colors.ENDC}")
        m1 = Matrix([
            [1, 2],
            [3, 4]
        ])
        m2 = "invalid"
        t = 0.5
        print(f"{Colors.OKBLUE}m1: {m1.__repr__()}\nm2: {m2}\nt: {t}{Colors.ENDC}")
        result = Matrix.lerp(m1, m2, t)
        print(f"{Colors.FAIL}This should not print: {result}{Colors.ENDC}")
    except TypeError as e:
        print(f"{Colors.OKGREEN}Caught expected error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    test_lerp()