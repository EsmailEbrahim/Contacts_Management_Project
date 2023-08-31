import os


class Contact:
    def __init__(self, Name, Phone, Email):
        self.Name = Name
        self.Phone = Phone
        self.Email = Email
    
    def __str__(self):
        return f"\tName: {self.Name}\n\tPhone: {self.Phone}\n\tEmail: {self.Email}"


class ContactManager:
    Contacts = []

    def AddContact(self, ContactObj):
        self.Contacts.append(ContactObj)
        return "Contact added successfuly."
    
    def RemoveContact(self, ContactName):
        for Index, Con in enumerate(self.Contacts):
            if Con.Name == ContactName:
                del self.Contacts[Index]
                return "Contact deleted successfully."
            else:
                continue
        return "Contact not found!"
    
    def SearchContact(self, ContactName):
        for Con in self.Contacts:
            if Con.Name == ContactName:
                return Con
            else:
                continue
        return None
    
    def DisplayContacts(self):
        if len(self.Contacts) == 0:
            return "No contacts found!"
        else:
            String = ""
            for Index, Con in enumerate(self.Contacts):
                if String == "":
                    String += ("_" * 20) + f"\n({Index+1}):\n{Con}\n" + ("_" * 20)
                else:
                    String += "\n" + ("_" * 20) + f"\n({Index+1}):\n{Con}\n" + ("_" * 20)
            return String


def Program(Manager):
    os.system("cls")
    print("Contacts Manager:\n")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Search Contact")
    print("4. Display Contacts")
    print("5. Exit")
    Choice = input("\nEnter your choice: ")
    if Choice == "1":
        os.system("cls")
        print("Add Contact:\n")
        Name = input("Enter name: ")
        Phone = input("Enter phone: ")
        Email = input("Enter email: ")
        Obj = Contact(Name, Phone, Email)
        print(Manager.AddContact(Obj))
        input("\nPress any key to back...")
        Program(Manager)
    elif Choice == "2":
        os.system("cls")
        print("Remove Contact:\n")
        Name = input("Enter name: ")
        print(Manager.RemoveContact(Name))
        input("\nPress any key to back...")
        Program(Manager)
    elif Choice == "3":
        os.system("cls")
        print("Search Contact:\n")
        Name = input("Enter name: ")
        print(Manager.SearchContact(Name))
        input("\nPress any key to back...")
        Program(Manager)
    elif Choice == "4":
        os.system("cls")
        print("Display Contacts:\n")
        print(Manager.DisplayContacts())
        input("\nPress any key to back...")
        Program(Manager)
    elif Choice == "5":
        exit()
    else:
        Program(Manager)


Manager = ContactManager()
Program(Manager)
