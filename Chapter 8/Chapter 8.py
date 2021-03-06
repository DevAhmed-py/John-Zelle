#CHAPTER 8: LOOP STRUCTURES AND BOOLEANS

#No 1
'''
print('This program computes the nth term of a Fibonacci series\n')

nth = int(input('Enter a nth term of the Fibonacci series you want: '))

def fibo(nth):

    a, b = 0, 1

    for i in range(3,nth+1):
        c = a + b
        a = b
        b = c

    print('\n{0}'.format(c))

fibo(nth)

## USING while loop ##

nth = int(input('Enter a nth term of the Fibonacci series you want: '))

a,b = 0, 1
sum = 0
while nth-2 > sum:
    c = a + b
    a = b
    b = c
    sum += 1
print(c)


#No 2

print('This program prints a nicely formatted table of windchill values')

def windchill(temperature, windspeed):
    if windspeed > 3:
        
        windChill = 35.74 + 0.6215*temperature - 35.75*(windspeed**0.16) + 0.4275*temperature * (windspeed**0.16)
        #windChill = round(windChill,2)
    else:
        windChill = 0
        
    return windChill

print('\n{0:>10}  {1:6} {2:7} {3:7} {4:7} {5:7} {6:7} {7:7} {8:7}'.format(-20,-10,0,10,20,30,40,50,60))
print('-----------------------------------------------------------------------------')
for windspeed in range(5,50,5):
    print('{0:2}  {1:0.3f}  {2:0.3f}  {3:0.3f}  {4:0.3f}  {5:0.3f}  {6:0.3f}  {7:0.3f}  {8:0.3f}  {9:0.3f}'.format(windspeed,windchill(-20,windspeed),windchill(-10,windspeed),windchill(0,windspeed),windchill(10,windspeed),windchill(20,windspeed),windchill(30,windspeed),windchill(40,windspeed),windchill(50,windspeed),windchill(60,windspeed)))


#No 3

print('This program calculates the period it takes to double an investment')

apr = float(input('Enter the annualized interest rate: '))

principal = float(input('Enter the initial investment: '))
finalPrincipal = principal*2
years = 0

while principal < finalPrincipal:

    interest = principal * apr
    years += 1
    principal += interest

print(principal)
print(years)


#No 4

print('This program calculates the Syracuse sequence\n')

def syr(x):
    if x % 2 == 0:
        syrX = x / 2

    elif x % 2 == 1:
        syrX = 3 * x + 1

    return syrX

x = int(input('Enter a number to start the Syracuse sequence: '))
print('\n{}'.format(x),end=' ')

while x > 1:

    syrX = syr(x)
    x = syrX
    print(int(syrX),end=' ')


#No 5
import math as m

print('This program determine if an input is a prime number or not')

n = int(input('\nEnter a number: '))

if n == 0:
    n = eval(input("Your number must be higher than 0: "))
    
elif (n % 1 != 0):
    n = eval(input("The number you entered was not whole: "))
    
elif (n < 1):
    n = eval(input("The number you entered was not positive: "))
    
else:
    x = m.sqrt(n)
    i = 2

    while i <= x:
        
        value = n % i
        #if any value is divisble, break and close program
        
        if value == 0:
            break
        #if no value is divisible evenly, print("The number is prime.")
        else:
            i = i + 1
            
    print('\nThe number is prime.')
    

#No 6

import math as m

def primeNum(n):

        #check if n is evenly divisible by values between 2 and int(m.sqrt(n))
        x = m.sqrt(n)
        i = 2

        while i <= x:
            value = n % i
            #if any value is divisble, break and close program
            if value == 0:
                return
            #if no value is divisible evenly, print("The number is prime.")
            else:
                i = i + 1
        print(n)

def main():
    x = eval(input("Input a positive whole number: "))
    #Validate x as a positive whole number
    if x == 0:
        x = eval(input("Your number must be higher than 0: "))
    elif (x % 1 != 0):
        x = eval(input("The number you entered was not whole: "))
    elif (x < 1):
        x = eval(input("The number you entered was not positive: "))
    else:
        for n in range(x):
            primeNum(n+1)

main()


#No 7

import math as m

def primeNum(n):
        #check if n is evenly divisible by values between 2 and int(m.sqrt(n))
        x = m.sqrt(n)
        i = 2
        while i <= x:
            value = n % i
            if value == 0:
                return None
            else:
                i = i + 1
        return n
def main():
    x = eval(input("Input a positive whole number: "))
    #Validate x as a positive whole number
    if x == 0:
        x = eval(input("Your number must be higher than 0: "))
    elif (x % 1 != 0):
        x = eval(input("The number you entered was not whole: "))
    elif (x < 1):
        x = eval(input("The number you entered was not positive: "))
    elif (x % 2 != 0):
        x = eval(input("The number you entered was not even: "))
    else:
        n = x
        while n > 0:
                prime = primeNum(n+1)
                if prime != None:
                        prime2 = x - prime
                        test = primeNum(prime2)
                        if test != None:
                            print("{0} + {1} = {2}".format(prime, prime2, x))
                n = n - 1 
                
main()


#No 8

#Euclid's algorithm

def main():
    m, n = eval(input("\nPlease enter 2 numbers, separated by a comma: "))

    try:
        if m < n:
            y = n
            n = m
            m = y
            
        while m != 0:
            y = m
            m = n % m
            n = y

        print("\nThe Greatest Common Divisor is {}".format(n))

    except TypeError:
        print("\nThe input must be numerical.")

main()


#No 9

#This program computes the fuel efficiency of a multi-leg journey
def MPG(start_odom):
    count = 0

    #get information about a series of legs
    leg = 0
    totGas = 0
    while leg != "\n":
        #current odometer and amount of gas used separated by space
        leg = input("Enter the current odometer and amount of gas (gallons), \nseparated by a space (<Enter> to quit)>> ")
        try:
            newodom, gas = leg.split(" ")
            newodom = eval(newodom)
            gas = eval(gas)

            count = count + 1

            #distance traveled per leg
            distance = newodom - odom
            #compute MPG for leg
            legMPG = distance/gas

            #set new odometer reading
            odom = newodom

            print("On leg {0}, you got {1}/gal.".format(count, round(legMPG, 2)))

            #add values to trip total
            totGas = totGas / gas
        except ValueError:
            break
    return totGas, distance

def main():
#Prompt the user for the starting odometer
    odom = int(input("What is your current odometer reading: "))
    totGas, distance = MPG(odom)

#print out miles/gal on each leg and the total MPG for the trip
    totMPG = distance + totGas
    print("On whole trip, you averaged {1}/gal.".format(count, round(totMPG, 2)))
main()


#No 10

#This program computes the fuel efficiency of a multi-leg journey
def MPG(odom, infile):
    count = 0

    #get information about a series of legs
    totGas = 0
    totDistance = 0
       
    for leg in infile.readlines():
        leg = str(leg)
        while leg != "\n":
            #current odometer and amount of gas used separated by space
            try:
                newodom, gas = leg.split(" ")
                newodom = eval(newodom)
                gas = eval(gas)

                count = count + 1

                #distance traveled per leg
                distance = newodom - odom
                
                #total distance
                totDistance = distance + totDistance

                #compute MPG for leg
                legMPG = distance/gas

                #set new odometer reading
                odom = newodom

                print("On leg {0}, you got {1}/gal.".format(count, round(legMPG, 2)))

                #add values to trip total
                totGas = totGas + gas
                totMPG = totDistance / totGas
                break

            except ValueError:
                break
    
    return totMPG

def main():
#Prompt the user for the starting odometer
    fname = input("Enter filename: ")
    infile = open(fname, "r")

    odom = int(input("What is your current odometer reading: "))
    totMPG = MPG(odom, infile)

#print out miles/gal on each leg and the total MPG for the trip
    print("On whole trip, you averaged {0}/gal.".format(round(totMPG, 2)))
main()


#No 11

def main():
    avgTemp = 0
    coolDeg = 0
    heatDeg = 0
    while True:
        #Accept input in degrees
        avgTemp = input("Enter average daily temperature (Type 'Exit' to quit)>> ")
        if avgTemp.lower() == "exit":
            break
        else:
            try:
                avgTemp = int(avgTemp)

                if avgTemp < 60:
                    coolDeg = coolDeg + abs((avgTemp - 60))
                elif avgTemp > 80:
                    heatDeg = heatDeg + (avgTemp - 80)
                else:
                    avgTemp = avgTemp
            except ValueError:    
                print("Make sure your input is a number.")
            except IndexError:
                print("Make sure your input is a number.")

                

    print("The cooling degree-day is {0} and the heating degree-day is {1}".format(coolDeg, heatDeg))

main()
'''

#No 12

#This program accepts a sequence of average daily temps and computes
#the running total of cooling and heating degree days

def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")

    coolDeg = 0
    heatDeg = 0
    avgTemp = 1

    while avgTemp != None:
        #Accept input in degrees
        for avgTemp in infile.readlines():
            print(avgTemp)
            try:
                avgTemp = int(avgTemp[0:-1])

                if avgTemp < 60:
                    coolDeg = coolDeg + abs((avgTemp - 60))
                elif avgTemp > 80:
                    heatDeg = heatDeg + (avgTemp - 80)
                else:
                    avgTemp = avgTemp
            except ValueError:
                if avgTemp[0:-1] == '':
                    break
                else:
                    return False
            finally:
                infile.close()
        break
    print("The cooling degree is {0} and the heating degree is {1}.".format(coolDeg, heatDeg))


main()
