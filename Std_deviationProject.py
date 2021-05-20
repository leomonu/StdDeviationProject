import math
import csv

with open('data.csv',newline="")as f:
    reader = csv.reader(f)
    file_data = list(reader)



def mean(data):
    n = len(data)
    total = 0
    for numbers in data:
        total += float(numbers[0])
    mean = total/n
    print(mean)
    return mean

mean = mean(file_data)
sqauredList = []
for number in file_data:
    a  = int(number[0])-mean
    a = a**2
    sqauredList.append(a)

sum = 0
for number in sqauredList:
    sum = sum+number

result = sum/(len(file_data))

std_deviation = math.sqrt(result)
print (std_deviation)