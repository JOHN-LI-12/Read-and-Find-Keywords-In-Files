#import array
import array

def calculate_times_a_number_in_array(array_to_check):
    """define a function calculate_times_a_number_in_array with input of array_to_check"""

    # use set() for array_to_check to get the numbers that showed in array to check
    array_to_evaluate=set(array_to_check)
    print("array_to_evaluate.",array_to_evaluate)

    # set two different variables that show values in array_to_check and array_to_evaluate
    for variables_array_to_evaluate in array_to_evaluate:
        # print("variables in array_to_check", variables_array_to_evaluate,"first loop")
        # set an integer count initializing value of 0
        count=0
        for variables_array_to_check in array_to_check:
            # print("variables in array_to_evaluate",variables_array_to_check,"second loop")
            # compare each variables in array_to_check and array_to_evaluate
            if variables_array_to_evaluate == variables_array_to_check:
                    # if there is a same number that shows more than 1 time, count increases by 1
                count+=1
        print("line", variables_array_to_evaluate, count)
                # print("the count is", count)

# use function calculate_times_a_number_in_array
# calculate_times_a_number_in_array([2,2,4])

matrix = []
for i in range(5):
    matrix.append([])

    for j in range(5):
        matrix[i].append(j)

print(matrix)

# make the nested list that contains same amount of arrays as the numbers have
# for index in range(len(keywords_list)):
# array_to_check.append([])
# print(len(keywords))




















#import array

#def calculate_times_a_number_in_array(array_to_check):

    #array_to_evaluate = []
#    array_to_evaluate = set(array_to_check)
#    for index_of_array_to_check in range (0,len(array_to_check)):
#        count=0
#        for index_of_array_to_evaluate in range (0,len(array_to_evaluate)):
#            #count=0
#           if array_to_evaluate[index_of_array_to_evaluate] == array_to_check[index_of_array_to_check]:
#                count+=1
#                #print(count)
#        print(array_to_evaluate[index_of_array_to_evaluate],":",count)
#    print(array_to_evaluate)
#    print(array_to_check)


#calculate_times_a_number_in_array([2,2,4])










#    for each_array_to_evaluate in array_to_evaluate:
#       count = 0
#       for each_array_to_check in array to check:
#              if each_array_to_evaluate == each_array_to_check:
#              count += 1
#           print(each_array_to_evaluate, ": ", count)

#calculate_times_a_number_in_array([2,2,4])
