# Gradient Descent based on a csv file imported directly ( 2 Columns of data per item )

from numpy import *

#mx + b -> Linear Regression

def compute_error_for_given_points( b, m , points ):
    totalError = 0
    for i in range(0 , len(points)):
        x = points[i,0]
        y = points[i,1]
        totalError+= ( y - (m*x+b) )**2
    return totalError / float (len(points))

def step_gradient( cb , cm , points , lr ):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))

    for i in range(0, len(points)):
        x = points[i,0]
        y = points[i,1]
        b_gradient +=  -(2/N) * ( y - ((cm * x) + cb))
        m_gradient +=  -(2/N) * x * ( y - ((cm * x) + cb))
    new_b = cb - (lr * b_gradient)
    new_m = cm - (lr * m_gradient)
    return[new_b, new_m]

def gradient_descent_runner(points, initial_b,initial_m,learning_rate, iterations):
    b = initial_b
    m = initial_m
    
    for i in range ( iterations ):
        b, m = step_gradient( b , m , array(points) , learning_rate )
    return [b,m]

def run():
    points = genfromtxt('data.csv', delimiter=',')
    learning_rate = 0.0001
    initial_b = 0
    initial_m = 0
    iterations = 1000
    [b , m] = gradient_descent_runner( points, initial_b,initial_m,learning_rate, iterations )
    print( 'Optimal point B: {} , optimal point M: {}'.format(b , m))

if __name__ == '__main__':
    run()