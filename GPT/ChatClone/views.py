from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

import openai

openai.api_key = "MY OPEN AI API KEY"

def chat(request):
    conversation = []  # Initialize the conversation history

    if request.method == "POST":
        # Get the user's message from the form submission
        message = request.POST["message"]
        conversation.append({"user": message})  # Add the user's message to the conversation history

        # Use the GPT API to generate a response
        model_engine = "text-davinci-002"
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=message,
            max_tokens=1024, # Quantity of words & punctuations generated. Max value is either 2048 or 4096 depending of the model used. 
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completion.choices[0].text
        conversation.append({"bot": response})  # Add the bot's response to the conversation history

        # Render the template with the generated response
        return render(request, "chat.html", {"conversation": conversation})

    else:
        # Render the template for the initial GET request
        return render(request, "chat.html")