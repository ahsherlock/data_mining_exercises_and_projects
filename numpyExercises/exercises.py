# #1: import Numpy
import numpy as np

# Create an array of zeros
print("#2: create an array of 10 zeros")
zero_Array = np.zeros(10)
print(zero_Array)
print("\n")

print("\n#3: create an array of 10 ones")
ones_Array = np.ones(10)
print(ones_Array)
print("\n")

print("#4: create an array of 10 fives")
# fill array with random shit
fives_array = np.arange(0, 10)
# broadcast all elements to 5.0
fives_array[0:10] = 5.0
print(fives_array)
#Correct answer
correct_fives = np.ones(10)*5
print(correct_fives)
print("\n")



print("#5: Create an array of the integers from 10 to 50")
ten_to_fifty = np.arange(10, 51)
print(ten_to_fifty)
print("\n")

print("Create an array of all the even integers from 10 to 50")
even_to_fifty = np.arange(10, 51, 2)
print(even_to_fifty)
print("\n")

print("Create a 3x3 matrix with values ranging from 0 to 8")
three_by_three = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
three_by_three = np.array(three_by_three)
print(three_by_three)
#Correct answer
correct_three = np.arange(9).reshape(3,3)
print("\n")

print("Create a 3x3 identity matrix.")
identity_matrix = np.eye(3)
print(identity_matrix)
print("\n")

print("Use NumPy to generate a random number between 0 and 1")
for i in range(11):
    random_number = np.random.rand()
    print("Random number {} is: {}".format(i, random_number))
print("\n")

print("Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution")
snd_array = np.random.randn(25)
print(snd_array)
print("\n")

print("Make a weird array...")
dumb_array = np.arange(0, 1, .01)
print(dumb_array)
print("\n")

print("Create an array of 20 linearly spaced points between 0 and 1")
linspace_array = np.linspace(0, 1, 20)
print(linspace_array)
print("\n")

print("Create this matrix: ")
print('''array([[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
       [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
       [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
       [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
       [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
       [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
       [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
       [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
       [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
       [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]]))''')
print("\nMy matrix:")
X = np.arange(1,101).reshape(10,10) / 100
print(X)
print("\n")

print("Create an array of 20 linearly spaced points between 0 and 1:")
betweenZeroAndOne = np.linspace(0,1,20)
print(betweenZeroAndOne)
print("\n")

print("Numpy indexing and selection exercises.")
matrix = np.arange(1,26).reshape(5,5)
print(matrix)
print("\n")



answer= '''array([[12, 13, 14, 15],
       [17, 18, 19, 20],
       [22, 23, 24, 25]])
        '''
print("\nmake this matrix: ", answer)

print("my matrix: ")
newSlice1 = matrix[2:,1:]
print(newSlice1)

#reset the original matrix
matrix = np.arange(1,26).reshape(5,5)
print("\n")
print(matrix)

answer= '''20
        '''
print("\nmake this matrix: ", answer)

print("my matrix: ")
myAnswer = matrix[3,4]
print(myAnswer)
print("\n")

#reset the original matrix
matrix = np.arange(1,26).reshape(5,5)
print(matrix)
print("\n")

answer= '''array([[ 2],
                  [ 7],
                  [12]])
        '''
print("\nmake this matrix: ", answer)


print("my matrix: ")

myAnswer = matrix[:3,1:2]
print(myAnswer)
print("\n")


print(" Sum all values in the matrix: ")
print("The sum of all values = ", matrix.sum())

print("\n Get the standard deviation of the values in the matrix.")
print("The Standard Deviation = ", matrix.std())

print("\n Get the sum of all the columns in the matrix.")
print("The Standard Deviation = ", matrix.sum(axis=0))