import numpy as np
import random

def thompson_sampling(data):

	N = data.shape[0]
	d = data.shape[1]

	N1_n = {} #The number of times the object got reward (1) up to n
	N0_n = {} #The number of tmes the object got 0 up to n

	for i in range(d):
		N1_n[i] = 0
		N0_n[i] = 0

	total_score = 0
	iter_object_selected = []


	for sample in range(N):
		
		object_results_from_distribution = []

		for object_ in range(d):
			if data[sample, object_] == 1:
				N1_n[object_] += 1
			elif data[sample, object_] == 0:
				N0_n[object_] += 1
			else:
				continue
			object_results_from_distribution.append(random.betavariate(N1_n[object_]+1, N0_n[object_]+1))
			

		iter_object_selected.append(np.argmax(object_results_from_distribution))
		reward = data[sample, np.argmax(object_results_from_distribution)]
		total_score += reward

	return iter_object_selected, total_score