import time

def time_it(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(func.__name__ + " took " + str((end-start)*1000) + " mil secs")
		return result
	return wrapper

@time_it
def cal_queb(numbers):
	result = []
	for num in numbers:
		result.append(num*num)
	return result

#@time_it
def cal_squre(numbers):
	result = []
	for num in numbers:
		result.append(num*num*num)
	return result	

# This is same as @time_it
cal_queb = time_it(cal_queb)

array = range(1,1000000)
cal_squre(array)
cal_queb(array)
