import random

def country_guessing_game():
    countries = ["usa", "canada", "brazil", "france", "japan", "australia", "india", "southafrica", "russia", "mexico","pakistan","palestine","qatar","iran"]
    
    # Choose a random country
    secret_country = random.choice(countries)
    
    print("Welcome to the Country Guessing Game!")
    print("I have selected a country. Can you figure out which one it is?")

    attempts = 0
    max_attempts = 4
    
    while attempts < max_attempts:
        # Get user input
        guess = input("Enter your guess: ").lower()
        
        # Increase the number of attempts
        attempts += 1
        
        # Check if the guess is correct
        if guess == secret_country:
            print(f"Great job! You successfully identified the country '{secret_country.capitalize()}' in just {attempts} attempts.")
            break

        else:
            print("Incorrect. Try again.")
    
    else:
        print(f"Unfortunately, you've exhausted all attempts. The correct country was '{secret_country.capitalize()}'.")
        

if __name__ == "__main__":
    country_guessing_game()
