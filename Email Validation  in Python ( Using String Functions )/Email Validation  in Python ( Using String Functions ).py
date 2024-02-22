class EmailValidator:
    def __init__(self):
        self.email = ""

    def validate_email(self, email):
        j, k, d = 0, 0, 0

        if len(email) >= 6:
            if email[0].isalpha():
                if "@" in email and email.count("@") == 1:
                    if (email[-4] == "." or email[-3] == "."):
                        for i in email:
                            if i.isspace():
                                k = 1
                            elif i.isalpha():
                                if i == i.upper():
                                    j = 1
                            elif i.isdigit():
                                continue
                            elif i == "_" or i == "." or i == "@":
                                continue
                            else:
                                d = 1
                        if k == 1 or j == 1 or d == 1:
                            print("Wrong email format. Please enter a valid email.")
                            return False
                    else:
                        print("Wrong email format. Please enter a valid email.")
                        return False
                else:
                    print("Wrong email format. Please enter a valid email.")
                    return False
            else:
                print("Wrong email format. Please enter a valid email.")
                return False
        else:
            print("Wrong email format. Please enter a valid email.")
            return False

        return True

    def get_valid_email(self):
        while True:
            email = input("Enter your email: ")
            if self.validate_email(email):
                self.email = email
                print("Email is valid.")
                break

validator = EmailValidator()
validator.get_valid_email()
print("Validated email:", validator.email)
