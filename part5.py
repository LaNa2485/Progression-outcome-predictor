# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1839526

# Date:  April 13, 2021

progress_counter = 0
trailer_counter = 0
retriever_counter = 0
excluded_counter = 0

all_credits = [
    [120, 0, 0],
    [100, 20, 0],
    [100, 0, 20],
    [80, 20, 20],
    [60, 40, 20],
    [40, 40, 40],
    [20, 40, 60],
    [20, 20, 80],
    [20, 0, 120],
    [0, 0, 120]
]


def progression_outcome_predictor():
    '''
    last modified : 13/09/2021
    author : naveed
    description : this function counts the progression outcomes
    '''
    global progress_counter
    global trailer_counter
    global retriever_counter
    global excluded_counter

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


def print_histogram():
    '''
    last modified : 13/09/2021
    author : naveed
    description : this function prints out the histogram according to the progression outcomes
    '''
    global progress_counter
    global trailer_counter
    global retriever_counter
    global excluded_counter
    total = progress_counter + trailer_counter + retriever_counter + excluded_counter

    progress_bar = ""
    trailer_bar = ""
    retrieve_bar = ""
    exclude_bar = ""
    for n in range(progress_counter):
        progress_bar = progress_bar + "*"
    for n in range(trailer_counter):
        trailer_bar = trailer_bar + "*"
    for n in range(retriever_counter):
        retrieve_bar = retrieve_bar + "*"
    for n in range(excluded_counter):
        exclude_bar = exclude_bar + "*"

    print(f'\nProgress   {progress_counter}: {progress_bar}')
    print(f'Trailing   {trailer_counter}: {trailer_bar}')
    print(f'Retriever  {retriever_counter}: {retrieve_bar}')
    print(f'Excluded   {excluded_counter}: {exclude_bar}')
    print(f'\n{total} outcomes in total')


for i in all_credits:
    pass_credits = i[0]
    defer_credits = i[1]
    fail_credits = i[2]
    progression_outcome_predictor()

print_histogram()

