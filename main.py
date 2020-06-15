import array


# def print_keywords_appearances(filename,keywords):
    #"""define a function that would print how many times we find apperances of the keywords"""

    # initializing value of 0 for an integer count_lines, count_lines will be the number of lines inside the file
    # count_lines = 0
    # create an empty array that will become the nested list name array_to_check
    # array_to_check = []
    # make the nested list that contains same amount of arrays as the numbers have
    # for index in range(len(keywords)):
        # array_to_check.append([])
    # print(len(keywords))
    # open a file with the input filename, and read this file
    # with open(filename, "r") as f:
        # read each line inside the file
        # for line in f:
            # for each line we read in file, we can increase count_lines by 1
            # count_lines += 1
            # for each word we find in each line, we compare that word with the keyword(ex: password in this
            # circumstances)
            # for word in line.split():
                # if we find a word that exactly matches with keyword, we can add count_lines into array_to_check
                # that represents which line we find the word
                # for index in range (len(keywords)):
                    # if word == keywords[index]:
                        # array_to_check[index].append(count_lines)
                    # print(len(array_to_check[index]),"appearances of",keywords[index])


def read_and_find(filename, keywords_list):
    """define a function that would input filename and password, and would return an array"""

    # initializing value of 0 for an integer count_lines, count_lines will be the number of lines inside the file
    count_lines = 0
    # create an empty array that will become the nested list name array_to_check
    array_to_check = []
    # make the nested list that contains same amount of arrays as the numbers have
    for index in range(len(keywords_list)):
        array_to_check.append([])
    # print(len(keywords))
    # open a file with the input filename, and read this file
    with open(filename, "r") as f:
        # read each line inside the file
        for line in f:
            # for each line we read in file, we can increase count_lines by 1
            count_lines += 1
            # for each word we find in each line, we compare that word with the keyword(ex: password in this
            # circumstances)
            for word in line.split():
                # if we find a word that exactly matches with keyword, we can add count_lines into array_to_check
                # that represents which line we find the word
                for index in range (len(keywords_list)):
                    if word == keywords_list[index]:
                        array_to_check[index].append(count_lines)
        # output how many lines we find in the file, and how many times the keyword appear
        print("Checked total", count_lines, " lines, and we find")
        for index in range(len(keywords_list)):
            print(len(array_to_check[index]), "appearances of", keywords_list[index])
        # print(array_to_check)
    # if the file fail to open
    # except:
        # tell the user that the filename he/she entered was wrong
        # print("Failed to open file. Please start again.\n")
    # after the loop is done, return array_to_check
    # print(array_to_check)
    return array_to_check


def calculate_times_a_number_in_array(array_to_check, keywords_list):
    """define a function calculate_times_a_number_in_array with input of array_to_check"""

    # use set() for array_to_check to get the numbers that showed in array to check
    for index in range(len(array_to_check)):
        array_to_evaluate = set(array_to_check[index])
    # array_to_evaluate2 = set(array_to_check2)
        # set two different variables that show values in array_to_check and array_to_evaluate
        for variables_array_to_evaluate in array_to_evaluate:
            # print("variables in array_to_check", variables_array_to_evaluate,"first loop")
            # set an integer count initializing value of 0
            count = 0
            for variables_array_to_check in array_to_check[index]:
                # print("variables in array_to_evaluate",variables_array_to_check,"second loop")
                # compare each variables in array_to_check and array_to_evaluate
                if variables_array_to_evaluate == variables_array_to_check:
                    # if there is a number that shows multiple times, we increase the count
                    count += 1
            # print("line", variables_array_to_evaluate, ":", count, repr(keywords_list[index]))
            print("line", variables_array_to_evaluate, ":", count, '"{}"'.format(keywords_list[index]))

     # for variables_array_to_evaluate2 in array_to_evaluate2:
         # count = 0
        # for variables_array_to_check2 in array_to_check2:
            # if variables_array_to_evaluate2 ==  variables_array_to_check2:
                # count += 1
        # print("Line", variables_array_to_evaluate2, ":", count)



# def run_multiple_times():
    # """define a function run_multiple_times"""

    # set a string answer that will be the condition for the loop
    # answer = 'y'
    # create a while loop that will let user try as many times as he/she wants
    # while (answer == 'y' or answer == 'Y'):
        # ask user to input filename
        # filename = input("Please enter the file name of the file you want to open: ")
        # ask user to input keyword
        # keyword = input("Please enter the keyword that you want to find in the file: ")
        # we create an empty array name array_to_check, and store the return values of function array_to_check into it
        # array_to_check = read_and_find(filename, keyword)
        # calculate_times_a_number_in_array(array_to_check)
        # answer = input("Enter 'Y' or 'y' for yes if you want to try again.\n"
                       # "All other inputs will consider as no.\n"
                       # "Do you want to try again?\n")
        # print(answer)


def main():
    """define the main function"""

    # we create an empty array name array_to_check, and store the return values of function array_to_check into it
    #
    # array_to_check =
    # print_keywords_appearances("testfile.txt",["password","file","this"])
    array_to_check = read_and_find("testfile.txt",['password','file','this'])
    # print(array_to_check)
    # read_and_find("testfile.txt","password","file")
    # use function calculate_times_a_number_in_array with input array_to_check to find the output of what we want
    # in which line we find the keyword, and how many times this keyword appeared
    calculate_times_a_number_in_array(array_to_check, ['password','file','this'])
    # do the steps above again,but this time we will enter a different keyword to process the program
    # array_to_check = read_and_find("testfile.txt", "file")
    # calculate_times_a_number_in_array(read_and_find("testfile.txt", "password", "file"))
    # input("Enter your input:")
    # print(input)
    # run_multiple_times()


if __name__ == "__main__":
    main()
