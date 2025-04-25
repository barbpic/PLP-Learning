from pet import Pet

def main():
    print("🐾 Welcome to the Digital Pet Simulator! 🐾")
    
    # Create a new pet
    pet_name = input("What would you like to name your pet? ")
    my_pet = Pet(pet_name)
    
    # Display initial status
    my_pet.get_status()
    
    # Main game loop
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Put your pet to sleep")
        print("3. Play with your pet")
        print("4. Check status")
        print("5. Teach a new trick (Bonus)")
        print("6. Show learned tricks (Bonus)")
        print("7. Quit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            my_pet.eat()
        elif choice == "2":
            my_pet.sleep()
        elif choice == "3":
            my_pet.play()
        elif choice == "4":
            my_pet.get_status()
        elif choice == "5":
            trick = input("What trick would you like to teach? ")
            my_pet.train(trick)
        elif choice == "6":
            my_pet.show_tricks()
        elif choice == "7":
            print(f"Thanks for playing with {my_pet.name}! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        # Small delay for better UX
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()