# Open login.txt file in read mode
with open('login.txt', 'r') as login_file:
    # Read the entire content of the file
    login_data = login_file.read()
    print(login_data)

# Open registration.txt file in write mode
with open('registration.txt', 'w') as registration_file:
    # Write data to the file
    registration_file.write("User: John\n")
    registration_file.write("Email: john@example.com\n")

# Open registration.txt file in append mode
with open('registration.txt', 'a') as registration_file:
    # Append data to the file
    registration_file.write("User: Alice\n")
    registration_file.write("Email: alice@example.com\n")



with open ('login.txt', 'r') as login_file:
    login_data = login_file.read()

with open ('registration.txt', 'w') as registeration_file:
    registeration_file.write(login_data)

print("Content copied from loign.txt to registrarion.txt")

