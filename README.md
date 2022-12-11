# Questionnaire
Cloning the repository
--> Clone the repository using the command below :

git clone https://github.com/leraks/Questionnaire.git


--> Create a virtual environment :

# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname
--> Activate the virtual environment :

envname\scripts\activate
--> Install the requirements :

pip install -r requirements.txt


# Running the App
--> To run the App, we use :

python manage.py runserver <br>
⚠ Then, the development server will be started at http://127.0.0.1:8000/


# Task :
Web application for managing a database of bonus cards (loyalty cards, credit cards, etc. I have met many variations). List of fields: card series, card number, card issue date, end date of card activity, date of use, amount, card status (not activated/activated/expired).

The functionality of the application is a list of cards with fields: series, number, release date, end date of activity, status search for the same fields viewing the profile of the card with the purchase history of it activating/deactivating the card deleting the card

Implement a card generator, indicating the series and number of generated cards, as well as the "end date of activity" with the values "1 year", "6 months" and "1 month".

# Task Ru

Простой сервис проведения тестирования по каким-либо темам. Т.е. есть тесты с вариантами ответов, один или несколько вариантов должны быть правильными.
Тесты группируются в наборы тестов, которые затем пользователь может проходить и видеть свой результат.

Функциональные части сервиса:

Регистрация пользователей, Аутентификация пользователей , Зарегистрированные пользователи могут проходить любой из тестовых наборов

# App Preview :
![image](https://user-images.githubusercontent.com/67760549/206897116-3b000f12-ab58-4491-b1da-25d5bb705999.png)
![image](https://user-images.githubusercontent.com/67760549/206897183-cfc37b56-6903-4465-bd40-fec358806d2e.png)
![image](https://user-images.githubusercontent.com/67760549/206897211-c0658a74-fc1f-4b53-9bb3-0e52fa579917.png)

