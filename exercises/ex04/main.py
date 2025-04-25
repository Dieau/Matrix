import sys
sys.path.append('../../')
from linear_algebra.vector import Vector
from utils.colors import Colors

def test_norms():
    print(f"{Colors.HEADER}\n=== Norm Tests ===\n{Colors.ENDC}")
    
    try:
        print(f"{Colors.BOLD}Test 1: Valid vector{Colors.ENDC}")
        v = Vector([1, 2, 3])
        print(f"{Colors.OKBLUE}v: {v}{Colors.ENDC}")
        result_1 = Vector.norm_1(v)
        result_2 = Vector.norm(v)
        result_inf = Vector.norm_inf(v)
        print(f"{Colors.OKGREEN}L1 Result: {result_1}, L2 Result: {result_2}, L∞ Result: {result_inf}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 2: Norms of an empty vector{Colors.ENDC}")
        v = Vector([])
        print(f"{Colors.OKBLUE}v: {v}{Colors.ENDC}")
        result_1 = Vector.norm_1(v)
        result_2 = Vector.norm(v)
        result_inf = Vector.norm_inf(v)
        print(f"{Colors.OKGREEN}L1 Result: {result_1}, L2 Result: {result_2}, L∞ Result: {result_inf}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")
    
    try:
        print(f"\n{Colors.BOLD}Test 3: Norms of a zero vector{Colors.ENDC}")
        v = Vector([0, 0, 0])
        print(f"{Colors.OKBLUE}v: {v}{Colors.ENDC}")
        result_1 = Vector.norm_1(v)
        result_2 = Vector.norm(v)
        result_inf = Vector.norm_inf(v)
        print(f"{Colors.OKGREEN}L1 Result: {result_1}, L2 Result: {result_2}, L∞ Result: {result_inf}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Unexpected error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    test_norms()