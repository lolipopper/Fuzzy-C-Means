<<<<<<< a91b877870fe931537350ca7c1490d7058599ed1
=======
import pandas
import math
import random

>>>>>>> Fuzzy
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

def normalize_data(dataset):
	mini = list(dataset[0])
	maks = list(dataset[0])
	for data in dataset:
		for i in range(len(data)):
			if (mini[i] > data[i]):
				mini[i] = data[i]
				# print("MINI")
			if (maks[i] < data[i]):
				maks[i] = data[i]
				# print("MAKS")
	ret = []
	for data in dataset:
		ret.append([(data[i]-mini[i])/(maks[i]-mini[i]) for i in range(len(data))])
	return ret

def init_membership_table(dataset, num_clusters):
	i = 0
	membership_table = []
	for data in dataset:
		membership_data = []
		for j in range (0, num_clusters):
			membership_data.append(random.uniform(0, 1))
		membership_table.append(membership_data)
	return membership_table

def data_times_number(data, number):
	new_data=[]
	i = 0
	for data_value in data:
		new_data.append(data_value*number)
	return new_data

def data_divided_number(data, number):
	new_data=[]
	i = 0
	for data_value in data:
		new_data.append(data_value/number)
	return new_data

def data_add_data(data1, data2):
	new_data = []

	if(len(data1)>len(data2)):
		max_len = len(data1)
	else:
		max_len = len(data2)

	for i in range(max_len):
		if(len(data1)<=i):
			new_data.append(data2[i])
		elif(len(data2)<=i):
			new_data.append(data1[i])
		else:
			new_data.append(data1[i]+data2[i])
	return new_data

def data_min_data(data1, data2):
	new_data = []

	if(len(data1)>len(data2)):
		max_len = len(data1)
	else:
		max_len = len(data2)

	for i in range(max_len):
		if(len(data1)<=i):
			new_data.append(data2[i])
		elif(len(data2)<=i):
			new_data.append(data1[i])
		else:
			new_data.append(data1[i]-data2[i])
	return new_data

def count_distance(data):
	temp = 0
	for data_value in data:
		temp += pow(data_value, 2)
	return math.sqrt(temp)

def calculate_centroid(dataset, membership_table, num_clusters, m_value):
	centroids = []
	divident = []
	divisor = 0
	for i in range(0, num_clusters):
		j = 0
		for data in dataset:
			divident = data_add_data(divident, data_times_number(data, pow(membership_table[j][i],m_value)))
			divisor += pow(membership_table[j][i],m_value)
			j+=1
		print(data_divided_number(divident,divisor))
		centroids.append(data_divided_number(divident,divisor))
	return centroids

def update_membership(dataset, membership_table, num_clusters, m_value):
	centroids = calculate_centroid(dataset, membership_table, num_clusters, m_value)
	new_membership_table = []
	i = 0
	for data in dataset:
		new_membership_data = []

		for j in range(0, num_clusters):
			divisor = 0
			for k in range(0, num_clusters):
				divisor += pow(count_distance(data_min_data(data, centroids[j]))/count_distance(data_min_data(data, centroids[k])),(2/(m_value-1)))
			new_membership_data.append(1/divisor)

		new_membership_table.append(new_membership_data)
		i+=1
	return new_membership_table

def max_membership_change(mem_old, mem_new):
	max_changes = mem_new[0][0]
	for i in range(len(mem_new)):
		for j in range(len(mem_new[i])):
			temp = abs(mem_new[i][j] - mem_old[i][j])
			if(temp>max_changes):
				max_changes = temp
	print(max_changes)
	return max_changes

def is_stop(mem_old, mem_new, epsilon):
	if(max_membership_change(mem_old, mem_new) <= epsilon):
		return True
	else:
		return False

def evaluate(dataset, membership_table):
	print("MASUK EVAL")
	ret = [0, 0]
	i = 0
	for data in dataset:
		temp = 0
		for j in range(len(membership_table[i])):
			if(membership_table[i][j] > membership_table[i][temp]):
				temp = j
		ret[temp] += 1
	return ret

filename = "CensusIncome/CencusIncome.data.txt"
dataset = import_data(filename, [1,3,5,6,7,8,9,13])
dataset, datalabels = separate_labels(dataset)
filename = "CensusIncome/CencusIncome.test.txt"
testset = import_test(filename, [1,3,5,6,7,8,9,13])
testset, testlabels = separate_labels(testset)

dataset = convert_to_int(dataset)
testset = convert_to_int(testset)

# dataset = normalize_data(dataset)
# testset = normalize_data(testset)


num_clusters = int(input("Num Clusters: "))
m_value = int(input("M: "))
epsilon = float(input("Epsilon: "))
membership_table = init_membership_table(dataset, num_clusters)
# print(data_add_data([1,1,2,3,1],[1,2,3]))
# print(data_times_number(dataset[0],2))
# print(calculate_centroid(dataset, membership_table, num_clusters, m_value))
new_membership_table = update_membership(dataset, membership_table, num_clusters, m_value)
print("COBA PRINT")

while(not is_stop(membership_table, new_membership_table, epsilon)):
	print("MASUK WHILE")
	membership_table = new_membership_table
	new_membership_table = update_membership(dataset, membership_table, num_clusters, m_value)
	print("COBA EVAL")
	print(evaluate(dataset, new_membership_table))


# for data in dataset:
# 	print(data)
# print("TEST VVVVVVVV DATA ^^^^^^^^^^")
# for data in testset:
# 	print(data)

# print(datalabels)
# print(testlabels)

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


