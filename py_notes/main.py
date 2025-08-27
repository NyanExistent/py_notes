#imports

#welcome

print("Welcome to PyNotes!")
print("Type !Help to see commands")

#Important stuff

command_list = ["!Help: display commands"]
com_list_index_pos = 0 
#Main loop
while True:
    user_input = str(input("[User]-> "))

    #display commands
    if(user_input == "!Help"):
        for com in command_list: 
            print(command_list[com_list_index_pos])
            com_list_index_pos + 1
        index_pos = 0

    #create a new file
    elif(user_input== "new"):
        print("Name file...")
        user_input = str(input("[User::New]-> "))
        open(f"usr_str/{user_input}", 'w')

    #write to a selected file
    elif(user_input == "write"):

        print("what file would you like to write to?")
        file_sel = str(input("[User::Sel]-> "))

        #saves the directory, then saves what you wrote till you !!QUIT!!
        with open(f"usr_str/{file_sel}", 'w') as file:
            while(True):
                user_input = str(input("[User::Wrt]~> "))
                if user_input == "!!QUIT!!":
                    break
                else: 
                    user_input_nl = user_input + "\n"
                    file.write(user_input_nl)
    #Stops program
    elif user_input == "!!QUIT!!":
        break
                
         
    

