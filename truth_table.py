import ttg
import string
import re
# print(ttg.Truths((['p', 'q', 'r'])))
#
#
# input (a ard b and c and d)
#
# if " AND " in sentence:
#     count = count + 1
#     split AND
# elif "OR" in sentence:
#     split OR
def split(word):
    return [char for char in word]


sentence = "not a and b and c or d xor e"
a = sentence.replace(" ","")
count = 0
str = ""
str2 = ""
str3 = ""

gates = ["and", "or"]



# if "and" in sentence:
#     x = sentence.split("and")
#     for y in x:
#             str +=y
#     b = str.split(" ")
#     for y in b:
#         if len(y)==1:
#             str2 +=y


# if "or" in str2:
#     x = str2.split("or")
#     for y in x:
#             str3 +=y
#     b = str.split(" ")
#     for y in b:
#         if len(y)==1:
#             str3 +=y
#


if __name__ == '__main__':

    # [ele for ele in test_list if (ele in test_string)]

    print(ttg.Truths(['a', 'b', 'c'], ['not((a or b) and c)']))

    # if any(word in sentence for word in gates):
    #     x = re.split('and |or | not | xor', sentence)
    #     for y in x:
    #         str += y
    #     b = str.split(" ")
    #     for y in b:
    #         if len(y) ==1:
    #             str2 += y
    #     print(str2)
    # str4 = split(str2)
    #
    # print(ttg.Truths(str4, [sentence]))
    # print(str2)


#Codigo viejo
value = ''
# if len(var_name) != 1:
#     temp = split(var_name)
#     print(ttg.Truths(temp))
#     return res.success(value)
#
# print(ttg.Truths([var_name]))
# return res.success(value)

