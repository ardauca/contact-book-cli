import json

def load_contacts():
        try:
            with open("contacts.json", "r", encoding="utf-8") as dosya:
                return json.load(dosya) # JSON metnini Python listesine çevirir
        except (FileNotFoundError, json.JSONDecodeError):
                # Dosya yoksa veya içi bozuksa çökmek yerine boş liste döner
            return []

def save_contacts(contacts):
    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)

def add_contact(contacts):
    if len(contacts) == 0:
        new_id = 1
    else:
        maxid = 0
        for kisi in contacts:
            if kisi["id"] > maxid:
                maxid = kisi["id"]
        new_id = maxid + 1

    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()
    email = input("Enter contact email: ").strip()

    if name == "" or phone == "":
        print("\nHata: İsim ve Telefon alanları boş bırakılamaz! Ana menüye yönlendiriliyorsunuz.\n")
        return  # Hata varsa fonksiyondan çık, sözlüğü hiç oluşturma

    # 3. Her şey doğruysa sözlüğü oluşturup listeye ekliyoruz
    newcontact = {
        "id": new_id,
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contacts.append(newcontact)
    print(f"Kişi {new_id} ID'si ile eklendi!")
def list_contacts(contacts):
    if len(contacts) == 0:
        print("\n Contacts are empty.\n")
    else:
        for kisi in contacts:
            print(f'{kisi["id"]}, {kisi["name"]}, {kisi["email"]}, {kisi["phone"]}')

def search_contact(contacts):
    arama_kelimesi=input("Enter the name of the contact you want to search: ").strip().lower()
    eslesen=[]
    for i in contacts:
        if str(arama_kelimesi) in i["name"].strip().lower(): #== yerine in kullandık çünkü "==" tam eşleşme için kullanılır.
            eslesen.append(i)
    if len(eslesen)==0:
        print("Eşleşme bulunamadı.") 
    else:
        for kisi in eslesen:
            print(f'{kisi["id"]}, {kisi["name"]}, {kisi["email"]}, {kisi["phone"]}')



def delete_contact(contacts):
    try:
        silinecek_id = int(input("Silmek istediğiniz kişinin ID'sini girin: "))
    except ValueError:
        print("\nHata: Lütfen geçerli bir sayısal ID girin!\n")
        return # Fonksiyondan erken çıkış
        
    bulundu = False
    
    for kisi in contacts:
        if kisi["id"] == silinecek_id:
            contacts.remove(kisi)
            bulundu = True
            print(f"\n{silinecek_id} ID'li Kisi silindi.")
            break
            
    if not bulundu:
        print(f"\nHata: {silinecek_id} ID'sine sahip bir kisi bulunamadi.\n")

def update_contacts(contacts):
    try:
        guncellenecek_id = int(input("Guncellemek istediğiniz kişinin ID'sini girin: "))
    except ValueError:
        print("\nHata: Lütfen geçerli bir sayısal ID girin!\n")
        return
        
    bulundu = False
    degisiklik_var = False 
    
    for kisi in contacts:
        if kisi["id"] == guncellenecek_id:  
            bulundu = True       

            new_name = input("Enter new contact name: ").strip()
            new_phone = input("Enter new contact phone number: ").strip()
            new_email = input("Enter new contact email: ").strip()
            
            if new_name != "":
                kisi["name"] = new_name
                degisiklik_var = True

            if new_phone != "":
                kisi["phone"] = new_phone
                degisiklik_var = True

            if new_email != "":
                kisi["email"] = new_email
                degisiklik_var = True
            
            if degisiklik_var:
                print(f"\n{guncellenecek_id} ID'li kişi başarıyla güncellendi.")
            else:
                print("\nHata: Hiçbir değişiklik yapılmadı.")
                
            break
            
    if not bulundu:
        print(f"\nHata: {guncellenecek_id} ID'sine sahip bir kisi bulunamadi.\n")

def main():

    contacts =load_contacts()

    while True:

        print("Welcome to the Contact Manager")
        print("press 1 to add contact")
        print("press 2 to list contacts")
        print("press 3 to search contacts")
        print("press 4 to update contacts")
        print("press 5 to delete contacts")
        print("press 6 to exit")
            
        secim=input("Choose an option: ")
        if secim=="1":
            add_contact(contacts)
            save_contacts(contacts)
    
        elif secim=="2":
            list_contacts(contacts)
        
        elif secim=="3":
            search_contact(contacts)
 
        elif secim=="4":
            update_contacts(contacts)
            save_contacts(contacts)

        elif secim=="5":
            delete_contact(contacts)
            save_contacts(contacts)
        
        elif secim=="6":
            break
        
        else:
            print("\nGeçersiz seçim. Lütfen tekrar deneyin.\n")
main()