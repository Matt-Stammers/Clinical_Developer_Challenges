'''
Basic ABCD2 Score calculator
'''

print('This is the basic ABCD2 Score calculator')

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

def clinical_score(speech_dist, unilat_weakness):
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

while True:
  try:
    a = int(input('>'))
    print()
    print(age_score(a))
    b = int(input('>'))
  except ValueError:
    print('Please input a number:')
    
while True:
  try:
    a = int(input('>'))
    print()
    print(age_score(a))
    b = int(input('>'))
  except ValueError:
    print('Please input a number:')
    
