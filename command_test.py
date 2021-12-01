

command=None

def command_test():
    command = input("Enter command: ")

    if command=='q' or command=='quit':
	    print('Yes!')
    else:
        print("No")


command_test()
