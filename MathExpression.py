# SUDO CODE FOR THIS PROGRAM
# START
#
# PRINT "Welcome to the Math Expression Evaluator!"
#
# LOOP forever:
#     PROMPT user to enter a math expression (or 'q' to quit)
#     IF input is 'q':
#         EXIT program
#
#     TRY:
#         REMOVE any unsafe characters (optional: sanitize input)
#         EVALUATE the expression using eval() or custom parser
#         DISPLAY the result
#
#     EXCEPT error in evaluation:
#         PRINT "Invalid expression. Please try again."
#
# END LOOP

import sys, math
print("Welcome to the Math Expression Evaluator! ")
while True:
    user_exp = input("Enter your Mathematical Expression or write quit to quit: \n ")
    if user_exp.lower() == 'quit':
        sys.exit()
    elif user_exp == '!,@,#,$,&,':
        print('Please enter a valid Mathematical Expression.\n')
        break
    if "+" in user_exp or "-" in user_exp or "*" in user_exp or "/" in user_exp or "%" in user_exp or "(" in user_exp or ")" in user_exp or "math." in user_exp:
        result = eval(user_exp, {"__builtins__": None}, {"math": math})
        print("Result:", result, "\n")
    else:
        print("Invalid input. Use numbers and math symbols like +, -, *, /, %, or math functions.\n")

