from API import Zendesk

x = Zendesk()
print('Welcome to ticket viewer')
print('Type' + '\'' + 'menu' + '\'' + ' to view options or' + '\'' + 'quit' + '\'' + 'to exit')
instruction = input()
if instruction == 'menu':
    x.requestData()
    while True:
        print('       Select View Options')
        print('       *Press 1 to view all tickets')
        print('       *Press 2 to view all tickets')
        print('       *Type' + '\'' + 'quit' + '\'' + 'to exit')
        instruction2 = input()
        if instruction2 == '1':
            x.handleData1()
        elif instruction2 == '2':
            print('Enter ticket number:')
            instruction3 = input()
            x.handleData2(int(instruction3))
        elif instruction2 == 'quit':
            print('quit')
            print('Thanks for using the viewer. GoodBye')
            exit()
        else:
            print('Wrong instruction!')
elif instruction == 'quit':
    print('quit')
    print('Thanks for using the viewer. GoodBye')
    exit()
else:
    print('Wrong instruction!')