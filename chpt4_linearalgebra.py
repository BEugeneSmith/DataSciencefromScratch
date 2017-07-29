from math import sqrt

# vector things
def vector_add(v,w):
    """ adds corresponding elements of two vectors """
    return [v_i + w_i for v_i,v_i in zip(v,w)]

def vector_subtract(v,w):
    """ subtracts corresponding elements of two vectors """
    return [v_i - w_i for v_i,v_i in zip(v,w)]

def vector_sum(vectors):
    """ sums all corresponding elements """
    result = vector[0]
    for vector in vectors[1:]:
        result = vector_add(result,vector)
    return result

def scalar_multiply(c,v):
    """ multiply scalar c times vector v """
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """ compute vector's ith element is the mean """
    # of the ith elements of the input vectors
    n = len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))

def dot(v,w):
    """ compute component wise product of two vectors """
    return sum(v_i * w_i for v_i,v_i in zip(v,w))

def sum_of_squares(v):
    # TODO
    return dot(v,v)

def magnitude(v):
    # length of a vector in projection
    return math.sqrt(sum_of_squares(v))

def squared_distance(v,w):
    """ distance between two vectors """
    return sum_of_squares(vector_subtract(v,w))

def distance(v,w):
    """ distance between two vectors """
    return magnitude(vector_subtract(v,w))

# matrices
def shape(A):
    """ return shape of a matrix """
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows,num_cols

def get_row(A,i):
    return A[i]

def get_col(A,j):
    return [A_i[j] for A_i in A]

def make_matrix(num_rows,num_cols,entry_fn):
    return [[entry_fn(i,j), for j in range(num_cols)] for i in range(num_cols)]

def is_diagonal(i,j):
    return 1 if i == j else 0
