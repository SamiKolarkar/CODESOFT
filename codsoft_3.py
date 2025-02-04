import random
import string
def generate():
    length=int(input(">Please enter the length of password:"))
    password=""
    letters=string.ascii_letters
    uppercase_letters=string.ascii_uppercase
    digits=string.digits
    specialchars=string.punctuation
    for i in range(length):
        character=random.choice(letters+uppercase_letters+digits+specialchars)
        password+=random.choice(character)
    print(f">Your password is:{password}")
if __name__=="__main__":
    generate()
