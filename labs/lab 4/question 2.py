#Primts hellow world
def helloWorld():
    print("Hello World")
          
#Prints hello world a certain number of times
def helloWorldNTimes(n):
    for i in range(n):
        helloWorld()

#Include a "main" function
def main():
    helloWorldNTimes(2)
    helloWorldNTimes(1)
    helloWorldNTimes(3)
    helloWorldNTimes(2)

#Calll tthe main function
main()