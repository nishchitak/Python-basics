##Converting a List into a Tuple
def convertTupleToList(list):
	return(tuple(list))
	

##Simple differences. Note the different parenthesis usage below for initialization. 
sampleList = [1,2,3,4]
sampleTuple = (1,2,3,4)

##Converting a List into a Tuple
list = [1,2,3,4]
print("When a list:")
print(list)
print("When a Tuple:")
print(convertTupleToList(list))

##Dictionary can be used to store a list as a value against a key
sampleDictionary={}
sampleDictionary[1]='one'
sampleDictionary[2]='two'
sampleDictionary[3]=['three','tres','teen','Trois']
sampleDictionary[sampleTuple]='Countdown'  #Tuple can be used as a key since it is immutable
sampleDictionary[3][-1] #This gets Trois 
sampleDictionary.get(3)[-1] #This gets Trois too!
sampleDictionary.get(4,"oops, there's nothing there")  #This return the oops string indicating there is no value for key=4