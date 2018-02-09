
#--------------------------  Writing a python file -------------------------
	
	#Writing python files is easy, simply download sublime text 3
	#Install the program and open it
	#click file -> new file in the top left hand corner
	#then save the file . File -> save as...
	#save the file with the file extension .py


#-------------------  insuring you have python installed on MAC -------------------------

	#the easiest way to run python files using using the command line provided to you on your computer
	#before you run a python file you need to make sure your computer knows what python is.
	#open the 'terminal' application by going in to your applications and clicking the 'Other' applications, then click 'terminal'
	#This will open a command line (also called terminal window)
	#To check if python is installed or not type ' python -v ' into the terminal window
	#If it prints out a whole bunch of stuff with the last thing it prints being a >>> then python is installed - hoorah!
	#if not youre going to need to download and install python from here:  https://www.python.org/downloads/
	#once you have installed python open the terminal window again and type python -v into the terminal window
	#it should now be installed

#-------------------  Navigating the command line -------------------------

	#Because youre running a file in the command line, its necessary for you to be able to find that file from the command line
	#To do this were gonna have to have to know two commands:
	#       ->cd
	#       ->ls
	#cd means call directory, its used to open folders. for instance if i wanted to open the folder 'Desktop', I would write cd Desktop
	#im not positive what ls stands for, I like to think 'List stuff', typing ls and pressing enter will print out the names of all the files and folders in your current folder
	#To run a python file you need to know where its is saved on your MAC. For instance this file is saved in ConorHeff/Desktop/College/Python/Amy
	#when you open the terminal window it will open by default at the home directory i.e ConorHeff.
	#To navigate to ConorHeff/Desktop/College/Python/Amy I will have to do a bunch of cd operations.
	#I could go cd Desktop/College/Python/Amy to get there in one step but its more likely youll go one by one:
	#cd Dektop
	#cd College
	#cd Python
	#cd Amy
	#Be aware the terminal is case sensitive so if i have a folder called conor and i try to cd CONor it wont work
	#at any stage if you want to see the files in the folder youre in just type ls


#-------------------  Running a python file -------------------------

	#Once you have established that python is installed and have navigated to the correct folder where the python file is located in the command line
	#the next step is to run the file, to do this were gonna use the python command
	#if I wanted to run the file 'Conor.py', when in the correct folder, you can just type ' python ./Conor.py ' and you will see it execute
	#And thats it! - good to go :) 







#-------------------  The actual code -------------------------
#-------------------  The actual code -------------------------
#-------------------  The actual code -------------------------

	#for the purpose of demonstration I will write all the code im writing as seperate functions, so that i can call and demonstrate the code independantly,
	#It is however not necessary (even bad practice) to write your code as a series of functions unless you intend on reusing this code multiple times.
	#I will explain further down how to write functions, so dont get hung up on reading the functions now
print("\nWelcome!!\n")
def welcome():
	print("\nTo run any of the topics discussed in the python file type:\n\t->variables\n\t->if\n\t->loops\n\t->functions\nor type 'quit' to exit\n")


welcome();
#-------------------  Variables and printing -------------------------
def introToVariables():
	print("\n\n----------------- Variables ----------------------\n")
	#The simplest thing you can do in programming is probably make a variable and print it out
	#variables in code are different from variables in maths
	#a maths variable represents and unknown value which you may or may not be able to deduce a value for
	#a variable in coding represents a known value which you typically want to reuse and associate with an englishy meaning
	#for instance if im writing a calender programme, the value 365 would be useful to store and reuse multiple times
	#I might make a variable called numberOfDaysInTheYear = 365, now whenever i want to refer to number of days of the year i can use the variable
	#numberOfDaysInTheYear.This makes the code more interpretable to someone who hasnt written it and allows us to update our code more
	#easily. Imagine tomorrow the number of days in the year change. If my calender programme is 1000000 lines long, its a pain in the neck
	#to update every 365 ive written one by one. Its much easier to change the value associated with a variable. 
	#Basically variables are handy :) 

	#simple variables are : integers, decimals, booleans (True or False), characters (letters) and strings(words)
	#these are called primitive data types (not important just the terminalogy)
	#to make a variable, you use the following syntax:

	myFirstVariable = True

	#This makes a variable with the name myFirstVariable and the boolean value True. Note True and False need to be spelt with a 
	#capital letter.
	#To print out any variable use print(). Specify what variable you want to print out by including the variable name inside the brackets;
	#e.g print(myFirstVariable). lets make some variables and print them out.

	#make a bunch of variables
	age = 20;                       #This is an integer variable
	name = "Conor"                  #This is a string variable
	height  = 175.4                 #This is a decimal variable
	sex = 'M'                       #This is a character variable

	#printing out the variables
	print("\n\nPrinting out simple variables..")
	print (name)
	print (age)
	print (height)
	print (sex)

	#printing out the variables with a string
	print("\n\nPrinting out variables with a string..")
	print ("name : "+name)
	print ("age : " +str(age))
	print ("height : " +str(height))
	print ("sex : "+ sex)
	#note if I want to print out numbers with a string, I have to convert the number to a string using str()

	#combining variables in a print statement
	print("\n\nPrinting out a string with a number of variables...")
	print("Hi my name is "+name+". I am "+str(age)+" years old and I am "+str(height)+"cm tall")

	print("\n\n----------------- Variables ----------------------\n")


