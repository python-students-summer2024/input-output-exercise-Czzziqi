"""
A little assignment to practice receiving text input from the user in Python programming.
Do not run this file... run main.py instead.
"""


def get_favorite_vegetable():
    """
    Asks the user to enter their favorite vegetable
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite vegetable.
    """
    # write your code here.
    favorite_vegetable=input("what's your favorite vegatable? ")
    output_message = "Interesting! I also love "+ favorite_vegetable + "!"
    print(output_message)

def get_favorite_number():
    """
    Asks the user to enter their favorite number
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite number.
    """
    # write your code here.
    Favorite_number=input("what's your favorite number? ")
    output_message_number="Interesting! I also love "+ Favorite_number + "!"
    print(output_message_number)

def get_name_and_zodiac_sign():
    """
    Asks the user to enter their name.
    Then ask them to enter their zodiac sign.
    Then print out, "Interesting! My name is also X, and I'm also a Y!",
    where X and Y are replaced by the user's name and zodiac sign, respectively.
    """
    # write your code here.
    name=input("what's your name? ")
    zodiac_sign=input("what's your zodiac sign? ")
    output_message_name_zodiac="Interesting! My name is also " + name + ", and I'm also a " + zodiac_sign + "!"
    print(output_message_name_zodiac)

def get_name_and_age():
    """
    Asks the user to enter their name.
    Then ask them to enter their age.
    Then print out, "Interesting! My name is also X, and I'm also Y years old!",
    where X and Y are replaced by the user's name and age, respectively.
    """
    # write your code here.
    name_2=input("what's your name? ")
    age=input("How old are you? ")
    output_message_name_age="Interesting! My name is also " + name_2 + ", and I'm also " + age + " years old!"
    print(output_message_name_age)