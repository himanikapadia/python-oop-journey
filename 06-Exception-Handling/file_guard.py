class EmptyFileError(Exception):
    # Custom Exception for empty files.
    pass

filename=input("Enter File name: ")

try:
    #trying opening file
    file=open(filename,"r")

    #Read the file content
    content=file.read()

    #Raise Custom Exception if file is empty
    if content.strip()=="":
        raise EmptyFileError("The File is Empty!")

except FileNotFoundError:
    print("The File not found!")

except PermissionError:
    print("Permission denied for accessing File")

except EmptyFileError as e:
    print(f" CAUTION: {e}")

# If there is not error
else:
    print("File Opened Successfully")
    print("\n----- File Content -----")
    print(content)

# This block Always runs 
finally:
    try:
        file.close()
        print("File Closed Successfully!")

    except NameError:
        print("No File was Opened!")