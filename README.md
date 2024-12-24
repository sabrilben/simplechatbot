# ChatMate!

Welcome to ChatMate, a simple chatbot powered by DialoGPT model and Gradio interface. This project showcases a simple chatbot that can engage in conversations and perform basic arithmetic calculations.

## Features

- **Conversational AI**: ChatMate uses the DialoGPT model to generate human-like responses.
- **Arithmetic Calculations**: ChatMate can perform basic arithmetic operations like addition, subtraction, multiplication, division, exponentiation, floor division, and modulus.
- **User-Friendly Interface**: Built with Gradio, ChatMate provides an easy-to-use interface for interacting with the chatbot.

## How to Use

1. **Open the chatbot**.
2. **Type anything** in the **Question** box (e.g., 'hello', 'What is AI?', 'calculate 9 * 7', 'bye', etc.).
3. **For calculations**, use the following operators:
    - `+` for addition
    - `-` for subtraction
    - `*` for multiplication
    - `/` for division
    - `**` for exponentiation
    - `//` for floor division
    - `%` for modulus
4. **Press 'Enter'** or click the **'Submit'** button.

The chatbot will respond to your queries.

## Code Explanation

Here's a brief explanation of what the code does:

1. **Imports**: The necessary libraries (`gradio`, `transformers`, and `torch`) are imported.
2. **Model and Tokenizer**: The DialoGPT model and tokenizer are loaded using the `transformers` library.
3. **Conversation History**: Variables to store the conversation history and interaction count are initialized.
4. **Helper Function**: A helper function `is_float` is defined to check if a value can be converted to a float.
5. **Chatbot Response Function**: The `chatbot_response` function handles user inputs, generates responses, and manages the conversation history.
    - **Reset History**: The conversation history is reset after every 5 interactions.
    - **Arithmetic Calculations**: If the input starts with 'calculate', the function performs the specified arithmetic operation.
    - **Predefined Responses**: The function provides predefined responses for 'hello' and 'bye'.
    - **Model Response**: For other inputs, the function generates a response using the DialoGPT model.
6. **Gradio Interface**: The Gradio interface is set up to provide a user-friendly way to interact with the chatbot.

## Installation

To run this project, you'll need to install several libraries. Just make sure you have the requirements.txt and run this code in terminal:

```bash
pip install -r requirements.txt
```

## Running the Chatbot

To run the chatbot, execute the simplechatbot.py script. This will launch the Gradio interface, allowing you to interact with ChatMate.

```bash
python simplechatbot.py
```

## Conclusion
ChatMate is a fun and engaging project that demonstrates the capabilities of conversational AI using DialoGPT and Gradio. Feel free to explore and enhance the chatbot to suit your needs.

If you have any questions or feedback, feel free to reach out.
