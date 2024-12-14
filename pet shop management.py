class PetShop:
    def __init__(self):
        self.pet_list = {
            'Dogs': {'Labrador': 10, 'Bulldog': 5, 'Poodle': 7,'Milo': 8,'Oreo': 3,'Popo': 4,'Charlie': 12,'Max': 11,'Rocky': 13,'Jacky': 15},
            'Cats': {'Persian': 3, 'Siamese': 4, 'Bengal': 6,'Jack': 9,'Sammy': 8,'Toby': 4,'Shadow': 11,'Simon': 15,'Jasper': 19,'Smudge': 16},
            'Birds': {'Parrot': 8, 'Canary': 12, 'Sparrow': 10,'Pigeon': 8,'Duck': 4,'Cuckoo': 3,'Sparrow': 7,'Robin': 9,'Canary': 10,'Kingfisher': 12},
        }
    def view_pet_list(self):
        if not self.pet_list:
            print("\nNo pets available in the shop.")
            return
        print("\nAvailable Pets:")
        for pet_type, breeds in self.pet_list.items():
            print(f"{pet_type}:")
            for breed, quantity in breeds.items():
                print(f"  {breed} - Available: {quantity}")
    def purchase_pet(self):
        self.view_pet_list()
        pet_type = input("Enter the type of pet you want to purchase (e.g., Dogs, Cats, Birds): ").title()
        if pet_type not in self.pet_list:
            print("Sorry, we don't have that pet type.")
            return
        breed = input(f"Enter the breed of {pet_type} you want to buy: ").title()
        if breed not in self.pet_list[pet_type]:
            print(f"Sorry, we don't have the breed {breed} of {pet_type}.")
            return
        if self.pet_list[pet_type][breed] > 0:
            print(f"{breed} is available.")
            confirm = input(f"Are you sure you want to purchase {breed}? (yes/no): ").lower()
            if confirm == 'yes':
                self.pet_list[pet_type][breed] -= 1
                print(f"{breed} purchased successfully!")
            else:
                print("Purchase canceled.")
        else:
            print(f"Sorry, {breed} is not available right now.")
    def add_pet(self):
        pet_type = input("Enter the type of pet to add (e.g., Dogs, Cats, Birds): ").title()
        if pet_type not in self.pet_list:
            print("This is a new pet type. Adding it to the list.")
            self.pet_list[pet_type] = {}
        breed = input(f"Enter the breed of {pet_type} to add: ").title()
        try:
            quantity = int(input(f"Enter the quantity of {breed} to add: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        if breed in self.pet_list[pet_type]:
            self.pet_list[pet_type][breed] += quantity
        else:
            self.pet_list[pet_type][breed] = quantity
        print(f"{quantity} {breed}(s) added to the list.")
    def delete_purchased_pet(self):
        pet_type = input("Enter the type of pet to delete (e.g., Dogs, Cats, Birds): ").title()
        if pet_type not in self.pet_list:
            print("No such pet type found.")
            return
        breed = input(f"Enter the breed of {pet_type} to delete: ").title()
        if breed not in self.pet_list[pet_type]:
            print(f"No breed {breed} of {pet_type} found.")
            return
        try:
            quantity = int(input(f"Enter the quantity of {breed} to delete: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        if quantity <= self.pet_list[pet_type][breed]:
            self.pet_list[pet_type][breed] -= quantity
            print(f"{quantity} {breed}(s) deleted from the list.")
        else:
            print(f"Cannot delete more than the available quantity of {breed}.")
def menu():
    shop = PetShop()
    while True:
        print("\nPet Shop Management System")
        print("1. View Pet List")
        print("2. Purchase Pet")
        print("3. Add New Pet")
        print("4. Delete Pet")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            shop.view_pet_list()
        elif choice == "2":
            shop.purchase_pet()
        elif choice == "3":
            shop.add_pet()
        elif choice == "4":
            shop.delete_purchased_pet()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    menu()