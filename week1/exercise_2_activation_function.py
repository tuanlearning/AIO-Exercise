
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


import math
def sigmoid(x):
    assert is_number(x), "x must be a number"
    return 1/(1+math.exp(-x))

def relu(x):
    assert is_number(x), "x must be a number"
    if x > 0:
        return x
    else:
        return 0

def elu(x, alpha = 0.01):
    assert is_number(x), "x must be a number"
    assert is_number(alpha), "alpha must be a number"
    if x > 0:
        return x
    else:
        return alpha*(math.exp(x) - 1)

x = float(input('Input x value: '))
function_type = input('Input activation function: ')

assert function_type in ('elu','relu','sigmoid'), f'{function_type} is not supported'

if function_type == 'elu':
    print(f'Input activation Function (sigmoid|relu|elu): elu')
    print(f'elu: f{x} = {elu(x)}')

if function_type == 'relu':
    print(f'Input activation Function (sigmoid|relu|elu): relu')
    print(f'relu: f{x} = {relu(x)}')

if function_type == 'sigmoid':
    print(f'Input activation Function (sigmoid|relu|elu): sigmoid')
    print(f'sigmoid: f{x} = {sigmoid(x)}')