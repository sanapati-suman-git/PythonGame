import random
word_bank = [
    'bubblegum', 'rainbow', 'unicorn', 'popsicle', 'jellybean',
    'cupcake', 'sunshine', 'whistle', 'fireworks', 'scooter',
    'honeybee', 'sprinkles', 'doodle', 'marshmallow', 'giggle',
    'lollipop', 'penguin', 'balloon', 'confetti', 'snuggle']

while True:
  word=random.choice(word_bank)
  guessedword=['_']*len(word)
  attempts=10
  doc=input('Are you ready to play (True/false): ').lower().strip()
  level=input("Enter the difficulty level(Easy -12/Medium -10/Hard -6) : ").lower().strip()
  if doc=='true':
    if level=='easy':
      attempts=12
    elif level=='medium':
      attempts=10
    elif level=='hard':
      attempts=6
    print('\nlet begin the game .....\n')
    while attempts>0:
      print('Current word: '+' '.join(guessedword))
      guess=input('Guess a letter: ').lower()
      if guess in word:
        for i in range(len(word)):
          if word[i]==guess:
            guessedword[i]=guess
        print('Great Guess!')
      else:
        attempts-=1
        print("Try again ! Atttempts left: "+str(attempts))
      if '_' not in guessedword:
        print('Congratualation !! you guesseed it right the word: '+word)
        break
    if attempts==0 and '_' in guessedword:
      print('You have run out of attempts ! the word was: '+word +'\nTry again...')
  else:
    print("See you soon...")

  play_again=input("Do you want to play again : ").lower().strip()
  if play_again!='true':
    break