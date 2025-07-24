import sys

# Method to choose the law and the contract snippet from a list
def choose_from_list(options):
    print("\nChoose:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(options):
                selected = options[choice - 1]
                return selected["law"], selected["text_snippet"]
            else:
                print("Invalid number")
        except ValueError:
            print("Enter a valid int")

# Method to ask a user if he wants to go ahead with law analisys
def ask_user_confirmation():
    response = input("You want to discover one of those laws? (yes/no): ").strip().lower()
    if response not in {"yes", "y"}:
        print("Exiting program.")
        sys.exit(0)

# Method to choose which kind of intervention the agents has to perform
def intervention_selection():
    print("\nSelect which kind of intervention to perform:")
    print("0 - Extract legal concepts")
    print("1 - Detect contradictions")
    print("2 - Assess legal risk")
    print("3 - Validate law citation")
    selected_intervention = input("Enter number (0-3): ")
    
    return selected_intervention