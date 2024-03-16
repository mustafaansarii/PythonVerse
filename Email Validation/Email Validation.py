import gradio as gr

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
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

        return True

    def get_valid_email(self, email):
        if self.validate_email(email):
            self.email = email
            return "Email is valid."
        else:
            return "Wrong email format. Please enter a valid email."

validator = EmailValidator()

input_email = gr.Textbox(label="Enter Your Email:")
output_text = gr.Textbox(label="Validation Result")

interface = gr.Interface(fn=validator.get_valid_email, inputs=input_email, outputs=output_text, title="Email Validator", description="Validate an email address.")

if __name__ == "__main__":
    interface.launch()
