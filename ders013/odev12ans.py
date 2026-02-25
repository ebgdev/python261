def set_password():
    while True:
        pass1 = input("Enter your password: ")
        
        if pass1.lower() == "exit":
            print("Process cancelled.")
            return None
        
        pass2 = input("Confirm your password: ")
        
        if pass2.lower() == "exit":
            print("Process cancelled.")
            return None

        # Boş kontrolü
        if not pass1 or not pass2:
            print("Passwords cannot be blank.\n")
            continue

        # Eşleşme kontrolü
        if pass1 != pass2:
            print("Passwords do not match. Try again.\n")
            continue

        # Uzunluk kontrolü
        if len(pass1) < 8:
            print("Password must be at least 8 characters long.\n")
            continue

        # Rakam kontrolü
        has_digit = False
        for ch in pass1:
            if "0" <= ch <= "9":
                has_digit = True

        if not has_digit:
            print("Password must contain at least one digit.\n")
            continue

        # Büyük harf kontrolü
        has_upper = False
        for ch in pass1:
            if "A" <= ch <= "Z":
                has_upper = True

        if not has_upper:
            print("Password must contain at least one uppercase letter.\n")
            continue

        print("Congrats, password set successfully!")
        return pass1