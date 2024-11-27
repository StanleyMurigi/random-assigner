import random
import os

def get_names():
    """Get names from the user."""
    print("Enter names (one per line). Type 'done' when finished:")
    names = []
    while True:
        name = input("Name: ").strip()
        if name.lower() == 'done':
            break
        if name:  # Ensure no empty names are added
            names.append(name)
    return names

def assign_numbers(names):
    """Randomly assign unique numbers to names."""
    numbers = list(range(1, len(names) + 1))
    random.shuffle(numbers)
    return {name: number for name, number in zip(names, numbers)}

def save_assignments(assignments, filename="assignments.txt"):
    """Save assignments to a file."""
    with open(filename, "w") as file:
        for name, number in assignments.items():
            file.write(f"{name} -> {number}\n")
    print(f"Assignments saved to {filename}")

def load_previous_assignments(filename="assignments.txt"):
    """Load previous assignments if the file exists."""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            print("Previous Assignments:")
            print(file.read())
    else:
        print("No previous assignments found.")

def main():
    print("Welcome to the Random Number Assigner!")
    
    # Check if there are previous assignments
    load_previous_assignments()
    
    # Get names from the user
    names = get_names()
    if not names:
        print("No names entered. Exiting.")
        return
    
    # Assign numbers
    assignments = assign_numbers(names)
    
    # Display the assignments
    print("\nRandom Assignments:")
    for name, number in assignments.items():
        print(f"{name} -> {number}")
    
    # Save the assignments
    save_assignments(assignments)

if __name__ == "__main__":
    main()

