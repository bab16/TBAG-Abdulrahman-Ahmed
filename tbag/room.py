def print_colored(text, color_code):
  print(f"\033[{color_code}m{text}\033[0m")


class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None  

    def get_description(self):
        return self.description
    
    def set_description(self, room_description):
        self.description = room_description

    def describe(self):
        print(self.description)

    def set_name(self, room_name):
        self.name = room_name
   
    def get_name(self):
        return self.name
    
    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def set_item(self, item):
        """Places an item in the room."""
        self.item = item

    def get_item(self):
        """Returns the item in the room."""
        return self.item

    def remove_item(self):
        """Removes the item from the room once it's collected."""
        self.item = None

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self.name)
        print("-------------------------------")
        print(self.description)

        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")
        
        if self.item is not None:
            print(f"You see a {self.item.name} here. {self.item.description}")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print_colored("You can't go that way!!!!!", 35)
            return self
