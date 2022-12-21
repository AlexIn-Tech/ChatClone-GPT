# **ChatClone-GPT**

**ChatClone-GPT** is a Proof Of Concept to learn how to use OpenAI API and Django in order to create a chatbot powered by the GPT API from OpenAI. It uses the GPT-3 natural language processing model to generate human-like responses to user input. I was inspired by the "ChatGPT" project from OpenAI and I was wondering how to create my own. 

Disclaimer : It's my first ever project using Django, so I may have done things wrong. sorry. 

## **Requirements**

- Python 3.6 or higher
- Django 2.0 or higher
- openai (Python library)
- An OpenAI API key (sign up at **[https://beta.openai.com/](https://beta.openai.com/)**) => and you need a payment method because it costs money to use it. 

## **How to create your own ChatClone-GPT**

1. Install the required libraries:
   
    ```python
    pip install django openai
    ```
    
2. Create your own Django app
   

Once you have Django installed, you can use the **`django-admin`** command-line utility to create a new project. Open a terminal window and navigate to the directory where you want to create your project, then run the following command:

```python
django-admin startproject GPT
```

This will create a new Django project with the name **`GPT`** in the current directory.

Next, you can create a new app within the project by running the following command:

```python
python manage.py startapp ChatClone
```

This will create a new app with the name **`ChatClone`** within the **`GPT`** project.

3. Now you can copy the needed files from my project and replace them in your project. 

Here are the needed folders/files : 
- GPT\ChatClone\templates
- GPT\ChatClone\templates\chat.html
- GPT\ChatClone\templates\index.html
- GPT\ChatClone\forms.py
- GPT\ChatClone\urls.py
- GPT\ChatClone\views.py
- GPT\GPT\urls.py

And then in this file you will have to just copy and replace a part : GPT\GPT\settings.py

replace in TEMPLATES : 
    ```python
    'DIRS': [],
     #replace it by 
	'DIRS': ['ChatClone\\templates',],
    ```

Do not copy and replace your file settings.py by mine. I removed my SECRET_KEY in mine. 

1. Run the Django development server:

    ```python
    python manage.py runserver
    ```

2. Open your web browser and go to **[http://localhost:8000/chat](http://localhost:8000/chat)** to start using **ChatClone-GPT**.

![ChatClone-GPT](screenshot\ChatClone-GPT.png)

## **Tips**

- You can customize the behavior of **ChatClone-GPT** by adjusting the parameters of the **`openai.Completion.create()`** function in the **`chat`** view. For example, you can change the **`temperature`** parameter to control the randomness of the generated responses.
- The "max_tokens" property in the views.py set the quantity of words & punctuations generated. Max value is either 2048 or 4096 depending of the model used.

## **Go Further**

- My CSS is awful, do not hesitate to do waaaaayyy better. 
- ChatClone-GPT** is just a basic example of what you can do with the GPT API and Python. There are many other ways you can customize and extend the chatbot, such as by adding additional functionality or integrating it with other services.
- You can learn more about the GPT API and other OpenAI models by visiting the OpenAI documentation page at **[https://beta.openai.com/docs](https://beta.openai.com/docs)**.

## **License**

**ChatClone-GPT** is released under the MIT License. You are free to use, modify, and distribute this program as long as you include the original copyright and license notice.