def ifElseStatements():
	print("\n\n-----------------if / Else----------------------\n")
	#if else statements are used to control when code is run. for instance when a person logs into black board if they are a student
	#you might want to show them a student version of the website. If the person is a lecturer you might want to show them a lecturer 
	#version of the website. 
	#in english youd want to say something like this:
	#   if the person is a lecturer -> load lecturer version of website
	#   else if they are not a lecturer -> load the student version of the website
	#in code this might look like

	print("\n\nExecuting an if else code block.....")
	lecturer = True
	if(lecturer == True):
		print("Loading lecturer version of website...")
	else:
		print("Loading the student version version of the website...")

	#if else statements are usually used to check the value of a variable that we know can onluy be a set few values.
	#e.g if you have a variable that can be set to either 1,2 or 3 and you want something different to happen depending on whether the 
	#value is 1,2 or 3 you would use an if,elif else statement e.g
	print("\n\nExecuting an if/ elif / else code block.....")
	variableValue = 2
	if(variableValue==1):
		print("The value is 1")
	elif(variableValue==2):
		print("The value is 2")
	else:
		print("The value is 3")

	print("\n\n-----------------if / Else----------------------\n")

def loopsIntro():
	print("\n\n-----------------Loops----------------------\n")
	#loops are very handy peices of code. They are used to repeat a piece of code a number of times 
	#for instance if i want to get a computer to guess random strings of words and letters until it cracks your password I would put that 
	#piece of code inside of a loop.
	#There are two kinds of loops, for loops and while loops. Technically these are equivalent, you can always use a while loop instead of a for loop
	#and a for loop instead of a while loop. For loops are used to iterate over lists. Their execution is bounded i.e will iterate as many
	#times as there are elements in a list where as while loops are conditional i.e they will run until a certain codition becomes true
	#it may be the case that the condition will never become true, in which case the loop will run infinitely and you have bojangled your code

	#arrays: 
	#arrays are simply a list of values. They must be all of the same data type e.g all integers or all strings
	#the values of an array can be accessed in a loop or independently 

	family = ["marie","fearghal","conor","kate","james"]		#an array of strings

	print("\nAccessing array elements in a for loop")
	for familyMember in family:									#this is the structure of a for loop, it will execute
		print(familyMember)										#as many times as there are elements 

	print("\nAccessing array elements independently:\n"+family[0])
	print(family[2])

	
	print("\nAccessing array elements in a while loop:")
	counter = 0;
	while(counter < len(family)):									#this is the structure of a while loop, it will execute
		print(family[counter])										#until counter is = to the number of elements in the array
		counter= counter+1							


	print("\n\n-----------------Loops----------------------\n")

