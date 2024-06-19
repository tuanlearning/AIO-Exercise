import torch
import torch.nn as nn
import torch.nn.functional as F

class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        return F.softmax(x, dim=0)

class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        # Subtracting the max value for numerical stability
        max_val = torch.max(x)
        stable_x = x - max_val
        return F.softmax(stable_x, dim=0)