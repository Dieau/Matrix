from typing import List, Tuple, Union

class Matrix:
    def __init__(self, data: List[List[Union[int, float]]]):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows in the matrix must have the same length.")
        
        if not all(isinstance(x, (int, float)) for row in data for x in row):
            raise TypeError("All elements of the matrix must be numeric (int or float).")
        
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0
    
    def add(self, other: 'Matrix') -> 'Matrix':
        """Element-wise matrix addition"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have same dimensions")
        return Matrix([
            [a + b for a, b in zip(row_a, row_b)]
            for row_a, row_b in zip(self.data, other.data)
        ])
    
    def sub(self, other: 'Matrix') -> 'Matrix':
        """Element-wise matrix subtraction"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have same dimensions")
        return Matrix([
            [a - b for a, b in zip(row_a, row_b)]
            for row_a, row_b in zip(self.data, other.data)
        ])
    
    def scl(self, scalar: float) -> 'Matrix':
        """Matrix scalar multiplication"""
        return Matrix([
            [x * scalar for x in row]
            for row in self.data
        ])
        
    @staticmethod
    def lerp(u: Union[float, 'Matrix'], v: Union[float, 'Matrix'], t: float) -> Union[float, 'Matrix']:
        """Linear interpolation between two matrices or scalars
        lerp(u, v, t) = u + t(v - u)
        """
        if isinstance(u, (int, float)) and isinstance(v, (int, float)):
            return u + t * (v - u)
        
        elif isinstance(u, Matrix) and isinstance(v, Matrix):
            if u.rows != v.rows or u.cols != v.cols:
                raise ValueError("Matrices must have identical dimensions for interpolation")
                
            return Matrix([
                [a + t * (b - a) for a, b in zip(row_u, row_v)]
                for row_u, row_v in zip(u.data, v.data)
            ])
        
        else:
            raise TypeError("Both arguments must be either numbers or matrices")
        
    def mul_vec(self, vec: 'Vector') -> 'Vector':
        """Matrix-vector multiplication
        Each output component is the dot product of a matrix row with an input vector
        """
        from .vector import Vector

        if self.cols != len(vec):
            raise ValueError("Matrix columns must match vector length")
        
        result = []
        for row in self.data:
            component = sum(a * b for a, b in zip(row, vec.data))
            result.append(component)
        
        return Vector(result)
    
    def mul_mat(self, other: 'Matrix') -> 'Matrix':
        """Matrix-matrix multiplication
        C[i][j] = sum(A[i][k] * B[k][j] for k in range(A.cols))
        """
        if self.cols != other.rows:
            raise ValueError("Inner dimensions must match for multiplication")
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                component = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                row.append(component)
            result.append(row)
        
        return Matrix(result)
    
    def trace(self) -> float:
        """Trace of a square matrix
        tr(A) = A₁₁ + A₂₂ + ... + Aₙₙ
        """
        if not self.is_square():
            raise ValueError("Trace only defined for square matrices")
        return sum(self.data[i][i] for i in range(self.rows))
    
    def transpose(self) -> 'Matrix':
        """Matrix transpose
        Aᵀ[i][j] = A[j][i]
        """
        return Matrix([[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)])
        
    def row_echelon(self) -> 'Matrix':
        """Row-echelon form (Gauss-Jordan elimination)
        - Leading pivot is 1
        - Each pivot is to the right of the one above
        - Rows with all zeros are at the bottom
        """
        if not self.data:
            return Matrix([])

        matrix = [row.copy() for row in self.data]
        lead = 0

        for r in range(self.rows):
            if lead >= self.cols:
                break

            i = r
            while matrix[i][lead] == 0:
                i += 1
                if i == self.rows:
                    i = r
                    lead += 1
                    if lead == self.cols:
                        return Matrix(matrix)

            matrix[i], matrix[r] = matrix[r], matrix[i]

            lv = matrix[r][lead]
            if lv != 0:
                matrix[r] = [x / lv for x in matrix[r]]

            for i in range(self.rows):
                if i != r:
                    lv = matrix[i][lead]
                    matrix[i] = [iv - lv * rv for iv, rv in zip(matrix[i], matrix[r])]

            lead += 1
            
            for r in range(len(matrix)):
                matrix[r] = [0.0 if x == -0.0 else x for x in matrix[r]]

        return Matrix(matrix)
    
    def determinant(self, precision: int = 10) -> float:
        """Matrix determinant
        Scalar value encoding the key properties of a linear transformation
        - Volume scaling factor in 3D spaces
        - Area scaling factor in 2D spaces
        - Zero if matrix is singular
        """
        if not self.is_square():
            raise ValueError("Determinant only defined for square matrices")
        
        if not self.data:
            raise ValueError("Determinant not defined for empty matrices")
        
        n = self.rows
        
        if n == 1:
            return round(self.data[0][0], precision)
        elif n == 2:
            return round(self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0], precision)
        elif n == 3:
            a, b, c = self.data[0]
            d, e, f = self.data[1]
            g, h, i = self.data[2]
            return round(a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g), precision)
        elif n == 4:
            matrix = [row.copy() for row in self.data]
            det = 1
            for i in range(n):
                pivot_row = i
                while pivot_row < n and abs(matrix[pivot_row][i]) < 1e-10:
                    pivot_row += 1
                if pivot_row == n:
                    return 0
                
                if pivot_row != i:
                    matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]
                    det *= -1
                
                pivot = matrix[i][i]
                if abs(pivot) < 1e-10:
                    return 0
                det *= pivot
                matrix[i] = [round(x / pivot, precision) for x in matrix[i]]
                
                for j in range(i + 1, n):
                    factor = matrix[j][i]
                    matrix[j] = [round(x - factor * y, precision) for x, y in zip(matrix[j], matrix[i])]
            
            return round(det, precision)
        else:
            raise NotImplementedError("Determinant for n>4 not implemented")
        
    def inverse(self, precision: int = 10) -> 'Matrix':
        """Matrix inverse
        The matrix that when multiplied by the original gives the identity matrix
        A·A⁻¹ = I
        """
        if not self.is_square():
            raise ValueError("Inverse only defined for square matrices")
        
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted")
        
        n = self.rows
        
        if n == 1:
            return Matrix([[round(1 / self.data[0][0], precision)]])
        elif n == 2:
            a, b = self.data[0]
            c, d = self.data[1]
            inv_det = 1 / det
            return Matrix([
                [round(d * inv_det, precision), round(-b * inv_det, precision)],
                [round(-c * inv_det, precision), round(a * inv_det, precision)]
            ])
        else:
            adjugate = []
            for i in range(n):
                adj_row = []
                for j in range(n):
                    minor = self._minor(i, j)
                    sign = (-1) ** (i + j)
                    adj_row.append(round(sign * minor.determinant(), precision))
                adjugate.append(adj_row)
            
            inverse = Matrix(adjugate).transpose()
            inverse = Matrix([[round(x / det, precision) for x in row] for row in inverse.data])
            return inverse
        
    def _minor(self, row: int, col: int) -> 'Matrix':
        """Creates a minor matrix by removing a row and column"""
        return Matrix([
            [self.data[i][j] for j in range(self.cols) if j != col]
            for i in range(self.rows) if i != row
        ])
        
    def rank(self) -> int:
        """
        Maximum number of linearly independent rows/columns
        """
        if not self.data:
            return 0

        rref = self.row_echelon()
        rank = 0
        
        for row in rref.data:
            if any(x != 0 for x in row):
                rank += 1
        
        return rank
    
    #---Utils---#

    def size(self) -> Tuple[int, int]:
        """Returns (rows, cols)"""
        return self.rows * self.cols

    def shape(self) -> Tuple[int, int]:
        """Returns (rows, cols)"""
        return (self.rows, self.cols)
    
    def is_square(self) -> bool:
        """Check if matrix is square"""
        return self.rows == self.cols
    
    def flatten(self) -> 'Vector':
        """Convert matrix to vector"""
        from .vector import Vector
        flattened = []
        for row in self.data:
            flattened.extend(row)
        return Vector(flattened)
    
    def __str__(self):
        return "Matrix:\n" + "\n".join(["[" + ", ".join(map(str, row)) + "]" for row in self.data])
    
    def __repr__(self):
        return f"Matrix({self.data})"