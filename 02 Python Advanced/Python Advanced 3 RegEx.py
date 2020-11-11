PYTHON REGEX DRILL //
=======================================================================
/^(?:(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})[.](?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})[.](?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})[.](?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2}))$/
This looks for a valid IPv4 address with four decimal numbers in the valid range, like 128.0.0.1 or 255.255.255.240, but not 999.999.999.999.

DRILL
  #s='sssgdds8sfsfs'
  #print(re.findall("([0-9]+)", s))

  #s='sssgdds-8sfsfs'
  #print(re.findall("(-[0-9]+)", s))

  #s='sssgdds-8s8fsfs'
  #print(re.findall("(-?[0-9]+)", s))

  #text = '21 scouts and 3 tanks fought against 4,003 protestors, so the manager was not 100.00% happy.'
  #print(re.findall("([0-9]+[.|,]?[0-9]*)", text))  # * means zero or more

  #text1 = "He had prudently disguised himself but   was quickly captured by the police."
  #print(re.findall("([A-z]+ly)", text1))

License plate
def main():

  plate = input("Enter your License plate number:")

  if (re.match("^[A-Z]{2}-[0-9]{3}-[A-Z]{2}$", plate)): 
      print("Good, this is a license plate number.")
  else:
      print("Not good, this is NOT a license plate number.")

main()

IP4
import re

def main():

  ip = input("Enter your IP address :")
   if (re.match("^([0-2][0-5][0-5]{1}|[0-1][0-9][0-9]{1}|[0-9]{0,1}[0-9]{1}).([0-2][0-5][0-5]{1}|[0-1][0-9][0-9]{1}|[0-9]{0,1}[0-9]{1}).([0-2][0-5][0-5]{1}|[0-1][0-9][0-9]{1}|[0-9]{0,1}[0-9]{1}).([0-2][0-5][0-5]{1}|[0-1][0-9][0-9]{1}|[0-9]{0,1}[0-9]{1})$", ip)):
      print("Good, this is a valid IP address.")
  else:
      print("Not good, this is NOT a valid IP address.")

# note, without parenthesis for each of the 4 parts it would pass for expample 20 as a valid IP4, next to a valid IP4 of course

email
import re

def main():

  mail = input("Enter your email :")
  match = (re.match("^[a-zA-Z0-9_\-\.+]+@[A-z]+.[A-z]+$", mail))
  while match is None:
    print("Not good, this is NOT a valid email address.")
    mail = input("Enter your email :")
    match = (re.search("^[a-zA-Z0-9_\-\.+]+@[A-z]+.[A-z]+$", mail))
  else:
    print("Good, this is a valid email address.")

main()

email+password

import re

def main():

  mail = input("Enter your email :")
  match = (re.match("^[a-zA-Z0-9_\-\.+]+@[A-z]+.[A-z]+$", mail))
  while match is None:
    print("Not good, this is NOT a valid email address.")
    mail = input("Enter your email :")
    match = (re.search("^[a-zA-Z0-9_\-\.+]+@[A-z]+.[A-z]+$", mail))
  else:
    print("Good, this is a valid email address.")
    password = input("Enter your Password :")
    if (re.match("^(.){6,}$", password)):
      print("Good, this is a valid password.")
    else:
      print("Not good, this is NOT a valid password.")

main()

10 VAlid Password bis laatste vleugel voorgaande

if (re.match("^(?=[a-z]+)(?=[A-Z]+)(?=[0-9]+)([?=\$#@]+)(.{2,})$", password)):
      print("Good, this is a valid password.")
    else:
      print("Not good, this is NOT a valid password.")

main()

groups / 2 approaches to split an emailaddress "audrey.boulevart@benextcomapgny.com"

 m = re.search("^(?P<who>\w*)[.]?(?P<who2>\w*)@(?P<operator>\w+)[.](?P<zone>\w+$)", "audrey.boulevart@benextcomapgny.com")
  if m is not None:
    print (m.group("who"))
    print (m.group('who2'))
    print (m.group('operator'))
    print (m.group('zone'))
  """


  mail="audrey.boulevart@benextcomapgny.com"
  splitMail = mail.replace('.',' ').split('@').copy() # splitmail ['audrey boulevart', 'benextcomapgny com']

  firstName =[]
  name =[]
  ope =[]
  zone =[]

firstName.append(splitMail[0].split()[0]) # splits standard on " " , appends 1st item in list splitMail to this list
  name.append(splitMail[0].split()[-1]) # index -1 always prints last item in Splitmail(in case more then 2 items in SPlitmail
  ope.append(splitMail[1].split()[0])
  zone.append(splitMail[1].split()[-1])

  print(firstName, name, ope, zone)

to split both approaches into lists:

import re

def main():

  # VERSION 1 - using re.search
  m = re.search("^(?P<who>\w*)[.]?(?P<who2>\w*)@(?P<operator>\w+)[.](?P<zone>\w+$)", "audrey.boulevart@benextcomapgny.com")
  if m is not None:
    firstName =[]
    name =[]
    zone =[]
    ope =[]
    firstName.append(m.group("who"))
    name.append(m.group('who2'))
    ope.append(m.group('operator'))
    zone.append(m.group('zone'))
  print(firstName, name, ope, zone)

  # VERSION 2 - using replace and split
  mail="audrey.boulevart@benextcomapgny.com"
  splitMail = mail.replace('.',' ').split('@').copy()
  print(splitMail)

  firstName =[]
  name =[]
  ope =[]
  zone =[]

  firstName.append(splitMail[0].split()[0])
  name.append(splitMail[0].split()[-1])
  ope.append(splitMail[1].split()[0])
  zone.append(splitMail[1].split()[-1])

  print(firstName, name, ope, zone)


main()

==> version 1 can only handle emails exactly in the given format a.a@b.b, version 2 can work with a.a.a@b.b.b, only splits at "." to " "






