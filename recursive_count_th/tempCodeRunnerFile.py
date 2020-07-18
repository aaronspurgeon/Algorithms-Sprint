    mid = len(word) // 2
            left = word[:mid]
            right = word[mid:]
            count_th(left)
            count_th(right)
            print(f'left is {left}, right is {right}')