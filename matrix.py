class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix 
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __add__(self, other):
        if self.eq_dem(other) == True:
            i = 0
            while i < self.rows:
                j = 0
                while j < self.cols:
                    self.matrix[i][j] += other.matrix[i][j]
                    j+=1
                i+=1
            return Matrix(self.matrix)
        return "Matrices could not be added due to dimnension mismatch."

    def __sub__(self,other):
        if self.eq_dem(other) == True:
            i = 0
            while i < self.rows:
                j = 0
                while j < self.cols:
                    self.matrix[i][j] -= other.matrix[i][j]
                    j+=1
                i+=1
            return Matrix(self.matrix)
        return "Matrices could not be subtracted due to dimnension mismatch."

    def eq_dem(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            return True 
        return False 

    def multipliable(self, other):
        if self.cols == other.rows:
            return True 
        return False 

    def zeros(self, rows, cols, matrixorlist):
        new = []
        i = 0
        while i < rows:
            row = []
            j = 0 
            while j < cols:
                row.append(0)
                j+=1
            new.append(row)
            i+=1
        if matrixorlist == "matrix":
            return Matrix(new)
        return new

    def __mul__(self, other):
        if self.multipliable(other) == True:
            new = self.zeros(self.rows, other.cols, "list")
            for i in range(self.rows): 
                for j in range(other.cols):
                    for k in range(other.rows):
                        new[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(new)
        return "Matrices could not be multiplied due to dimension mismatch"

    def transpose(self):
        new = self.zeros(self.cols, self.rows, "list")
        for i in range(len(new[0])):
            for j in range(len(new)):
                new[j][i] = self.matrix[i][j]
        return Matrix(new)

    def determinant(self):
        if self.matrix.square() == True:
            print("square")
        print("square")

    def __pow__(self, power):
        if power == 0:
            return 1; # need to change to return identity matrix
        elif power == 1:
            return self.matrix; 
        elif power > 1:
            return self.__mul__(self)
            return Matrix(self.__mul__(self.__pow__(power - 1)))

    def identitymatrix(self, size):
        pass

    def inverse(self):
        pass

    def square(self):
        if self.rows == self.cols:
            return True 
        return False

    def __str__(self):
        string = ""
        i = 0
        while i < self.rows:
            j = 0
            while j < self.cols:
                string = string + str(self.matrix[i][j]) + " "
                j+=1
            string+="\n"
            i+=1
        return string
        
# TEST CODE     
m1 = Matrix([
    [1,7],
    [2,3]])
m2 = Matrix([
    [3,4],
    [5,6]])
m3 = Matrix([
    [3,4],
    [5,6]])

print(m1 ** 2)


def mul(a, b):
    return a * b

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    elif exponent > 1:
        return mul(base, power(base, exponent - 1))

