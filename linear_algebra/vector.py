from typing import List, Tuple, Union
import math

class Vector:
    def __init__(self, data: List[Union[int, float]]):
        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("All elements of the vector must be numeric (int or float).")
        self.data = data
    
    def add(self, other: 'Vector') -> 'Vector':
        """Element-wise addition"""
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must be same length")
        return Vector([a + b for a, b in zip(self.data, other.data)])
    
    def sub(self, other: 'Vector') -> 'Vector':
        """Element-wise subtraction"""
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must be same length")
        return Vector([a - b for a, b in zip(self.data, other.data)])
    
    def scl(self, scalar: float) -> 'Vector':
        """Scalar multiplication"""
        return Vector([x * scalar for x in self.data])

    @staticmethod
    def linear_combination(vectors: List['Vector'], coefficients: List[float]) -> 'Vector':
        """Creates a linear combination of vectors
        v = α₁v₁ + α₂v₂ + ... + αₖvₖ (where k ≤ n, n is the number of vectors)
        """
        if not vectors or not coefficients:
            raise ValueError("Vectors and coefficients must not be empty")
        
        if len(coefficients) > len(vectors):
            raise ValueError("Number of coefficients cannot exceed the number of vectors")
        
        vector_size = len(vectors[0].data)
        if not all(len(vec.data) == vector_size for vec in vectors):
            raise ValueError("All vectors must have the same size")
        
        if not all(isinstance(coeff, (int, float)) for coeff in coefficients):
            raise TypeError("All coefficients must be numeric (int or float)")
        
        result = [0.0] * vector_size
        
        for vec, coeff in zip(vectors, coefficients):
            for i in range(len(vec.data)):
                result[i] += vec.data[i] * coeff
        
        return Vector(result)
    
    @staticmethod
    def lerp(u: Union[float, 'Vector'], v: Union[float, 'Vector'], t: float) -> Union[float, 'Vector']:
        """Linear interpolation between two points
        lerp(u, v, t) = u + t(v - u)
        """
        if isinstance(u, (int, float)) and isinstance(v, (int, float)):
            return u + t * (v - u)
        elif isinstance(u, Vector) and isinstance(v, Vector):
            if len(u.data) != len(v.data):
                raise ValueError("Vectors must have same length")
            return Vector([a + t * (b - a) for a, b in zip(u.data, v.data)])
        else:
            raise TypeError("u and v must be both numbers or both vectors")
        
    @staticmethod
    def dot(u: 'Vector', v: 'Vector') -> float:
        """Dot product (inner product) of two vectors
        u·v = u₁v₁ + u₂v₂ + ... + uₙvₙ
        """
        if len(u) != len(v):
            raise ValueError("Vectors must have same dimension")
        return sum(a * b for a, b in zip(u.data, v.data))
    
    @staticmethod
    def norm_1(v: 'Vector') -> float:
        """Taxicab/Manhattan norm (L1 norm)
        Sum of absolute values
        ||v||₁ = |v₁| + |v₂| + ... + |vₙ|
        """
        return sum(abs(x) for x in v.data)

    @staticmethod
    def norm(v: 'Vector') -> float:
        """Euclidean norm (L2 norm)
        Standard "length" of a vector
        ||v||₂ = √(v₁² + v₂² + ... + vₙ²)
        """
        return math.sqrt(sum(x**2 for x in v.data))

    @staticmethod
    def norm_inf(v: 'Vector') -> float:
        """Maximum norm (L∞ norm)
        Largest component magnitude
        ||v||∞ = max(|v₁|, |v₂|, ..., |vₙ|)
        """
        if not v.data:
            return 0
        return max(abs(x) for x in v.data)
    
    @staticmethod
    def angle_cos(u: 'Vector', v: 'Vector', precision: int = 10) -> float:
        """Cosine of angle between two vectors
        cosθ = (u·v) / (||u||·||v||)
        """
        norm_u = Vector.norm(u)
        norm_v = Vector.norm(v)

        if norm_u == 0 or norm_v == 0:
            raise ValueError("Cannot compute the angle cosine with a zero or empty vector")

        cos_theta = Vector.dot(u, v) / (norm_u * norm_v)
        return round(cos_theta, precision)
    
    @staticmethod
    def cross_product(u: 'Vector', v: 'Vector') -> 'Vector':
        """3D Cross product
        u×v = (u₂v₃-u₃v₂, u₃v₁-u₁v₃, u₁v₂-u₂v₁)
        """
        if len(u) != 3 or len(v) != 3:
            raise ValueError("Cross product only defined for 3D vectors")
        
        return Vector([
            u.data[1] * v.data[2] - u.data[2] * v.data[1],
            u.data[2] * v.data[0] - u.data[0] * v.data[2],
            u.data[0] * v.data[1] - u.data[1] * v.data[0]
        ])
    
    #---Utils---#

    def size(self) -> int:
        """Returns the dimension of the vector"""
        return len(self.data)
    
    def shape(self) -> Tuple[int]:
        """Returns the shape (n,) where n is length"""
        return (len(self.data),)
    
    def reshape(self, rows: int, cols: int) -> 'Matrix':
        """Convert vector to matrix"""
        from .matrix import Matrix
        if rows * cols != len(self.data):
            raise ValueError("Shape mismatch for reshaping")
        return Matrix([self.data[i*cols:(i+1)*cols] for i in range(rows)])
    
    def __str__(self):
        return f"Vector({self.data})"
    
    def __len__(self) -> int:
        """Returns the number of elements in the vector (for len())."""
        return self.size()
