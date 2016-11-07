__author__ = 'eladron'

#A python challange from: http://pythonhow.com/challenge/instructions.html


str = "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et "\
"magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, "\
"pellentesque  eu,  pretium  quis,  sem.  Nulla  consequat  massa  quis  enim.  Donec  pede "\
"justo,  fringilla  vel,  aliquet  nec,  vulputate  eget,  arcu.  Etiam  ultricies  nisi  vel  augue. "\
"Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Aenean commodo "\
"ligula  eget  dolor.  Aenean  massa.  Cum  sociis  natoque  penatibus  et  magnis  dis "\
"parturient python, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque "\
"eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla "\
"vel,  aliquet  nec,  vulputate  eget,  arcu.  Etiam  ultricies  nisi  vel  augue.  Curabitur "\
"ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Cum sociis natoque penatibus "\
"et  magnis  dis  parturient  montes,  nascetur  ridiculus  mus.  Donec  quam  felis,  ultricies "\
"nec,  pellentesque  eu,  pretium  quis,  axa  quouq.  Nulla  consequat  massa  quis  enim. "\
"Donec pede justo, fringilla vel, aliquet nec,  vulputate eget,  arcu. Etiam ultricies nisi "\
"vel  augue.  Curabitur  ullamcorper  ultricies  nisi.  Proin  at  neque  et  tellus  ultricies "\
"consequat.  Duis  vitae  mi  commodo,  suscipit  nunc  vel,  porta  tellus.  In  eu  volutpat "\
"sapien.  Mauris  dignissim  velit  eget  diam  tristique,  nec  egestas  magna  maximus. "\
"Pellentesque  python,  lorem  a  eleifend  vehicula,  arcu  urna  facilisis  odio,  maximus "\
"maximus  massa  nisl  sed  sapien.  Quisque  nisi  nunc,  dignissim  ut  malesuada  non, "\
"fringilla  vitae  sem.  Nunc  turpis  quam,  rutrum  at  egestas  ut,  pretium  tincidunt  est. "\
"Praesent  imperdiet  mauris  eu  felis  lobortis  vehicula.  Sed  dictum  lorem  at  rutrum "\
"rhoncus. Suspendisse sit amet ex ac eros python cursus. Duis pretium rutrum lacus, sit "\
"amet vulputate ipsum condimentum vel. Vivamus lacus ipsum, python in justo quis, "\
"blandit condimentum velit. Sed semper posuere leo, elementum tristique leo euismod "\
"quis."

#number of characters in string
numberOfCharecters = len(str)

#9'th characters in string
charecter99 = str[100]

#middle charecter in string
def midOfStr(str,numPlaces):

    if len(str)%2: middle =  len(str)/2
    else:          middle =  len(str)/2

    return str[middle-numPlaces: middle+numPlaces+1]


def numberOfWords():
    lsWords = str.split()
    return len(lsWords)

def fromEnd270And270FromBegining():
    lsWords = str.split()
    return [lsWords[-272], lsWords[-271],lsWords[-270],lsWords[-269], lsWords[269],lsWords[270],lsWords[271]]


print(fromEnd270And270FromBegining())