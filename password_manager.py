import re


def check_password_strength(password):
    # Check for minimum length
    if len(password) < 8:
        return "Password too short! Must be at least 8 characters."

    # Check for both letters and numbers
    if not re.search(r"[A-Za-z]", password):
        return "Password must contain letters."
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one number."

    # Check for special characters
    if not re.search(r"[@$!%*#?&]", password):
        return "Password must contain at least one special character (@, $, !, %, *, etc.)."

    return "Password is strong!"

# Function to store the password


def store_password(service, username, password):
    with open("passwords.txt", "a") as file:
        file.write(f"{service}: {username}, {password}\n")
    print(f"Password for {service} saved successfully!")

# Function to retrieve the password for a specific service


def retrieve_password(service):
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                stored_service, details = line.split(": ")
                if stored_service == service:
                    username, password = details.strip().split(", ")
                    print(
                        f"Service: {service}\nUsername: {username}\nPassword: {password}")
                    return
        print(f"No password found for {service}")
    except FileNotFoundError:
        print("No passwords stored yet.")


if __name__ == "__main__":
    while True:
        print("\nPassword Manager")
        print("1. Store a new password")
        print("2. Retrieve a password")
        print("3. Check password strength")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            service = input("Enter the service (e.g., Gmail): ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            store_password(service, username, password)

        elif choice == "2":
            service = input("Enter the service to retrieve password: ")
            retrieve_password(service)

        elif choice == "3":
            password = input("Enter a password to check strength: ")
            result = check_password_strength(password)
            print(result)

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid option, please try again.")