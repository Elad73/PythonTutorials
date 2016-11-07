

# -----------------------------------------------------------------------------------------------------------------------#
# THE MOSE NUMBERS
def the_most_numbers(lsNumbers):
    return 0 if not len(lsNumbers) else max(lsNumbers) - min(lsNumbers)

print(the_most_numbers(1, 2, 3))
# -----------------------------------------------------------------------------------------------------------------------#
# THREE WORDS
def three_words(text):

    index = 0
    for item in text.split():
        if item.isdigit(): index = 0
        else:
            index += 1
            if index == 3:
                return True

    return False


# -----------------------------------------------------------------------------------------------------------------------#

# SECRET MESSAGE
def secret_message(str1):
    ls_message = []
    for char in str1:
        if char.isupper(): ls_message.append(char)
    return ''.join(ls_message)

# -----------------------------------------------------------------------------------------------------------------------#

# EVEN THE LAST

def evenTheLast(ar):

    return 0 if not len(ar) else sum(ar[::2])*ar[len(ar)-1]

# -----------------------------------------------------------------------------------------------------------------------#

def high_and_low(numbers):
    # ...
    ls = numbers.split(" ")
    lsInt = []
    for element in ls:
        lsInt.append(int(element))
    low = high = lsInt[0]
    print(lsInt)
    #print("low:" + low)
    #print("high:" + high)
    #print("-" * 20)

    for i in lsInt:
    #    print("i:" + i)

        if i > high:
            high = i
     #       print("high:" + high)

        if i < low:
            low = i
      #      print("low:" + low)

        #print("*" * 20)

    return "".join(str(high) + " " + str(low))


# -----------------------------------------------------------------------------------------------------------------------#

def string_clean(s):
    """
        Function will return the cleaned string
        """
    resultLs = []

    for char in s:
        try:
            if int(char) not in range(10):
                resultLs.append(char)
        except:
            print(char)
            resultLs.append(char)

    print("".join(resultLs))


    return str("".join(resultLs))

# -----------------------------------------------------------------------------------------------------------------------#




