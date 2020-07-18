'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def check_2(list):

    # THtHThth
    pass


counter = 0


def count_th(word):
    global counter
    # end = len(word)
    # if len(word) == 0:
    #     return 0
    # if word[0] + word[0 + 1] != 'th':
    #     word = word[1::]
    #     counter = counter + 1
    #     return count_th(word)
    # else:
    #     return counter

    # counter = 0
    # if len(word) == 0:
    #     return 0
    # elif len(word) > 2:
    #     if word[len(word) // 2] is not 'h':
    #         mid = len(word) // 2
    #         left = word[:mid]
    #         right = word[mid:]
    #         count_th(left)
    #         count_th(right)
    #         print(f'left is {left}, right is {right}')
    if len(word) < 2:
        return 0

    elif word[0] + word[0 + 1] == 'th':
        return 1+count_th(word[1:])
    else:
        return count_th(word[1:])


print(count_th("abcthefthghith"))
