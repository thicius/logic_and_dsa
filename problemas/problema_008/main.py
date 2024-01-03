def is_abecedarian(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if i > j and x[i] < x[j]:
                return False
    return True

# This function checks whether a word is abecedarian, i. e., its letters are in alphabetical order


print(is_abecedarian('coisa'))
print(is_abecedarian('cego'))
