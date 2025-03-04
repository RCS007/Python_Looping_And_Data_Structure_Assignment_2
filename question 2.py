# Question 2

# Ask the user to enter the name, age and shoe size for four people.

# • Ask for the name of one of the people in the list and display their age and shoe size.
# • Display the names and ages of all the people in the list but do not show their shoe size.
# • After gathering the four names, ages and shoe sizes, ask the user to enter the name of the person they
# want to remove from the list. Delete this row from the data and display the other rows on separate
# lines.

# Create an empty list to store people data
people_data = []

# Gather information for four people
for _ in range(4):
    name = input("Enter the name: ")
    age = int(input(f"Enter the age of {name}: "))
    shoe_size = float(input(f"Enter the shoe size of {name}: "))
    people_data.append({"name": name, "age": age, "shoe_size": shoe_size})

# Ask for the name of a person and display their age and shoe size
search_name = input("Enter the name of the person to search for: ")
found = False
for person in people_data:
    if person["name"].lower() == search_name.lower():
        print(f"{person['name']} - Age: {person['age']}, Shoe Size: {person['shoe_size']}")
        found = True
        break

if not found:
    print(f"Person with name {search_name} not found.")

# Display names and ages of all the people (without shoe size)
print("\nNames and Ages of all people:")
for person in people_data:
    print(f"{person['name']} - Age: {person['age']}")

# Ask the user for the name of the person they want to remove
remove_name = input("\nEnter the name of the person you want to remove: ")
people_data = [person for person in people_data if person["name"].lower() != remove_name.lower()]

# Display the remaining data
print("\nRemaining people after removal:")
for person in people_data:
    print(f"{person['name']} - Age: {person['age']}")
