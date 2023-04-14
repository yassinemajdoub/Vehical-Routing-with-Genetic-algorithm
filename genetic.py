import numpy as np

# Define the parameters of the problem
num_tasks = 10
num_resources = 5
pop_size = 20

# Generate an initial population randomly
pop = np.random.randint(low=0, high=num_resources, size=(pop_size, num_tasks))