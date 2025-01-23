print("1.Add a contact\n2.Edit a contact\n3.Delete a contact\n4.Search a contact\n5.List all contacts\n6.Exit")
cb={}
choice=int(input("Enter the choice:"))
while choice!=6:
    if choice==1:
        name=input("Enter the name:")
        phone=int(input("Enter the phone number:"))
        cb[name]=phone
        print("contact added successfully")
    elif choice==2:
        name=input("Enter the name:")
        phone=int(input("Enter the phone number:"))
        cb[name]=phone
        print("contact edited successfully")
    elif choice==3:
        name=input("Enter the name:")
        cb.pop(name)
        print("contact deleted successfully")
    elif choice==4:
        name=input("Enter the name:")
        print(f"phone number of {name} is {cb[name]}")
    elif choice==5:
        print("Name\t\t\t\t\t\t\tPhone number")
        print('------------------------------------------')
        for i,j in cb.items():
            print(i,"\t\t\t\t\t\t\t\t",j)
    elif choice==6:
        break
    else:
        print("Invalid")
    choice=int(input("Enter the choice:"))


    
      



    



    


    
        
        
