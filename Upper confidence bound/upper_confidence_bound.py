import numpy as np


def upper_confidence_bound(data):

	N = data.shape[0] # number of samples (Example: How many times add was shown, How many times machine was played)
	d = data.shape[1] # number of dfferent objects (Examples: Different ads, Bandit machines)

	#Ni(n) - the number of times the object 'i' was selected up until the nubmer n
	#Ri(n) - the sum of rewards of the object 'i' up to the number n

	#The idea is to have the best object at each iteration 1-n

	N_i_n = {}
	R_i_n = {}
	iter_object_selected = []
	#Setting starting values
	for i in range(d):
		N_i_n[i] = 0
		R_i_n[i] = 0

	total_results = 0 
	
	#The main loop
	for sample in range(N):
		object_selected = 0
		max_upper_bound = 0
		

		for object_ in range(d):

			if N_i_n[object_] > 0:
				average_reward = R_i_n[object_]/N_i_n[object_]
				delta_of_object = np.sqrt(3/2 * np.log(sample+1) / N_i_n[object_])
				upper_bound = average_reward + delta_of_object

			else:
				upper_bound = float("+inf")

			if upper_bound > max_upper_bound:
				max_upper_bound = upper_bound
				object_selected = object_

		
		iter_object_selected.append(object_selected)
		N_i_n[object_selected] += 1
		
		reward = data[sample, object_selected]
		
		R_i_n[object_selected] +=  reward

		total_results +=  reward

	return iter_object_selected, total_results
		

