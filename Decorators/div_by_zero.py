def check(func):
	def inside(a,b):
		if b == 0 :
			print("Can't Devide")
			return
		return func(a,b)	
	return inside		


@check
def div(a, b):
	return a/b

#div = check(div)


print(div(4,2))
print(div(4,0))
