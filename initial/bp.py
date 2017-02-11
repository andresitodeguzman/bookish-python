import os

def determineS(s):
    if s:
        if s > 180:
            return "high"
        elif s < 90:
            return "low"
        else:
            return "normal"
    else:
        return False

def determineD(d):
    if d:
        if d > 180:
            return "high"
        elif d < 90:
            return "low"
        else:
            return "normal"
    else:
        return False

def process(a,b):
    if a:
        if b:
            systole = determineS(int(a))
            diastole = determineD(int(b))
            if systole == "high":
                if diastole == "high":
                    return "Systole and diastole are high"
                elif diastole == "low":
                    return "Systole is high but diastole is low"
                else:
                    return "Systole is high but diastole is normal"
            elif systole == "low":
                if diastole == "high":
                    return "Systole is low but diastole is high"
                elif diastole == "low":
                    return "Systole and diastole are low"
                else:
                    return "Systole is low but diastole is normal"
            else:
                return "You are normal"
        else:
            return "Cannot be empty"
    else:
        return "Cannot  be empty"

c = input("What is your systolic pressure? ")
e = input("What is your diastolic pressure? ")
f = process(c,e)
print(f)
