import random
losowy = random.randint(1,100)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
guesses = [0]
while True:
    
    #kod zeby proba byla uznawana jako int i pytanie z polem do wpisania, odrzucenie randomu)
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    
    #porownanie proby do wylosowanego numeru
    if guess == losowy:
        print(f"Congratulations, you guessed it in only {len(guesses)} guesses!")
        break
        
    #jesli proba nie byla udana, dodaj do listy prób
    guesses.append(guess)
    if guesses[-2]:  
        if abs(losowy-guess) < abs(losowy-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(losowy-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
            
input("Koniec gry, utkay")