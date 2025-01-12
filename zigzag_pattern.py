import time, sys
indent = 0
indentIncreasing = True

try:
    while True:
        print(" " * indent, end="")
        print("***********")
        time.sleep(0.2)

        if indentIncreasing == True:
            indent = indent + 1
            if indent == 10:
                indentIncreasing = False    # For changing the direction once it reaches 10 by making it "False"
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True     # For changing the direction once it reaches 0 by making it "True" again
except KeyboardInterrupt:
    sys.exit()