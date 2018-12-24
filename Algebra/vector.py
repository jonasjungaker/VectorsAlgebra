class vector:
    def __init__(self, *vals):
        self.x = list(vals)
        for val in vals:
            float(val)
        self.dimension = len(self.x)

    def __getitem__(self, key):
        return self.x[key]

    def __setitem__(self, key, value):
        self.x[key] = value
        return self

    def __add__(self, other):
        if type(other) == type(int): # This also needs to support floating point types
            for i in range(self.dimension):
                self[i] += other
            return self
        self._checkDimension(other)
        newx = []
        for i in range(self.dimension):
            newx.append(self[i] + other[i])
        return vector(*newx)

    def __eq__(self, other):
        if self.dimension != other.dimension:
            return False
        for i in range(self.dimension):
            if self[i] != other[i]:
                return False
        return True

    def __mul__(self, other):
        if type(other) == type(int):
            x = []
            for i in range(self.dimension):
                x.append(self[i] * other)
            return vector(*x)
        self._checkDimension(other)
        value = 0
        for i in range(self.dimension):
            value += self[i] * other[i]
        return value

    def __rmul__(self, other):
        return self * other

    def __matmul__(self, other):
        if self.dimension != other.dimension != 3:
            raise TypeError("Vector dimensions must be 3")
        v = vector(0, 0, 0)
        v[0] = (self[1] * other[2]) - (self[2] * other[1])
        v[1] = (self[2] * other[0]) - (self[0] * other[2])
        v[2] = (self[0] * other[1]) - (self[1] * other[0])
        return v

    def __sub__(self, other):
        return self + ( - other)

    def __neg__(self):
        v = []
        for i in range(self):
            v.append( - self[i])
        return vector(*v)

    def __abs__(self):
        value = self.magnitude()
        return value**0.5

    def _checkDimension(self, other):
        if self.dimension != other.dimension:
            raise TypeError("Vector dimensions must agree")

    def magnitude(self):
        # Returns the value of the sum of all values of the vector squared
        powerMagnitude = 0
        for a in self.x:
            powerMagnitude += a*a
        return powerMagnitude

    
