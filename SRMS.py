import SRMS_MODULE as srms
from os import system,name
system('cls')
choice = srms.menu()
while choice >= 1 and choice <=5:
    if(choice == 1):
        srms.add()
    elif(choice == 2):
        srms.view()
    elif(choice == 3):
        srms.search()
    elif(choice == 4):
        srms.delete()
    elif(choice == 5):
        exit()
    choice = srms.menu()
