import numpy as np
def preprocess_input(x):
    x=x/255.
    x-=0.5
    x*=2.
    return x
