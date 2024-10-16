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
