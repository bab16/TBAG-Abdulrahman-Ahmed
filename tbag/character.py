
def print_colored(text, color_code):
  print(f"\033[{color_code}m{text}\033[0m")



class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description 
        self.conversation = None 

    def describe(self):
        print(f"{self.name} is in this room!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation 

    def talk(self):
        if self.conversation is not None:
          print_colored(f"[{self.name} says]: {self.conversation}", 36)
        else:
            print(f"{self.name} doesn't want to talk to you!")

    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight you!")
        return True 




class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None 

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness 
    
    def fight(self, combat_item):
       
        if combat_item == self.weakness.lower():
            print_colored(f"You defeated {self.name} off with the {combat_item}!!!", 42)
            return True
        
        else:
            print(f"{self.name} DESTROYED YOU WEAKLING!")
            return False