def functionsIntro():
	print("\n\n-----------------functions----------------------\n")
	#functions are a way in computer programming of reusing code so that we dont have to type it out again. Typically you will
	#write a function either to break up a problem into sub problems or if we are carrying out a particular task at various stages
	#of a program, we will write a function to encapsulate this task so that we dont end up writing the same code a bunch of times.

	#e.g
	#for instance imagine you were writing a piece of code to sort 5 lists of numbers that you were receiving at different random times
	#you could write a piece of code that would sort the first list and then a very similar piece of code to sort the second list, then
	#when you recieve the third list again you will write a very similar piece of code to sort this and so on. You will end up writing
	#virtually the same bit of code 5 times, this makes your code look really long and messy, it is better if you can just write a function
	#called sort() so that every time you get a list, you can sort it by just calling sort() on your list.

	#the syntax of the function declaration is how you see above def functionsIntro():
	#def stands for define. we are defining a function called functionsIntro
	#the brackets are for a list of arguments, we didnt include any here, but functions in general are able to accept values which they can operate on
	#the colon means "everything under this colon, indented by one tab is part of this function"
	#TAB SPACING IS VERY IMPORTANT IN PYTHON!!
	#you can relate functions in coding to functions in maths f(x) is a function that accepts a value and has an output
	#coding functions can accept more than one input and will usually have an output (though they dont have to)
	#lets look at some functions:

	print("\n\nPrinting f(x)")						#just to make the output look nice. otherwise unimportant
	print(f(3))
	#this is a call to the f(x) function below. To call or invoke a function you write the function name followed by brackets
	#e.g functionName()
	#if the function is expecting arguments or inputs you include these inside the brackets 
	#e.g functionName(argument1, argument2)
	#if a function returns an output you need to save it in a variable, you do this by assigning the function call to a variable
	#e.g storedValue = functionName(argument1,argument2)
	#in this example, the result returned by the value is saved in the variable storedValue
	

	#Calling the print function written below
	unorderedArray = [45,2,34,69,20,1070,16,13,1,8]
	print("\n\nPrinting unordered array...")
	printArray(unorderedArray)
	


	#Calling the sort function, saving the output of that function and printing it by calling the printArray function written below
	print("\n\nPrinting ordered array...")
	orderArray = sortArray(unorderedArray)
	printArray(orderArray)

	#Calling the introduce function
	print("\n\nCalling the introduce function...")
	print("Why dont you introduce yourself to us?")
	introduce("Conor",20,"Trinity College")

	print("\n\n-----------------functions----------------------\n")

#this is a function which calcultes the value of x^3 - 3x^2 + 7x +11
#in programming we call the x in f(x) an argument/parameter or input, they all mean the same thing
#similar to a function in maths where f(x) returns a value called 'y' e.g f(x) = y. This function also returns a value
def f(x):
	return (x*x*x)-(3*x*x)+(7*x)+11

#this is a function which loops through and prints out the elements of an array which you pass into it. Note that it does not return anything
#a function which does not return anything is said to be a void function and they're totally okay
def printArray(array):
	stringOfArray = ""
	for element in array:
		stringOfArray = stringOfArray+str(element)+","
	print(stringOfArray)

#This is a function which takes in an array and sorts it in ascending order. It is unimportant to understand the functionality
#of this function, just to see that functions can take in complex information, such as an array, carry our a complex function
#and also return a complex piece of data (again in this case an array). This function is a simple bubbleSort function, a well
#known sorting algorithm, if you are interested in how it works, you can see it explained better here : https://www.youtube.com/watch?v=6Gv8vg0kcHc
def sortArray(array):
	temp = array[0];
	index=0;
	isSorted = False;

	while(index< len(array) ):
		comparatorIndex = 1;
		while (comparatorIndex < len(array)-index):
			if(array[comparatorIndex-1] > array[comparatorIndex]):
				temp = array[comparatorIndex-1];
				array[comparatorIndex-1] = array[comparatorIndex]
				array[comparatorIndex] = temp
			comparatorIndex = comparatorIndex+1
		index = index+1	
	return array

#Here is another function, not really note worthy, just to demonstrate that you can pass in more than one argument to a function
def introduce(name, age, college):
	print("Hey my name is "+name+" I am "+str(age) +" years old. I study at "+college+"\n\n")






















#Simply how the programme runs, you can ignore!!


takingInput = True

while(takingInput==True):
	answer = raw_input("What topic would you like to run?\n")
	if(str.lower(answer)=="variable" or str.lower(answer)=="variables"):
		introToVariables();
		print("\n")
	elif(str.lower(answer)=="if" or str.lower(answer)=="ifElse"):
		ifElseStatements();
		print("\n")
	elif(str.lower(answer)=="loop" or str.lower(answer)=="loops" or str.lower(answer)=="for" or str.lower(answer)=="while"):
		loopsIntro();
		print("\n")
	elif(str.lower(answer) == "function" or str.lower(answer) == "functions" or str.lower(answer) == "f(x)"):
		functionsIntro();
		print("\n")
	elif(str.lower(answer) =="quit" or str.lower(answer) == "exit"):
		takingInput=False;
		print("Okay, goodbye :) ")
	else:
		print("------------------------------------------------\n")
		print("Error, this is not a valid topic.\n")
		print("------------------------------------------------")
		welcome()

def welcome():
	print("To run any of the topics discussed in the python file type:\n\t->variables\n\t->if\n\t->loops\n\tfunctions\n\n or type 'quit' to exit")






