users = {
    "Aryan":"aryan@123",
    "Jay":"jay@123"
    
}
username_attempts = 3
while username_attempts >0 :
    username = input("Username:")
    if username in users:
        break
        
    else:
        username_attempts-=1
        if username_attempts > 0:
            print(f"Invalid username. Try again. Attempts left:{username_attempts}")
        else:
            print("Login failed. No more attempts left")
            exit()

password_attempts = 3
while password_attempts>0:
    password = input("Password:")
    if users[username] == password:
        print("Login successful, Welcome back", username)
        break
    else:
        password_attempts-=1
        if password_attempts > 0:
            print(f"Incorrect password. Attempts remaining:{password_attempts}")
        else:
            print("Login failed. No more attempts left")
            



