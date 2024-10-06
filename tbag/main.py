from room import Room
from character import Enemy, Character
from item import Item





def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")


print_colored('''       ~~~~ WELCOME TO BAB'S ADVENTURE GAME ~~~~       ''', 32)


kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
treasure_room = Room("Treasure Room")  


kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall.set_description("A large room with ornate golden decorations")
treasure_room.set_description("A secret room filled with treasure and mysteries!")  


kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
dining_hall.link_room(treasure_room, "east")  


Zombae = Enemy("Zombae", "A not-so-friendly zombie")
Zombae.set_conversation('''  "ARRGGGGGG ARRGGHS BRAAINSS" ''')
Zombae.set_weakness("H2O")
dining_hall.set_character(Zombae)

Goose = Character("Goosey", "An adorable, yet intelligent silly little goose")
Goose.set_conversation(''' QUAAACK QUACK.... ~loud cough~ "oh QUACK where are my cigarettes?!" ''')
kitchen.set_character(Goose)

Rizzy = Character("Rizzy", "A mad chemist with a passion for Lidl brownies, and really wants to talk.....")
Rizzy.set_conversation(" AHA! I HAVE BEEN WAITING FOR YOU!!!! You need to use the chemical formula of aqua to defeat Zombae! HEAD BACK EAST!!")
ballroom.set_character(Rizzy)


treasure = Item("Teleporter", "a DEVICE that telports you ofcourse!!!!")
treasure_room.set_item(treasure)  


current_room = kitchen
zombae_defeated = False  
inventory = []  


while True:
    print("\n")
    current_room.get_details()
    
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("Move? (north, east, south, west), Talk?, Fight?, or Collect?: ").strip().lower()

    
    if command in ["north", "south", "east", "west"]:
        next_room = current_room.move(command)
        if next_room:
            
            if next_room == treasure_room and not zombae_defeated:
                print_colored("The Treasure Room is locked until you defeat Zombae!", 31)
            else:
                current_room = next_room
        else:
            print_colored("You can't go that way!", 31)

    
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("--- cricket noises ---")

    
    elif command == "fight":
        if inhabitant is not None:
            print_colored("Feeling BRAVE huh... ", 34)
            print("What will you fight with?: ")
            fight_with = input().strip().lower()

            
            if isinstance(inhabitant, Enemy) and inhabitant.name == "Zombae":
                if inhabitant.fight(fight_with):
                    print_colored("GOOD VICTORY BRAVE ADVENTURER!", 42)
                    current_room.set_character(None) 
                    zombae_defeated = True  
                    print_colored("You have unlocked the Treasure Room!", 32)
                    print_colored(''' I would collect whatever is in there if i was you....:) ''', 46)
                else:
                    print_colored("      YOU LOST THE FIGHT", 31)
                    print_colored('''Press "F" to pay respects, respawn and return to the game!''', 43)
                    input()
            else:
                
                if inhabitant.fight(fight_with):
                    print_colored(f"You defeated {inhabitant.name}!", 42)
                    current_room.set_character(None)  
                else:
                    print_colored("      YOU LOST THE FIGHT", 31)
                    print_colored('''Press "F" to pay respects, respawn and return to the game!''', 43)
                    input()
        else:
            print("There is no one to fight here.")

    
    elif command == "collect":
        if item is not None:
            inventory.append(item.name)  
            print_colored(f"You collected the {item.name}!", 32)
            current_room.set_item(None)  

          
            if item.name.lower() == "teleporter":
                print_colored("You've collected the Teleporter! You can now teleport to any dream destination.", 36)

               
                dream_destination = input("Where would you like to teleport to? (Type your dream destination!!!): ").strip()
                print_colored(f"Initiating teleportation sequence to {dream_destination}...", 34)
                print_colored(f"~~~WHOOOSH~~~~ You have teleported to {dream_destination}! Peace at last AYYYYYYY!!!!!", 32)
                print_colored("Thank you for playing Bab's Adventure game!! The game has now ended DROP A LIKE FOR PT2!!", 33)
            break  


            
            print_colored("Your current inventory: " + ", ".join(inventory), 34)
        else:
            print_colored("There's nothing here buddy", 35)

 
    else:
        print_colored("      Invalid command      ", 31)
