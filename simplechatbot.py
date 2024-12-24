"""
SimpleChatbot.ipynb

Automatically generated by Colab.

Original file is located at
https://colab.research.google.com/drive/1cTTEQkYDKIHR24L7vlEdEMEWP-JT6UFg?usp=sharing

"""

import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the Hugging Face model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

conversation_history = []
conversation = None
interaction_count = 0

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def chatbot_response(prompt):
    global conversation_history
    global conversation
    global interaction_count

    # Reset conversation history after every 5 interactions
    if interaction_count >= 5:
        conversation_history = []
        conversation = None
        interaction_count = 0

    lines = prompt.splitlines()

    if len(lines) > 1:
        response = "Please only input 1 line per prompt."
    elif len(lines) == 1 and prompt.lower().startswith('calculate '): # "calculate" in prompt.lower():
        calculation = prompt.lower().lstrip("calculate ")
        component = calculation.split()
        if len(component) == 3:
            num1, operator, num2 = component
            if is_float(num1) == True and is_float(num2) == True and operator in ['+', '-', '*', '/', '**', '//', '%']:
                num1 = float(num1)
                num2 = float(num2)

                if operator == '+':
                    result = num1 + num2
                    response = f"The result is {result}"
                elif operator == '-':
                    result = num1 - num2
                    response = f"The result is {result}"
                elif operator == '*':
                    result = num1 * num2
                    response = f"The result is {result}"
                elif operator == '**':
                    result = num1 ** num2
                    response = f"The result is {result}"
                elif operator == '%':
                    result = num1 % num2
                    response = f"The result is {result}"
                elif operator == '/':
                    if num2 != 0:
                        result = num1 / num2
                        response = f"The result is {result}"
                    else:
                        response = "Error: Division by zero"
                elif operator == '//':
                    if num2 != 0:
                        result = num1 // num2
                        response = f"The result is {result}"
                    else:
                        response = "Error: Division by zero"
            else:
                response = "Invalid operator and/or calculation format. Please use 'calculate <num1> <operator> <num2>"
        else:
            response = "Invalid operator and/or calculation format. Please use 'calculate <num1> <operator> <num2>"
    elif len(lines) == 1 and prompt.lower() == "hello":
        response = "Hi there! How can I help you today?"
    elif len(lines) == 1 and prompt.lower() == "bye":
        response = "Goodbye! Have a great day!"
    else:
        # Encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')

        # Append the new user input tokens to the chat history
        if conversation is not None:
            bot_input_ids = torch.cat([conversation, new_user_input_ids], dim=-1)
        else:
            bot_input_ids = new_user_input_ids

        # Generate a response while limiting the total chat history to 1000 tokens
        conversation = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

        # Decode the response
        response = tokenizer.decode(conversation[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

    # Update conversation history
    conversation_history.append(f"Q: {prompt}")
    conversation_history.append(f"A: {response}")

    # Increment interaction count
    interaction_count += 1

    history = "\n".join(conversation_history[-6:])  # Show last 3 interactions (Q&A pairs)

    return history

desc = "Your friendly chatbot powered by DialoGPT and Gradio. Let's chat! (pleasee.. 🥲)."

article = "<h3>How to Use:</h3> " \
          "<ol><li>Open the chatbot.</li> " \
          "<li>Type anything in the <strong>Question</strong> box (e.g., 'hello', 'What is AI?', 'calculate 9 * 7', 'bye', etc.).</li>" \
          "<li>For calculations, use the following operators:" \
          "<ul><li>+ for addition</li>" \
          "<li>- for subtraction</li>" \
          "<li>* for multiplication</li>" \
          "<li>/ for division</li>" \
          "<li>** for exponentiation</li>" \
          "<li>// for floor division</li>" \
          "<li>% for modulus</li></ul></li>" \
          "<li>Press 'Enter' or click the 'Submit' button.</li></ol>" \
          "<h5>The chatbot will respond to your queries.</h5>"

demo = gr.Interface(fn=chatbot_response,
                    inputs=gr.Textbox(label="User", placeholder="Say something pleaseee..."),
                    outputs=gr.Textbox(label="Conversation"),
                    title="ChatMate!",
                    description=desc,
                    article=article,
                    theme='allenai/gradio-theme').launch()