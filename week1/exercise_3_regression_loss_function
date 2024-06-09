import random
import math

def generate_samples(num_samples):
    targets = [random.randint(0,10) for i in range(num_samples)]
    predicts = [random.randint(0,10) for i in range(num_samples)]
    return targets, predicts

def mean_absolute_error(targets, predicts):
    result = sum([abs(y_pred - y_tar) for y_pred,y_tar in zip(targets,predicts)])/len(targets)
    print(f'loss name: mae, sample: {len(targets)}, loss: {result}')
def mean_square_error(targets, predicts):
    result = sum([(y_pred - y_tar)**2 for y_pred,y_tar in zip(targets,predicts)])/len(targets)
    print(f'loss name: mse, sample: {len(targets)}, loss: {result}')
def root_mean_square_error(targets, predicts):
    result = math.sqrt(sum([(y_pred - y_tar)**2 for y_pred,y_tar in zip(targets,predicts)])/len(targets))
    print(f'loss name: rmse, sample: {len(targets)}, loss: {result}')

num_samples = input("please input number of samples: ")
try:
    num_samples = int(num_samples)
except:
    raise ValueError('number of samples must be integer')

loss_name = input("please input the loss name: (mae|mse|rmse): ")

if loss_name not in ('mae','mse','rmse'):
    raise ValueError(f'{loss_name} is not supported')

targets, predicts = generate_samples(num_samples)
print(f'targets:{targets}')
print(f'predicts:{predicts}')

if loss_name == 'mae':
    mean_absolute_error(targets, predicts)
elif loss_name == 'mse':
    mean_square_error(targets,predicts)
elif loss_name == 'rmse':
    root_mean_square_error(targets, predicts)