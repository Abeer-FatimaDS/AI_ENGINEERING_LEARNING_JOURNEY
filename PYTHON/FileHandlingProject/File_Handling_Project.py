from pathlib import Path
import os

def Create_File():
    try:
        name = input("Please tell your name: ")

        path = Path(name)

        if not path.exists():
            with open(path, "w") as f:
                data = input("What do you want to write? ")
                f.write(data)

            print("File Created Successfully")
        else:
            print("Enter some other name. File name already exists")

    except Exception as err:
        print(f"An Error occurred: {err}")
def Read_File():
    try:
        name = input("Please tell your file name :- ")
        path = Path(name)
        if path.exists():
            with open(path,"r") as fs:
                content = fs.read()
                print(f"your file content is \n {content}")
        else:
            print("error no such file exists")
    except Exception as err:
        print(f"An error occured as {err}")
def Update_File():
    try:
        name = input("please tell your file name :- ")
        path = Path(name)

        if path.exists():
            print("operations ")
            print("1 . Renaming the file ")
            print("2 . Appending the content")
            print("3 . Overwriting the file ")

            choice = int(input("Enter your option :- "))

            if choice == 1:
                newname = input("tell your new file name:- ")
                new_path = Path(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print("renamed successfully ")
                else:
                    print("file already exists")
            
            elif choice == 2:
                with open(path,'a') as fs:
                    data = input("what do you want to append :- ")
                    fs.write(" \n"+data)
                print("successfully appended")
            
            elif choice == 3:
                with open(path , "w") as fs:
                    data = input("what do you want to overwrite :- ")
                    fs.write(" \n"+data)
                print("successfully overwrittten")

    except Exception as err:
        print(f"An error occured as {err}")
def Delete_File():
    try:
        name = input("please tell your file name :- ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("file deleted successfully")
        else:
            print("Error no such file exists")
    except Exception as err:
        print(f"An error occured as {err}")



print("Press 1 to Create a file")
print("Press 2 to Reading a file")
print("Press 3 to Updating a file")
print("Press 4 to Deleting a file")


user_response = 0
while user_response not in [1, 2, 3, 4]:
    user_response = int(input("Enter your Response: "))
    if user_response == 1:
        Create_File()
    elif user_response == 2:
        Read_File()
    elif user_response == 3:
        Update_File()
    elif user_response == 4:
        Delete_File()
    else:
        print("PLease enter the intructed numbers. Try Again")
