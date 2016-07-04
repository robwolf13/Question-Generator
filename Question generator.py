# -*- coding: utf-8 -*-#
___author___='robert woolley'

''' To make; variable control, gui, output control, diagram questions,
loop for multiple questions

Example question formats(seperate ans no)
A+B
[A*B]/B
A + B * C
(A - B) / C
A**3
(seperate ans yes)
q;Ax+Bx a;[A+B]x
q;x**2 - [B*C]x + [B*C] = 0 a;B,C

'''
import math
import random

ops = ["+","-","*","/"]
#Default question format
questionFormat = {
    "name":"",
    "rawFormatQ":"",
    "rawFormatA":"",
    "numberOfQs":0,
    "variableLimits":{"A":[1,10],"B":[1,10],"C":[1,10],"D":[1,10]}
    }
#Main loop that creates a single question and answer from a format
def createQuestionNAnswer(rawFormat):
    #Starting variables
    ques = ""
    ans = ""
    # square bracket means number calculated before displaying it
    inBracket = False
    bracket = ""
    # goes through each part of the str question format creating two str one for the answer and one for the question
    for idx in range(len(rawFormat)):
        m = rawFormat[idx]
        if inBracket == False:
            if m in ops:
                ans = ans + m
                ques = ques + displayOp(m,[rawFormat[idx+1],rawFormat[idx-1]])
            elif m in variables:
                ans = ans + str(variables[m])
                ques = ques + str(variables[m])
            elif m == ' ':
                ques = ques + m
            elif m == '[':
                inBracket = True
            else:
                ans = ans + m
                ques = ques + m
        else:
            if m in ops:
                bracket = bracket + m
            elif m in variables:
                bracket = bracket + str(variables[m])
            elif m == ']':
                bracket = eval(bracket)
                ans = ans + str(bracket)
                ques = ques + str(bracket)
                inBracket = False
                bracket = ""
            else:
                bracket = bracket + m
    return (ques,str(eval(ans)))

#Same as the above but only creates a question or answer
def createQuestionOnly(rawFormat):
    ques = ""
    inBracket = False
    bracket = ""
    for idx in range(len(rawFormat)):
        m = rawFormat[idx]
        if inBracket == False:
            if m in ops:
                ques = ques + displayOp(m,[rawFormat[idx+1],rawFormat[idx-1]])
            elif m in variables:
                ques = ques + str(variables[m])
            elif m == ' ':
                ques = ques + m
            elif m == '[':
                inBracket = True
            else:
                ques = ques + m
        else:
            if m in ops:
                bracket = bracket + m
            elif m in variables:
                bracket = bracket + str(variables[m])
            elif m == ']':
                bracket = eval(bracket)
                ques = ques + str(bracket)
                inBracket = False
                bracket = ""
            else:
                bracket = bracket + m
    return ques

def createAnswerOnly(rawFormat):
    ans = ""
    inBracket = False
    bracket = ""
    for idx in range(len(rawFormat)):
        m = rawFormat[idx]
        if inBracket == False:
            if m in ops:
                ans = ans + m
            elif m in variables:
                ans = ans + str(variables[m])
            elif m == ' ':
                continue
            elif m == '[':
                inBracket = True
            else:
                ans = ans + m
        else:
            if m in ops:
                bracket = bracket + m
            elif m in variables:
                bracket = bracket + str(variables[m])
            elif m == ']':
                bracket = eval(bracket)
                ans = ans + str(bracket)
                inBracket = False
            else:
                bracket = bracket + m
    return ans

#displays things like * and / as their proper symbol
def displayOp(op,next):
    if op == '+':
        return '+'
    elif op == '-':
        return '-'
    elif op == '*':
        if next[0] == '*':
            return ''
        elif next[1] == '*':
            return '^'
        else:
            return '×'
    elif op == '/':
        return '÷'
    else:
        print ("Error in displayOp")

#requests a question format from the user
def requestQuestionFormat():
    global questionFormat
    separateAnswer = input("Separate answer (y/n)")
    if separateAnswer == 'n':
        questionFormat['rawFormatQ'] = input("Question format:")
    elif separateAnswer == 'y':
        questionFormat['rawFormatQ'] = input("Question:")
        questionFormat['rawFormatA'] = input("Answer:")
    questionFormat['numberOfQs'] = input("Number of questions:")
    print (questionFormat)
    run = input ("Run this question (y/n)")
    if run == 'y':
        multipleQuestions(questionFormat['numberOfQs'])
    else:
        requestQuestionFormat()

#rerandomises the variables
def randomiseVariables():
    global variables
    if questionFormat["variableLimits"] == 0:
        varA = random.randint(1,10)
        varB = random.randint(1,10)
        varC = random.randint(1,10)
        varD = random.randint(1,10)
        variables = {"A":varA,"B":varB,"C":varC,"D":varD}
    else:
        variables = {}
        for m in questionFormat["variableLimits"]:
            variables[m] = random.randint(questionFormat["variableLimits"][m][0],questionFormat["variableLimits"][m][1])

#loop that creates multiple questions
def multipleQuestions(n):
    k = 1
    while k <= eval(n):
        k = k + 1
        randomiseVariables()
        listOfQnA=[]
        if questionFormat['rawFormatA'] == '':
            print(createQuestionNAnswer (questionFormat['rawFormatQ']))
        else:
            print (createQuestionOnly(questionFormat['rawFormatQ']))
            print (createAnswerOnly(questionFormat['rawFormatA']))
    print (listOfQnA)

'''randomOrAll = input("Random or all:")'''

requestQuestionFormat()



