import random
import string
import gradio as gr

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def password_generator(length):
    if length <= 0:
        return "Please enter a valid number for the password length."
    else:
        return generate_password(length)

input_number = gr.Number(label="Enter the desired length of the password:")
output_text = gr.Textbox(label="Generated Password:")

interface = gr.Interface(fn=password_generator, inputs=input_number, outputs=output_text, title="Password Generator", description="Generate a random password of specified length.")

if __name__ == "__main__":
    interface.launch(share=True)
