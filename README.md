# VectorsAlgebra

This library aims to extend pythons ability for numbers and algebra and to make linear algebra easy. 


## Algebra
A library for easy matrix and vector algebra with python 3 as well as easy plotting graphs of list of numbers


### vector
A vector is in practice a list of integers or floating point numbers that has the functionality of an algebraic vector. Thi means that it supports most vector operations of general algebra such as vector addition, subtraction, dot product, cross product and scalar multiplication. This makes the vector datatype useful for linear algebra in any dimension. 

`vector.vector(*vals)`
	the constructor takes a list of floating point numbers or integers vals and returns a vector object which has the same dimension as the number of vals
	The constructor takes an unpacked list, example: `v1 = vector(1, 2, 3)` returns a vector object of dimension 3. To make a vector of a list of numbers `myList = [1, 2, 3]` the constructor is called `myVector = vector(*myList)`

`vector.magnitude()`
	gives the square of the absolut length of the vector which is useful for length comparison between vectors. Faster than `abs(vector)`

