command = ""
started = False
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Already started")

        else:
            started = True
            print('Your Car has been started.')
    elif command == "stop":
        if not started:
            print("Already stopped")
        else:
            started = False
            print('Your Car has been stopped.')
    elif command == "help":
        print(''' 
start - to start the car
stop - to stop the car
quit - to end the program
        ''')

    else:
        print('Thank you for using this program')


