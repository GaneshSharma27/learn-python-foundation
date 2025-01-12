import pyinputplus as pyip
import time, random

number_of_question = 10
correct_answer = 0
for question_number in range(number_of_question):
    number_1 = random.randint(0, 9)
    number_2 = random.randint(0, 9)

    prompt = "#%s: %s * %s = " %(question_number, number_1, number_2)
    prompt = f"{question_number}: {number_1} * {number_2}"

    try:
        # right answers are handled by allowRegexes
        # wrong answers are handled by blockRegexes, with a custom message
        pyip.inputStr(prompt, allowRegexes=["^%s$" %(number_1 * number_2)], blockRegexes=[(".*", "Incorrect!")], timeout=8, limit=3)
    except pyip.TimeoutException:
        print("Out of time!")
    except pyip.RetryLimitException:
        print("Out of tries!")
    else:
        # this block runs if no exceptions were raised in the try block
        print("Correct!")
        correct_answer += 1
    time.sleep(1)           # brief pause to let user see the result

print("Score: %s/%s" %(correct_answer, number_of_question))