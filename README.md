# OnceNAS Project Summary

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

## 4. Running and Viewing Results

By running the `run_once_search.py` script, you successfully evaluated the architecture. The output provided detailed information about the nodes in the reduce cell and normal cell, as well as the architecture’s matrix representation.

### Run the architecture evaluation script
```bash
python run_once_search.py
```

![image](https://github.com/user-attachments/assets/3e96315f-c75a-4bf8-9688-177f795924b2)
