# Jeleah McLean
#CIS 261 
# Country Lab 

def display_menu():
    print("command menu")
    print("view --> view country name")
    print("add --> Add a (country")
    print("delete --> delete a (country")
    print("exit --> Exit the program")
    print()
    
def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_lines = "country codes: "
    for code in codes:
        codes_line += code + " "
        print(codes_lines)
        
def view(countries):
    codes = input (" Enter country code: ")
    code = code.upper
    if code in countries:
        name = countries [code]
        print(f" country name: {name}. \n")
    else:
        print("There is no country with that code. \n ")
        
def add(countries):
    code = input("Enter country code: ")
    code = code. upper()
    if code in countries:
        name = countries [code]
        print(f"{name} is already using that code")
    else:
        name = input("enter country name:")
        name = name.title()
        countries [code] = name
        print(f"(name) was added . \n")
        
def delete(countries):
    code = input(" enter country code: ")
    code = code.upper()
    if code in countries:
        name =countries.pop(code)
        print(f"{name} was deleted ")
    else:
        print(" there is no country with that code.\n ")
        
def main():
    countries = {"AF": "Afghanistan", "DE": "Germany", "CA": "Canada" }

    display_menu()
    while True:
        command = input("command: ")
        command = command.lower()
        if  command == "view":
            view(countries)
        elif command == "add":
            add(countries)
        elif command == "delete":
            delete (countries)
        elif command == "exit":
            print("Bye")
            break
        else:
            print("not a valid commandd, please try again.\n")
            
if __name__ == "__main__":
    main()
    
        
