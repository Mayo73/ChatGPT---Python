import openai

# Setzen Sie Ihren OpenAI API-Schlüssel
# Set your OpenAI-Key
openai.api_key = 'YOUR API CODE' # Example: 'sk-rWwnK4TmP0bR4zbpnbYsKLAGbkFJ1UAcUnwBebIq8O5qb7B2' (This Code doesn't work!)

# Ihr Chatverlauf, beginnend mit einem Nutzerbeitrag
# Your Chathistory, beginning with a userinput
chat_history = []

while True:
    user_input = input("Sie: ")
    chat_history.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        # Ändere das "#" vor "model="gpt-3.5-turbo"" oder "model="gpt-4"" um das gewollte Modell zu wählen (gpt-3.5-turbo ist vorausgewählt)
        # Change the "#" in front of "model="gpt-3.5-turbo"" or "model="gpt-4"" to select the model you want to use (gpt-3.5-turbo is preselected)
        model="gpt-3.5-turbo",
        # model="gpt-4",
        messages=chat_history,
        max_tokens=1000  # Passen Sie dies an, um die Antwortlänge zu steuern / Adjust the number to control the response length
    )

    bot_reply = response['choices'][0]['message']['content']
    print("")
    print("Bot:", bot_reply)
    print("")
    chat_history.append({"role": "assistant", "content": bot_reply})
