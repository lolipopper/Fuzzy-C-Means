import pandas

def import_file_data(filename):
	file = open(filename)
	fl = file.readlines()
	ret = []
	for line in fl:
		line = line.strip()
		attr = line.split(", ")
		ret.append(attr)
		print(attr)
	return ret

def import_data(filename, remove_column)
	dataset = import_file_data(filename)
	dataset = data[0:len(data)-1]
	for data in dataset:
		for col in sorted(remove_column, reverse=True):
			del my_list[col]
	return data

filename = "CensusIncome/CencusIncome.data.txt"
dataset = import_file_data(filename, )
print(dataset)

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
