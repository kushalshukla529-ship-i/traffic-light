print("________________________WELCOME TO OUR CODE BY WHICH YOU CAN KNOW ABOUT TRAFFIC LIGHT BY TIME_____________________________ ")
time= int(input("Write current hour in the form (0-23):"))
traffic=input("What is the current condition of the traffic light(high/medium/low): ") 
if 0<=time<7:
    print("Signal: Blinking Yellow")
elif traffic=="high" and 7<=time<=10 or 5<=time<=8:
    print("Green Light for 60 secounds")
elif traffic== "medium":
    print("Green light for 40 secounds")
elif traffic=="low":
    print("Green light for 20 secounds")
else:
    print("Invalid input")