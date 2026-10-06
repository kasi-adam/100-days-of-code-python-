name = input ("Full Name: ")
Age = int(input ("Age: " ))
prog_exp = float(input("How many years of programming?:"))
prog_lang = input("Programming languages you know separated by comma:")
GitHub= input("Do you have a gitHub account?")
Prg_project = input("Have you completed a programming project?")

print("=====CANDIDATE SCREENING SYSTEM=====")
print("Name: ",name)
print("Age: ",Age)

languages = []
prog_lang = prog_lang.split(',')
print("Programming Languages:")
for lang in prog_lang:
    languages.append(lang.strip())
    print("-",lang.strip())

eligible = Age>=18 and prog_exp>=1 and GitHub=="yes" and Prg_project=="yes"
if eligible:
    print ("Eligibility: Eligible")
elif Age < 18:
    print("Eligibility: Not Eligible - You must be 18 or older.")
else:
    print("Eligibility: Not Eligible")

score = 0
if Age>=18:
    score+=10
if prog_exp>=1:
    score+=20
if GitHub=="yes":
    score+=20
if Prg_project=="yes":
    score+=30
for lang in languages:
    score+=5
print("Candidate score:", score)

if not eligible:
    print("Recommendation: Not Recommended")
elif score >= 80:
    print("Recommendation: Strong Candidate")
elif score >= 60:
    print("Recommendation: Potential Candidate")
elif score >= 40:
    print("Recommendation: Needs More Experience")
else:
    print("Recommendation: Not Recommended")