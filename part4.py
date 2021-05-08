# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1839526

# Date:  April 13, 2021

progress_counter = 0
trailer_counter = 0
retriever_counter = 0
excluded_counter = 0
done_entering = False


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
            pass_credits = int(input("Enter your total PASS credits: "))
            while pass_credits % 20 != 0 or pass_credits > 120:
                print("Out of range.\nCredit Scores should be in the range 20,40,60,80,100 and 120\nPlease enter a valid credit score.")
                try:
                    pass_credits = int(input("Enter your total PASS credits: "))
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
            defer_credits = int(input("Enter your total DEFER credits: "))
            while defer_credits % 20 != 0 or defer_credits > 120:
                print("Out of range.\nCredit Scores should be in the range 20,40,60,80,100 and 120\nPlease enter a valid credit score.")
                try:
                    defer_credits = int(input("Enter your total DEFER credits: "))
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
            fail_credits = int(input("Enter your total FAIL credits: "))
            while fail_credits % 20 != 0 or fail_credits > 120:
                print("Out of range.\nCredit Scores should be in the range 20,40,60,80,100 and 120\nPlease enter a valid credit score.")
                try:
                    fail_credits = int(input("Enter your total FAIL credits: "))
                except ValueError:
                    print("Integer Required")
        except ValueError:
            print("Integer Required")
    return fail_credits


def get_student_credits():
    '''
    last modified : 13/09/2021
    author : naveed
    description : this function checks the total and counts the students' progression outcomes
    '''
    global progress_counter
    global trailer_counter
    global retriever_counter
    global excluded_counter

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
        progress_counter += 1
    elif pass_credits == 100 and (defer_credits == 20 or fail_credits == 20):
        print("Progress (module trailer)")
        trailer_counter += 1
    elif fail_credits > 60:
        print("Exclude")
        excluded_counter += 1
    else:
        print("Do not progress – module retriever")
        retriever_counter += 1

# Progress 1 | Trailer 0 | Retriever 0 | Exclude 1
# Progress 1 | Trailer 1 | Retriever 1 | Exclude 1
#     *
#                  *
#                               *
#                                            *


def print_vertical_histogram():
    '''
    last modified : 13/09/2021
    author : naveed
    description : this function prints out the vertical histogram according to the progression outcomes
    the vertical histogram is constructed by separating the first three columns using end=''
    the rows are separated by keeping the default ending for the fourth column
    then each row is printed adding a star under the appropiate column or
    replacing by spaces if all the values of that particular column has been added.
    '''
    global progress_counter
    global trailer_counter
    global retriever_counter
    global excluded_counter

    total_count = progress_counter + trailer_counter + retriever_counter + excluded_counter
    count = total_count
    print("---------------------------------------------------------------")
    print(f'Progress {progress_counter} | Trailer {trailer_counter} | Retriever {retriever_counter} | Exclude {excluded_counter}')
    while count > 0:
        for i in range(progress_counter):
            print(f'    *', end='')
            progress_counter -= 1
            break
        else:
            print(f'     ', end='')
        for i in range(trailer_counter):
            print(f'           *', end='')
            trailer_counter -= 1
            break
        else:
            print(f'            ', end='')
        for i in range(retriever_counter):
            print(f'           *', end='')
            retriever_counter -= 1
            break
        else:
            print(f'             ', end='')
        for i in range(excluded_counter):
            print(f'             *')
            excluded_counter -= 1
            break
        else:
            print(f'             ')
        count = progress_counter + trailer_counter + retriever_counter + excluded_counter
    print("---------------------------------------------------------------")
    print(f'\n{total_count} outcomes in total')


get_student_credits()
enter_credits = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()

while not done_entering:
    if enter_credits == "y":
        get_student_credits()
        enter_credits = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
    elif enter_credits == "q":
        print_vertical_histogram()
        done_entering = True
    else:
        print("Invalid Input")
        enter_credits = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
