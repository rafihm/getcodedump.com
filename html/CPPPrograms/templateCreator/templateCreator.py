import sys
import os


def main():
	print "------------------------------------HAHAHAHAHAHAH-------------------------------\nPreset ctrl + D when you done with the input"


	codeHeader =  readInputFromUser("Enter Header for the code:")
	codeHeader =  "\n" +'<p id="codeHeading">' + codeHeader + '</p>' + "\n"
	codeDescription = readInputFromUser("Enter the code Description:")
	codeDescription = '<div><p id="codeDescription">' + codeDescription + '</p></div>' + "\n"
	print "Enter the Name of the File:"
	codeFileName = str(raw_input())
	print "Enter the number of examples:"
	exampleCount = int(raw_input())
	exampleDescription = {}
	exampleCode = {}
	exampleOutput = {}

	if exampleCount > 1:
		for i in range(exampleCount):
			exampleDescription[i] = readInputFromUser("Enter the Example Description for Exampe " + str(i+1))
			exampleDescription[i] = '</br></br><div><p id="codeDescription">' + exampleDescription[i] + '</p></div>' + "\n"

			exampleCode[i] = readInputFromUser("Enter the code for Example" + str(i+1))
			exampleCode[i] = '<pre id="code">' + exampleCode[i] + '</pre>' + "\n"

			exampleOutput[i] = readInputFromUser("Enter the Output for Example" + str(i+1))
			exampleOutput[i] = '<h5>Output:</h5>' + "\n" + '<pre id="output">' + exampleOutput[i] + '</pre>' + "\n"
	else:
		exampleCode[0] = readInputFromUser("Enter the code for Example 1")
		exampleCode[0] = '</br><pre id="code">' + exampleCode[0] + '</pre>' + "\n"

		exampleOutput[0] = readInputFromUser("Enter the Output for Example 1")
		exampleOutput[0] = '<h5>Output:</h5>' + "\n" + '<pre id="output">' + exampleOutput[0] + '</pre></br>' + "\n"


	print "Processing ....................."
	htmlTemplate = readFromFile("templateTopPart.txt") + codeHeader + codeDescription

	if exampleCount > 1:
		for i in range(exampleCount):
			htmlTemplate = htmlTemplate + exampleDescription[i] + exampleCode[i] + readFromFile("templateAdPart.txt") + exampleOutput[i]
	else:
		htmlTemplate = htmlTemplate + exampleCode[0] + readFromFile("templateAdPart.txt") + exampleOutput[0]

	htmlTemplate = htmlTemplate + readFromFile("templateBottomPart.txt")


	writeToFile(codeFileName,htmlTemplate)
	print "_______DONE_________.   ",codeFileName
	#print htmlTemplate








def readFromFile(fileName):
	file1 = open(fileName,"r")
	return file1.read()

def readInputFromUser(question):
	print(question)
	#press CTRL + D to stop the input
	contents = []
	text = ""
	while True:
	    try:
	        line = raw_input()
	    except EOFError:
	        break
	    contents.append(line)
	    text = text + line + "\n"
	return text


def writeToFile(fileName,fileContent):
	fh = open(fileName,"w")
	fh.write(fileContent)
	fh.close()



if __name__ == "__main__":
	while True:
		main()