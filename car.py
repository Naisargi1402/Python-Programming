command = ""
started = False
while True:
	command = input(">").lower()
	if command.lower() == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started.")
	elif command.lower() == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("Car stopped.")
	elif command =="help":
        print("""
              Start - to start the car
              stop - to stop the car
              quit - to quit
              """)
    elif command == "quit":
        break
    else:
        print(" i dont understand.")
