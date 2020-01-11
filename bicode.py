from tkinter import *
import re
root = Tk()
root.title('Binary Counter')
root.geometry('500x500')
logo = PhotoImage(file="JackHawk9000.png")

b = StringVar()  #stores user input as String
"""
	ValidateInput:
	ensures that the user input string does not contain 
	special chars / regular characters (only numbers)

	then ensures the user input contains only 1 or 0 (binary) values
	if checks pass, calls binaryToNumber() function passing the 
	clean user input as it's argument
"""
def validateInput():
	error = False
	binaryInput = b.get()
	# Regex expression to find any chars / special chars in string
	isNotNumber = bool(re.search(r'\D', binaryInput))
	# if chars found error flag set to true, display error message
	if isNotNumber == True:
		error = True
	# if no chars found, ensure the digits are only 1's or 0's (binary)
	else:
		for num in binaryInput:
			num = int(num)
			if num != 0 and num != 1:
				error = True
			else:
				error = False
		
	if error == True:
		lab12 = Label(text="Invalid, Please input binary digits only", font=20, fg="Red").pack()
	# if no errors found, convert user input string to integer and sends to 
	# binary calculator.
	else:
		binaryInput = int(binaryInput)
		binaryToNumber(binaryInput)

"""
	binaryToNumber:
	@param num (the user input binary integer)

	function calculates the standard number received from binary input
"""
def binaryToNumber(num):
	decValue = 0
	base = 1
	temp = num
	
	while(temp):
		lastDig = temp % 10
		temp = int(temp / 10)
		decValue += lastDig * base
		base = base * 2
	valueToString = str(decValue)
	lab12= Label(text=decValue, font=20).pack()

# JackHawk9000 Logo
label2 = Label(root, image=logo).pack() 

labl1 = Label(root, text='Torrence is a flaming Douche', font=30).pack(pady=10)
# user input field
text = Entry(root, textvariable=b).pack() 
# submit button
button1 = Button(root, text='Submit', command=validateInput).pack(pady=10) 

root.mainloop()