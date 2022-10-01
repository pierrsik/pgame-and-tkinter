from tkinter import *
from tkinter import messagebox as mb
import json

root = Tk()
root.geometry("800x450")
root.title("HACK O HOLICS QUIZZ")

with open("data.json") as f:
	data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])


title = Label(root, text="HACK O HOLICS QUIZZ",width=50, font=("ariel", 20, "bold"))
title.place(x=-100, y=30)

class Quiz:
	def __init__(self):
		self.questionNumber=0
		self.displayQuestion()
		self.selectedOption=IntVar()
		self.opts=self.radioButtons()
		self.displayOptions()
		self.buttons()
		self.dataSize=len(question)
		self.correct=0

quiz = Quiz()
root.mainloop()


def displayResults(self):
		wrongCounter = self.dataSize - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrongCounter}"

		score = int(self.correct / self.dataSize * 100)
		result = f"Score: {score}%"

		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

def checkAnswer(self, questionNumber):
    if self.selectedOption.get() == answer[questionNumber]:
        return True


def nextButton(self):
		if self.checkAnswer(self.questionNumber):
			self.correct += 1
		self.questionNumber += 1
		if self.questionNumber==self.dataSize:
			self.displayResults()
			root.destroy()
		else:
			self.displayQuestion()
			self.displayOptions()
def buttons(self):
    next_button = Button(root, text="Next",command=self.nextButton,
    width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
    next_button.place(x=350,y=380)

def displayOptions(self):
		val=0
		self.selectedOption.set(0)
		for option in options[self.questionNumber]:
			self.opts[val]['text']=option
			val+=1
	# This method shows the current Question on the screen
def displayQuestion(self):
    questionNumber = Label(root, text=question[self.questionNumber], width=60,font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
    questionNumber.place(x=70, y=100)

def radioButtons(self):
    q_list = []
    y_pos = 150
    while len(q_list) < 4:
        radio_btn = Radiobutton(root,text=" ",variable=self.selectedOption,
        value = len(q_list)+1,font = ("ariel",14))
        q_list.append(radio_btn)
        radio_btn.place(x = 100, y = y_pos)
        y_pos += 40
        return q_list


