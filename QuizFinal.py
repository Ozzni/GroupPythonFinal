#Into. to Programming: Python - Final Project code
#Avery, Leila, Josiah
#Quiz Program

#Initialize variables
Score = 0
totalQuestions = 5
Answer = ""
Q = 0
Q1 = "1+1=? \n A: 2 - B: 11 \n C: 1 - D: 3"
Q2 = "1-1=? \n A: 2 - B: 0 \n C: 1 - D: 3"
Q3 = "1*1=? \n A: 2 - B: 11 \n C: 1 - D: 3"
Q4 = "1/1=? \n A: 2 - B: 11 \n C: 3 - D: 1"
Q5 = "1^1=? \n A: 1 - B: 11 \n C: 2 - D: 3"
QuestionList = [Q1, Q2, Q3, Q4, Q5]
QuestionAnswer = ["A", "B", "C", "D", "A"]
Name = input("What is your name? ")


#Introduces the quiz
print("Math Quiz - 5 questions")
print()

#question loop
while Q < totalQuestions:
   
    #prints the current question from list, gets answer
    print(QuestionList[Q])
    Answer = input("A, B, C, or D? ")
    
    #validating input #TODO: this currently only accepts A as valid. Make this pass by if ANY of A B C or D are the given answer.
    while Answer != "A" and "B" and "C" and "D":
        Answer = input("Invalid answer. Please type A, B, C, or D ")
    
    #check if answer is correct and assign points accordingly
    if Answer == QuestionAnswer[Q]:
        print("Correct answer! ")
        Score = Score + 1
    else:
        print("Incorrect answer. ")
    
    #Iterate on the loop
    Q = Q + 1


#print final results
print("Hello,", Name, "your score is:", Score, "/", totalQuestions, "!")