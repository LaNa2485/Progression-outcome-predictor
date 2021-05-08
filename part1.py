# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1839526

# Date:  April 13, 2021

print("---------------------------------------------------------------")
pass_credits = int(input("Please enter your credits at pass: "))
defer_credits = int(input("Please enter your credit at defer: "))
fail_credits = int(input("Please enter your credit at fail: "))

totalCredits = pass_credits + defer_credits + fail_credits

if pass_credits == 120:
    print("Progress")
elif pass_credits == 100 and (defer_credits == 20 or fail_credits == 20):
    print("Progress (module trailer)")
elif fail_credits > 60:
    print("Exclude")
else:
    print("Do not progress – module retriever")
print("---------------------------------------------------------------")
