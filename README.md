# OnceNAS test Summary

## 1. Environment Setup and Dependency Installation

After creating a virtual machine on Google Cloud Platform (GCP), the first step was setting up the virtual environment and installing the necessary dependencies. When encountering the externally-managed-environment error, the solution was to install the libraries in a virtual environment.

### Create a virtual environment
```bash
python3 -m venv myenv
```

### Activate the virtual environment
```bash
source myenv/bin/activate
```

### Install required libraries
```bash
pip install torch torchvision
pip install darts-bench
```

## 2. Cloning the OnceNAS Repository

After configuring the SSH key, the OnceNAS repository was successfully cloned from GitHub.

### Generate SSH key
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

### Add SSH key to GitHub
```bash
ssh-add ~/.ssh/id_rsa
```

### Clone the OnceNAS repository
```bash
git clone https://github.com/OnceNAS-Bench/OnceNAS-Bench.git
```

## 3. Evaluating OnceNAS Architectures

OnceNAS provides an API that allows for loading architecture data and performing architecture evaluations. You used the `DartsBenchAPI` from `api_darts.py` to load the dataset and define the architecture. The codes are shown in `run_once_search.py`.
```python
from api_darts import DartsBenchAPI as API

# Load the DARTS-Bench dataset
api = API('data_545.pkl', verbose=False)

# Define the Genotype architecture string
str = "Genotype(normal=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 0), ('dil_conv_5x5', 2), " \
      "('avg_pool_3x3', 2), ('dil_conv_3x3', 1), ('dil_conv_3x3', 2), ('none', 0)], " \
      "normal_concat=range(2, 6), " \
      "reduce=[('dil_conv_3x3', 0), ('none', 1), ('sep_conv_5x5', 2), ('avg_pool_3x3', 0), " \
      "('skip_connect', 0), ('dil_conv_3x3', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 3)], " \
      "reduce_concat=range(2, 6))"

# Convert architecture string to a list (reduction=True means reduce cell)
arch = api.str2lists(str, reduction=True)
print('There are {:} nodes with optional operations in this reduce cell'.format(len(arch)))
for i, node in enumerate(arch):
    print('The {:}-th node (node {:}) is with op: {:}'.format(i + 3, i + 2, node))

# Convert architecture string to a list (reduction=False means normal cell)
arch = api.str2lists(str, reduction=False)
print('There are {:} nodes with optional operations in this normal cell'.format(len(arch)))
for i, node in enumerate(arch):
    print('The {:}-th node (node {:}) is with op: {:}'.format(i + 3, i + 2, node))

# Print the architecture matrix representation
arch_matrix = api.str2matrix(str)
print('Architecture matrix:', arch_matrix)

```


## 4. Running and Viewing Results

By running the `run_once_search.py` script, you successfully evaluated the architecture. The output provided detailed information about the nodes in the reduce cell and normal cell, as well as the architecture’s matrix representation.

### Run the architecture evaluation script
```bash
python run_once_search.py
```

![image](https://github.com/user-attachments/assets/3e96315f-c75a-4bf8-9688-177f795924b2)

## 5. Result Analysis

### 1. Reduce Cell
This section represents the reduce cell in the network architecture. In DARTS, the reduce cell is responsible for reducing the size of feature maps, usually through pooling or convolution operations. It contains several nodes, and each node applies different operations.

```
There are 4 nodes with optional operations in this reduce cell
The 3-th node (node 2) is with op: [('dil_conv_3x3', 0), ('none', 1)]
The 4-th node (node 3) is with op: [('sep_conv_5x5', 2), ('avg_pool_3x3', 0)]
The 5-th node (node 4) is with op: [('skip_connect', 0), ('dil_conv_3x3', 1)]
The 6-th node (node 5) is with op: [('dil_conv_5x5', 0), ('sep_conv_5x5', 3)]
```

- **The 3-th node (node 2)**: This node executes two operations:
  - `('dil_conv_3x3', 0)`: Uses 3x3 dilation convolution connected to node 0.
  - `('none', 1)`: A skip connection (none) to node 1.

- **The 4-th node (node 3)**: This node executes two operations:
  - `('sep_conv_5x5', 2)`: Uses 5x5 separable convolution connected to node 2.
  - `('avg_pool_3x3', 0)`: Uses 3x3 average pooling connected to node 0.

The remaining nodes follow a similar pattern, describing the operations each node performs and the nodes they connect to.

### 2. Normal Cell
The normal cell is responsible for keeping the feature map size constant. Like the reduce cell, it contains multiple nodes, each executing different operations.

```
There are 4 nodes with optional operations in this normal cell
The 3-th node (node 2) is with op: [('max_pool_3x3', 0), ('sep_conv_5x5', 1)]
The 4-th node (node 3) is with op: [('sep_conv_5x5', 0), ('dil_conv_5x5', 2)]
The 5-th node (node 4) is with op: [('avg_pool_3x3', 2), ('dil_conv_3x3', 1)]
The 6-th node (node 5) is with op: [('dil_conv_3x3', 2), ('none', 0)]
```

- **The 3-th node (node 2)**: This node performs two operations:
  - `('max_pool_3x3', 0)`: Uses 3x3 max pooling connected to node 0.
  - `('sep_conv_5x5', 1)`: Uses 5x5 separable convolution connected to node 1.

The rest of the nodes are described in a similar format, indicating the operations they perform and the connections between them.

### 3. Architecture Matrix
The architecture matrix is a 2D array that represents the connections between operations and nodes in the network. Each row in the matrix corresponds to a node in the architecture, and each number represents an operation or connection.

```
Architecture matrix: [[[1. 5. 0. 0. 0.]
                       [5. 0. 7. 0. 0.]
                       [0. 6. 2. 0. 0.]
                       [0. 0. 6. 0. 0.]]

                      [[6. 0. 0. 0. 0.]
                       [2. 0. 5. 0. 0.]
                       [3. 6. 0. 0. 0.]
                       [7. 0. 0. 5. 0.]]]
```

The matrix provides a numerical representation of the operations and the nodes they connect to in the architecture.

## PS:
As shown in screenshot, the open-source code of OnceNAS only retains the evaluation part based on DARTS. This is of limited significance, and the virtual machine has been deleted to save costs. Therefore, most of the content, except for the output screenshots, is reconstructed from memory and may contain errors.
![image](https://github.com/user-attachments/assets/4c99692f-253e-4f92-9ea0-25bb1aea854c)

