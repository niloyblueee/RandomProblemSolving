
shoes_number=int(input('Number of shoes: '))
shoe_size=list(map(int, input('Shoe sizes: ').split()))
earning=0
if len(shoe_size)!=shoes_number:
    print('invalid number of shoe sizes given')
else:
    number_of_customers=int(input(''))
    for i in range(number_of_customers):
        purchase= list(map(int, input('').split()))
        reqSize=purchase[0]
        if reqSize in shoe_size:
            shoe_size.remove(reqSize)
            earning+=purchase[1]
            
print(earning)
        
#Task

#bro is a shoe shop owner. His shop has  number of shoes.
#He has a list containing the size of each shoe he has in his shop.
#There are  number of customers who are willing to pay  amount of money only if they get the shoe of 
# their desired size.

#Your task is to compute how much money bro earned.

#Input Format

#The first line contains , the number of shoes.
#The second line contains the space separated list of all the shoe sizes in the shop.
#The third line contains , the number of customers.
#The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.
#Sample Input

#10
#2 3 4 5 6 8 7 6 5 18
#6
#6 55
#6 45
#6 55
#4 40
#18 60

#sample output
#200