import pandas

def import_file_data(filename):
	file = open(filename)
	fl = file.readlines()
	ret = []
	for line in fl:
		line = line.strip()
		attr = line.split(", ")
		ret.append(attr)
		# print(attr)
	return ret

def separate_labels(dataset, label_column=-1):
	if (label_column == -1):
		label_column = len(dataset[0])-1
	labels = []
	for data in dataset:
		labels.append(data[label_column])
		del data[label_column]
	return dataset, labels

def drop_columns(dataset, remove_column):
	for data in dataset:
		for col in sorted(remove_column, reverse=True):
			del data[col]
	return dataset

def import_data(filename, remove_column):
	dataset = import_file_data(filename)
	dataset = dataset[0:len(dataset)-1]
	dataset = drop_columns(dataset, remove_column)
	return dataset

def import_test(filename, remove_column):
	dataset = import_file_data(filename)
	dataset = dataset[1:len(dataset)-1]
	dataset = drop_columns(dataset, remove_column)
	return dataset

def convert_to_int(dataset):
	ret = []
	for data in dataset:
		ret.append([int(att) for att in data])
		# print(data)
	return ret

filename = "CensusIncome/CencusIncome.data.txt"
dataset = import_data(filename, [1,3,5,6,7,8,9,13])
dataset, datalabels = separate_labels(dataset)
filename = "CensusIncome/CencusIncome.test.txt"
testset = import_test(filename, [1,3,5,6,7,8,9,13])
testset, testlabels = separate_labels(testset)

dataset = convert_to_int(dataset)
testset = convert_to_int(testset)

for data in dataset:
	print(data)
print("TEST VVVVVVVV DATA ^^^^^^^^^^")
for data in testset:
	print(data)

# data_frame = pandas.read_csv("CencusIncome.data.csv")
# # print(data.as_matrix())

# data_frame_numeric = data_frame.drop(columns=['workclass','education','marital-status','occupation','relationship','race','sex','native-country'])
# data_frame_numeric_noclass = data_frame_numeric.drop(columns=['annual-salary'])

# print(data_frame_numeric_noclass)

# data_matrix_numeric_noclass = data_frame_numeric_noclass.as_matrix()
# print(data_matrix_numeric_noclass)

# def calculateClusterCenters():
# 	cluster_centers = []
# 	for center_idx in range(num_clusters):
# 		for data in data_matrix_numeric_noclass:
			


# def calculateMembershipMatrix():


# num_clusters = input("Num Clusters: ")
# m = input("m: ")
