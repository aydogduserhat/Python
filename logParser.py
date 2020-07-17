nameoflog = input("Please type the name of log file (etc. log.log)...")
file = open(nameoflog, 'r')
lines = file.readlines()
def groupIp():
     ipadress = []
     for line in lines:
          ipadress.append(line)
     ipadress.sort()
     for i in ipadress:
          print(i)
def calculateBytes():
     list = []
     for line in lines:
          list.append(line.split()[9])

     for i in range(0, len(list)):
          if list[i] == '-':
               list[i] = 0

     for i in range(0, len(list)):
          if list[i] == '-':
               print("If you see this message, you still have '-' elements in your list")
     for i in range(0, len(list)):
          list[i] = int(list[i])
     sum = 0
     for i in range(0, len(list)):
          sum += i
     print(sum, "bytes are transferred")
def groupHTTP():
     list = []
     list2 = []
     list3 = []
     for line in lines:
          list.append(line)
     for line in list:
          list2.append(str(line.split()[8]) + " " + str(line.split()))
     list2.sort(reverse=True)
     for i in list2:
          list3.append(i[4:])
     for i in list3:
          print(i)
def requestCount():
     sum = 0
     for line in lines:
          sum += 1
     print(sum)
switch = True
while switch == True:
     key = input("1 for grouping by ip adress \n 2 for grouping by HTTP Status code \n 3 for see the total number of bytes transferred \n 4 for see request count \n 5 for exit")
     if key == "1":
          groupIp()
     elif key == "2":
          groupHTTP()
     elif key == "3":
          calculateBytes()
     elif key == "4":
          requestCount()
     elif key == "5":
          switch = False
     else:
          print("Please enter a valid number...")
          pass
