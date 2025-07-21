"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""

questions_file = open('questions.txt','r')

questions_list = [line.strip() for line in questions_file]
questions_file.close()

score = 0
total = len(questions_list) # set total score

for line in questions_list:
    # split equation with '=' into question and answer
    q, a = line.split('=')

    # print question and wait for user to input their answer
    answer = input(f"{q}=")

    if a == answer: # if user input matches answer
        score += 1 # increase score

result = open('result.txt','w')
result.write(f"Your final score is {score}/{total}.")
result.close()
