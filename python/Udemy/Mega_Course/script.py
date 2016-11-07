__author__ = 'eladron'

def celsius2Farenheit(celsiusTemp) :
    if celsiusTemp < -273.3:
        return "No matter can hold this Temperature. " \
               "Think again..."
    return celsiusTemp*1.8+32;

def conditionalBlock(num, param):
    if num < param:
        res =  str(num) + " is less"
    elif num > param:
       res = str(num) + " is more, yes this is cool."
    else:
        res =  str(num) + " is equal"

    frame = '\n' + "*"*len(res) + '\n'

    return frame + res + frame

res = conditionalBlock(3,4)


def forLoops(emailLs, mailPLatform):

    mailingList = ""
    for value in emailLs:
        if mailPLatform in value:
            mailingList += value

    if len(mailingList) > 0:
        return mailingList
    else:
        return "No mail was found"

mailingList = ['elad@fusic.com', 'elad@gmail.com', 'elad@hotmail.com']

def whileLoop():
    password='python123'
    userInput = ''
    while userInput != password:
        userInput = raw_input("Enter password: ")
        print(userInput)
        if userInput == password: print("You are logged in!")
        else: print("Sorry, try again!")


def currency_converter():

    rate    = float(input("Enter rate: "))
    euros   = float(input("Enter euros: "))

    dollars = euros * rate
    return dollars

def forLoop2Lists():
    ls1 = ['jhon','jack','jason']
    ls2 = ['hotmail', 'gmail', 'yahoo']

    for i,j in zip(ls1,ls2):
        print (i,j)

temperatures = [10,-20,-289,100]
for temp in temperatures:
    print(celsius2Farenheit(temp))

#forLoop2Lists()

