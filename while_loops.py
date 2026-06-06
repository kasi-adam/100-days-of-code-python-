all_scores=[]
all_passes=[]
all_failures=[]

scores=input("Enter the students scores or type 'done'\n ")
while True:
   if scores=='done':
      break
   scores_list=scores.split()
   for i in range(len(scores_list)):
      scores_list[i] = int(scores_list[i])

   all_scores.extend(scores_list)
   scores=input("Enter the students scores or type 'done'\n ")

if len(all_scores) == 0:
    print("No scores entered")
    exit()

total_score=sum(all_scores)
passes=0
fails=0

Highest_score=max(all_scores)
lowest_score=min(all_scores)
Average_score=total_score/len(all_scores)
Average_score=round(Average_score,2)

for score in all_scores:

   if score >=50:
      all_passes.append(score)
      passes+=1
   else:
      all_failures.append(score)
      fails+=1
print("Here are the scores you entered:",all_scores)
print("The number of passes are:",passes)
print("The number of failures are:",fails)
print("the average score is:",Average_score)
print("The highest score is:",Highest_score)
print("The lowest score is:",lowest_score)






