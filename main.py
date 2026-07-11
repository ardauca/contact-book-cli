def load_contacts():
    pass

def save_contacts(contacts):
    pass

def add_contact(contacts):
    if len(contacts)==0:
        new_id=1
    else:
        maxid=0
        for kisi in contacts:
            if kisi["id"]>maxid:
                maxid = kisi["id"]
        new_id = maxid + 1
    newcontact = {
        "id": new_id,
        "name" : input("Enter contact name: "),
        "phone": input("Enter contact phone number: "),
        "email": input("Enter contact email: ")
        
    }

    contacts.append(newcontact)
    print(f"Öğrenci {new_id} ID'si ile eklendi!")

def list_contacts(contacts):
    if len(contacts) == 0:
        print("\n Contacts are empty.\n")
    else:
        for kisi in contacts:
            print(f'{kisi["id"]}, {kisi["name"]}, {kisi["email"]}, {kisi["phone"]}')

def search_contact(contacts):
    pass

def delete_contact(contacts):
    pass

def main():

    contacts =load(contacts
                   )

    while True:

        print("Welcome to the Contact Manager")
        print("press 1 to add contact")
        print("press 2 to list contacts")
        print("press 3 to search contacts")
        print("press 4 to delete contacts")
        print("press 5 to exit")
            
        secim=input("Choose an option: ")
        if secim=="1":
            add_contact(contacts)
    
        elif secim=="2":
            list_contacts(contacts)
        
        elif secim=="3":
            search_contact(contacts)
        
        elif secim=="4":
            delete_contact(contacts)
        
        elif secim=="5":
            break
        
        else:
            print("\nGeçersiz seçim. Lütfen tekrar deneyin.\n")
main()