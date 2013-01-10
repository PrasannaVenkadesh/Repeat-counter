#!/usr/bin/python

#A Program to get input as a list and display the number of times the words occured in the list along with the word, regardless of case. Filter out and remove punctions.

import re
import string

#main module starts here
def main():	

	#Input Part starts here

	number_of_words = input("Enter number of words: ")
	list_data = []
	print "Enter the words 1 per line by pressing Enter after each word"
	for i in range(0,number_of_words):
		list_data.append(raw_input("Enter Word: "))

	#Input part Ends here & Processing starts here

	converted_string = " ".join(list_data)	
	converted_string = converted_string.lower()
	for c in string.punctuation:
		converted_string = converted_string.replace(c,"")

	relisted_data = converted_string.split()

	dict_data = {};
	for item in relisted_data:
		if dict_data.has_key(item):
			dict_data[item] = dict_data[item] + 1
		else:
			dict_data[item] = 1

	#Processing Ends here and Output starts below

	for i in dict_data:
		print i, dict_data[i]

	#Output Ends here
#main module ends here

if __name__ == "__main__":
	main() #Calling main module