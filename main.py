from smartscan_registration_module import create_qr_code, register_user_from_qr, user_storage

# Define lambda functions for in-memory operations
create_user, add_user, get_users = lambda name, email, gender: {"name": name, "email": email, "gender": gender}, lambda user: user_storage.append(user), lambda: user_storage

# Display existing users
print("Current users in the in-memory database:")
existing_users = get_users()
if existing_users:
    for user in existing_users:
        print(f"Name: {user['name']}, Email: {user['email']}, Gender: {user['gender']}")
else:
    print("No users found.")

# Direct entry of new user details
print("\nEnter details to add a user directly:")
user_name = input("Name: ")
user_email = input("Email: ")
user_gender = input("Gender: ")

# Add user data to in-memory storage
new_user = create_user(user_name, user_email, user_gender)
add_user(new_user)

# Show updated user list
print("\nUpdated users in the in-memory database:")
updated_users = get_users()
for user in updated_users:
    print(f"Name: {user['name']}, Email: {user['email']}, Gender: {user['gender']}")

# Details for QR code generation
print("\nEnter details to generate a QR code:")
qr_name = input("Name: ")
qr_email = input("Email: ")
qr_gender = input("Gender: ")

# Filename for QR code
file_name = input("Enter the QR code filename (e.g., 'user_qr.png'): ")
if not file_name.lower().endswith(".png"):
    print("Filename should end with '.png'. Appending '.png' to the filename.")
    file_name += ".png"

# Generate QR code with provided details
create_qr_code(qr_name, qr_email, qr_gender, file_name)

# Register user from the generated QR code
print("\nRegistering user from the QR code...\n")
register_user_from_qr(file_name, create_user, add_user, get_users)
final_users = get_users()
for user in final_users:
    print(f"Name: {user['name']}, Email: {user['email']}, Gender: {user['gender']}")