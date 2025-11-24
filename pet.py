def create_pet():
    pet = {
    'name' : input("Name of your pet:"),
    'happy' : 50,
    'hungry' : 50,
    'energy' : 50,
    'cleanliness' : 50,
    'health': 50,
    'mood':'netural'
    }
    return pet

def status_of_pet(pet):
    print("pet status")
    print("name of your pet:", pet['name'])
    print("energy of pet", pet['name'],pet['energy'])
    print("hunger level",pet['name'], pet['hungry'])
    print("cleaniness of",pet['name'], pet['cleanliness'])
    print("happiness level",pet['name'], pet['happy'])
    print("health of",pet['name'], pet['health'])
    print("mood of", pet['name'], pet['mood'])
def mood_of_pet(pet):
    if pet['hungry']<=70:
        pet['mood']="hungry"
    elif pet['energy']<=30:
        pet['mood']="your pet is very sleepy"
    elif pet['health']<50:
        pet['mood']="sick"    
    elif pet['happy']<=40:
        pet['mood']="play with your pet it is sad"
    elif pet['cleanliness']<=30:
        pet['mood']="irritated"
        
        
def feed_pet(pet):
    pet['hungry'] +=20
    pet['cleanliness'] -=10
    print(pet['name'],"ate food")
    
def bath_pet(pet):
    pet['cleanliness'] +=30
    pet['energy'] -=10
    pet['happy'] +=10
    print(pet['name'], "is now clean")

    
def sleep_pet(pet):
    pet['energy'] +=20
    pet['hungry'] -=20
    print(pet['name'],"has rested well")

def play_pet(pet):
    pet['energy'] -=20
    pet['happy']  +=30
    pet['hungry'] -=20
    print(pet['name'], "is now very happy")
    
def bark_pet(pet):
    pet['energy'] -=20
    pet['hungry'] -=10
    
    
def game_over(pet):
    if pet['hungry']<=0 or pet['energy']<=0 or pet['cleanliness']<=0:
        print("Your pet is Dead")
        return True
    return False
    
    
    
    
def show_menu():
    print("1 feed the pet")
    print("2 bath the pet")
    print("3 let the pet sleep")
    print("4 play with pet")
    print("5 bark")
    print("6 check status")
    print("7 Quit")
    
def main():
    pet = create_pet()
    status_of_pet(pet)
    
    while True:
        mood_of_pet(pet)
        show_menu()
        choice = input("choose an action:")
        if choice == "1":
            feed_pet(pet)
        elif choice == "2":
            bath_pet(pet)
        elif choice == "3":
            sleep_pet(pet)
        elif choice == "4":
            play_pet(pet)
        elif choice == "5":
            bark_pet(pet)
        elif choice == "6":
            status_of_pet(pet)
        elif choice == "7" :   
            print("goodbye")
            break
        else:
            print("invalid choice")
            
main()
        