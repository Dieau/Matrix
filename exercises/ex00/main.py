import sys
sys.path.append('../../')
from linear_algebra.vector import Vector
from linear_algebra.matrix import Matrix
from utils.colors import Colors
from utils.plotter import Plotter

def test_vector_operations():
    print(f"{Colors.HEADER}\n=== Vector Operations Test ===\n{Colors.ENDC}")
    
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    
    print(f"{Colors.OKBLUE}v1: {v1}\nsize: {v1.size()}, shape: {v1.shape()}\n{Colors.ENDC}")
    print(f"{Colors.OKBLUE}v2: {v2}\nsize: {v2.size()}, shape: {v2.shape()}\n{Colors.ENDC}")
    
    fig = Plotter.plot_vector([v1, v2], labels=["v1", "v2"], colors=["red", "blue"], title="Initial Vectors")
    Plotter.wait_for_next(fig)
    
    print(f"\n{Colors.BOLD}Basic Operations:{Colors.ENDC}")
    
    result = v1.add(v2)
    print(f"\n{Colors.OKGREEN}Addition: {v1} + {v2} = {result}\n{Colors.ENDC}")
    fig = Plotter.plot_vector([v1, v2, result], labels=["v1", "v2", "v1 + v2"], colors=["red", "blue", "green"], title="Vector Addition")
    Plotter.wait_for_next(fig)
    
    result = v1.sub(v2)
    print(f"{Colors.OKGREEN}Subtraction: {v1} - {v2} = {result}\n{Colors.ENDC}")
    fig = Plotter.plot_vector([v1, v2, result], labels=["v1", "v2", "v1 - v2"], colors=["red", "blue", "green"], title="Vector Subtraction")
    Plotter.wait_for_next(fig)
    
    result = v1.scl(2.5)
    print(f"{Colors.OKGREEN}Scaling (2.5): {v1} * 2.5 = {result}\n{Colors.ENDC}")
    fig = Plotter.plot_vector([v1, result], labels=["v1", "v1 * 2.5"], colors=["red", "green"], title="Vector Scaling")
    Plotter.wait_for_next(fig)


def test_matrix_operations():
    print(f"{Colors.HEADER}\n=== Matrix Operations Test ===\n{Colors.ENDC}")
    
    m1 = Matrix([
        [1, 2, 3],
        [4, 5, 6]
    ])
    m2 = Matrix([
        [7, 8, 9],
        [10, 11, 12]
    ])
    
    print(f"{Colors.OKBLUE}m1: {m1.__repr__()}\nsize: {m1.size()}, shape: {m2.shape()}\n{Colors.ENDC}")
    print(f"{Colors.OKBLUE}m2: {m2.__repr__()}\nsize: {m2.size()}, shape: {m2.shape()}\n{Colors.ENDC}")
    
    print("\nVisualizing matrices:")
    fig = Plotter.plot_matrix_wireframe(m1, title="Matrix m1 (Wireframe)")
    Plotter.wait_for_next(fig)
    
    fig = Plotter.plot_matrix_wireframe(m2, title="Matrix m2 (Wireframe)")
    Plotter.wait_for_next(fig)
    
    print(f"\n{Colors.BOLD}Basic Operations:\n{Colors.ENDC}")
    
    result = m1.add(m2)
    print(f"{Colors.OKGREEN}Addition:\n{m1.__repr__()} + {m2.__repr__()}\n= {result}{Colors.ENDC}")
    fig = Plotter.plot_matrix_wireframe(result, title="Matrix Addition (Wireframe)")
    Plotter.wait_for_next(fig)
    
    result = m1.sub(m2)
    print(f"{Colors.OKGREEN}\nSubtraction:\n{m1.__repr__()} - {m2.__repr__()}\n= {result}{Colors.ENDC}")
    fig = Plotter.plot_matrix_wireframe(result, title="Matrix Subtraction (Wireframe)")
    Plotter.wait_for_next(fig)
    
    result = m1.scl(2.5)
    print(f"{Colors.OKGREEN}\nScaling (2.5): {m1.__repr__()} * 2.5\n= {result}{Colors.ENDC}")
    fig = Plotter.plot_matrix_wireframe(result, title="Matrix Scaling (Wireframe)")
    Plotter.wait_for_next(fig)

if __name__ == "__main__":
    test_vector_operations()
    test_matrix_operations()