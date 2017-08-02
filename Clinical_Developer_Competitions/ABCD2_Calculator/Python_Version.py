'''
Basic ABCD2 Score calculator - this was my original attempt at Python version of it - very roughly hashed out
'''

print('This is the basic ABCD2 Score calculator. It will take in the age, systolic blood pressure, diastolic blood pressure, basic clinical features, duration and diabetic status and return the abcd2 score')

def age_score(age):
    if age >= 60:
        return 1
    else:
        return 0
        
def blood_pressure(systolic, diastolic):
    if systolic >= 140 or diastolic >= 90:
        return 1
    else:
        return 0

def clinical_score(unilat_weakness, speech_dist):
    if unilat_weakness == True:
        return 2
    elif speech_dist == True:
        return 1
    else:
        return 0
        
def duration(duration_of_symptoms):
    if duration_of_symptoms >= 60:
        return 2
    elif duration_of_symptoms >= 10:
        return 1
    else:
        return 0
        
def diabetes(diabetic):
    if diabetic == True:
        return 1
    else:
        return 0

print('Please input the age of the patient:')
a = int(input('>'))
print('Please input the systolic blood pressure in mmHg')
b = int(input('>'))
print('Please input the diastolic blood pressure in mmHg')
c = int(input('>'))
print('Did the patient have unilateral weakness?')
d = bool(input('> True/False'))
print('Did the patient have speech disturbance?')
e = bool(input('> True/False'))
print('How long did the symptoms last? (in minutes)')
f = int(input('>'))
print('Is the patient diabetic?')
g = bool(input('> True/False'))

pt_age = age_score(a)
pt_bp = blood_pressure(b,c)
pt_clinical = clinical_score(d,e)
pt_duration = duration(f)
pt_diabetic = diabetes(g)

ABCD2_score = pt_age+pt_bp+pt_clinical+pt_duration+pt_diabetic

print('The ABCD2 score is:')
print(ABCD2_score)
