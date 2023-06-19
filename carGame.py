command=""
while True:
    command=input('> ').lower()
    if command=='start':
       print('Car started ready to go')
    elif command=="stop":
         print("Car Stoped")
    elif command=="help":
        print("""
start- to start the car
stop-to stop the car
quit- to exit
        
        """)
    elif command=="quit":
        break
    else:
            print("I don't understand that")
