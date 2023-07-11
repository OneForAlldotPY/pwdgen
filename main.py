from Generator import generate_pwd, hash_pwd, evaluate_password_strength

def main():
     while True:
        user_password_length = int(input("Input the number of digits for the password: "))
        generated_password = generate_pwd(user_password_length)
        hashed_password = hash_pwd(generated_password)
        password_strength = evaluate_password_strength(generated_password)

        print("Generated Password: ", generated_password)
        print("Hashed Password: ", hashed_password)
        print("Password Strength: ", password_strength)

        restart = input("Press R to restart or press Enter to exit: ")
        if restart.lower() != "r":
            break

if __name__ == "__main__":
    main()