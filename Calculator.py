import re

def main():
    flag = True
    while (flag):
        mathString = input("Print Exit if you want exit from program \nEnter a math expression: ")
        if mathString == "Exit":
            flag = False
        else:
            mathString = simpleFormatter(mathString)
            mathString = "(" + mathString + ")"
            print(ParenthesFormatter(mathString))



def ParenthesFormatter(mathString):
    if mathString.count("(") != 0 and mathString.count(")") != 0:
        Parenthes = re.findall(r'\([+-/*^0-9]+\)', mathString)
        FormatPar = Parenthes
        for index in range(len(Parenthes)):
            mathString = mathString.replace(Parenthes[index], fullMathFormatter(FormatPar[index]))
        return ParenthesFormatter(mathString)
    else:
        return mathString

def fullMathFormatter(mathString):
    mathString = mathString.replace(")", "").replace("(", "")
    mathString = powerExpressionFormat(mathString)
    mathString = multiExpressionsFormat(mathString)
    mathString = additExpressionsFormat(mathString)
    return str(mathString)

def additExpressionsFormat(mathString):
    if mathString.count("-") != 0 or mathString.count("+") != 0:
        additExpr = re.findall(r'\d+(?:\.\d+)?(?:[+-]\d+(?:\.\d+)?)+', mathString)
        for index in range(len(additExpr)):
            mathString = mathString.replace(additExpr[index], additEval(additExpr[index]))
    return mathString

def additEval(mathString):
    mathString = mathString.replace("-", " - ").replace("+", " + ")
    arrayString = mathString.split(" ")
    out = float(arrayString[0])
    for index in range(len(arrayString)):
        if arrayString[index] == "-":
            out -= float(arrayString[index + 1])
        if arrayString[index] == "+":
            out += float(arrayString[index + 1])
    return str(float(out))


def powerExpressionFormat(mathString):
    if mathString.count("^") != 0:
        powExpr = re.findall(r'\d+\^\d+', mathString)
        for el in powExpr:
            mathString = mathString.replace(el, str(int(el.split("^")[0])**int(el.split("^")[-1])))
        return mathString
    return mathString

def multiExpressionsFormat(mathString):
    if mathString.count("*") != 0 or mathString.count("/") != 0:
        multiExpr = re.findall(r'\d+(?:\.\d+)?(?:[*/]\d+(?:\.\d+)?)+', mathString)
        for index in range(len(multiExpr)):
            mathString = mathString.replace(multiExpr[index], multiEval(multiExpr[index]))
    return mathString

def multiEval(mathString):
    mathString = mathString.replace("/", " / ").replace("*", " * ")
    arrayString = mathString.split(" ")
    out = float(arrayString[0])
    for index in range(len(arrayString)):
        if arrayString[index] == "/":
            out /= float(arrayString[index + 1])
        if arrayString[index] == "*":
            out *= float(arrayString[index + 1])
    return str(float(out))



def simpleFormatter(mathString):
    mathString = mathString.replace(" ", "")
    mathString = mathString.replace("++", "+")
    mathString = mathString.replace("--", "-")
    mathString = mathString.replace("//", "/")
    mathString = mathString.replace("**", "*")
    mathString = mathString.replace("^^", "^")
    mathString = mathString.replace(")(", ")*(")
    for el in "0123456789":
        if el + "(" in mathString:
            mathString = mathString.replace(el + "(", el + "*(")
    return mathString



#print(ParenthesFormatter("40 + (30+20) + (30+23+(30+22))"))

main()