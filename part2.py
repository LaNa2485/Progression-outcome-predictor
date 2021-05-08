# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1839526

# Date:  April 13, 2021


def get_pass_credits():
    '''
    last modified : 13/09/2021
    author : naveed
    return : pass_credits
    description : this funtion takes the user input making sure it's in the range 20,40,60,80,100 and 120.
    '''
    pass_credits = 1
    while pass_credits % 20 != 0:
        try:
            pass_credits = int(input("Please enter your credits at pass: "))
            while pass_credits % 20 != 0 or pass_credits > 120:
                print("Out of range.\nCredit Scores should be in the range 20,40,60,80,100 and 120\nPlease enter a valid credit score.")
                try:
                    pass_credits = int(input("Please enter your credits at pass: "))
                except ValueError:
                    print("Integer Required")
        except ValueError:
            print("Integer Required")
    return pass_credits


def get_defer_credits():
    '''
    last modified : 13/09/2021
    author : naveed
    return : defer_credits
    description : this funtion takes the user input making sure it's in the range 20,40,60,80,100 and 120.
    '''
    defer_credits = 1
    while defer_credits % 20 != 0:
        try:
            defer_credits = int(input("Please enter your credit at defer: "))
            while defer_credits % 20 != 0 or defer_credits > 120:
                print("Out of range.\nCredit Scores should be in the range 20,40,60,80,100 and 120\nPlease enter a valid credit score.")
                try:
                    defer_credits = int(input("Please enter your credit at defer: "))
                except ValueError:
                    print("Integer Required")
        except ValueError:
            print("Integer Required")
    return defer_credits


def get_fail_credits():
    '''
    last modified : 13/09/2021
    author : naveed
    return : fail_credits
    description : this funtion takes the user input making sure it's in the range 20,40,60,80,100 and 120.
    '''
    fail_credits = 1
    while fail_credits % 20 != 0:
        try:
            fail_credits = int(input("Please enter your credit at fail: "))
            while fail_credits % 20 != 0 or fail_credits > 120:
                print("Out of range.\nCredit Scores should be in the range 20,40,60,80,100 and 120\nPlease enter a valid credit score.")
                try:
                    fail_credits = int(input("Please enter your credit at fail: "))
                except ValueError:
                    print("Integer Required")
        except ValueError:
            print("Integer Required")
    return fail_credits

print("---------------------------------------------------------------")
pass_credits = get_pass_credits()
defer_credits = get_defer_credits()
fail_credits = get_fail_credits()

total_credits = pass_credits + defer_credits + fail_credits

while total_credits != 120:
    print("Total Incorrect \nInvalid Total number of credits entered\nPlease enter all 120 credits.")
    pass_credits = get_pass_credits()
    defer_credits = get_defer_credits()
    fail_credits = get_fail_credits()

    total_credits = pass_credits + defer_credits + fail_credits

if pass_credits == 120:
    print("Progress")
elif pass_credits == 100 and (defer_credits == 20 or fail_credits == 20):
    print("Progress (module trailer)")
elif fail_credits > 60:
    print("Exclude")
else:
    print("Do not progress – module retriever")
print("---------------------------------------------------------------")
