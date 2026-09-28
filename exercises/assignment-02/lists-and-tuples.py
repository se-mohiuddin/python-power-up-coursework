'''
Question-1:
Lists and Tuples You have been given the following data:

temperatures = [25, 30, 27, 22, 28, 33, 29]
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') 

a) Create a new list containing the temperature and day pairs as tuples. 
b) Find the maximum temperature from the list and print it along with the corresponding day. 
c) Calculate and print the average temperature.
'''
temperatures = [25, 30, 27, 22, 28, 33, 29]
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
#a)
new_list = [('Monday',25), ('Tuesday',30), ('Wednesday',27), ('Thursday',22), ('Friday',28), ('Saturday',33), ('Sunday',29)]
#b)
max=temperatures[0]
if max < temperatures[1]:
    max=temperatures[1]
if max < temperatures[2]:
    max=temperatures[2]
if max < temperatures[3]:
    max=temperatures[3]
if max < temperatures[4]:
    max=temperatures[4]
if max < temperatures[5]:
    max=temperatures[5]
if max < temperatures[6]:
    max=temperatures[6]
indx=temperatures.index(max)
print(new_list[indx])
#c)
sum=temperatures[0]+temperatures[1]+temperatures[2]+temperatures[3]+temperatures[4]+temperatures[5]+temperatures[6]
avg=sum/(len(temperatures))
print("The average temperature is :", avg)
