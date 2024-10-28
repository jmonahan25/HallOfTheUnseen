# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sp = Character("Front Desk Worker")

define cr = Character("Laura")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg dormroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "You're reporting for another day of being an RA, but you have to pick up a new badge."

    python:
        name = renpy.input("What's your name again?")
        name = name.strip() or "Jake Statefarm"

    define yn = Character("[name]")

    show sponge happy

    # These display lines of dialogue.

    sp "How can I help you?"

    yn "Hey, I'm here to get that annoying ass duty phone, and pick up my new badge."

    sp "Alriiight, here you go! Good luck, it's thirsty thursday!"

    hide sponge happy

    "It was a typical September Thursday."

    "The nights had started to become cooler and packs of freshman stood by the front door anxiously waiting for that one friend who's always late."

    "The sickeningly sweet smell of pink whitney fills your nose."

    define vb = Character("Voice behind you")

    vb "Welp, guess we're gonna be calling paramedics tonight"

    show courage happy

    "You turn and see Laura (your duty partner for the night)"

    yn "Don't jinx us! I heard on Saturday they had to call the paramedics 6 times because some fratboys were so mad we lost the game that they decided to mix whisky and vodka and then ate an edible."

    cr "I will never understand freshmen. It's like they're constantly trying to make a new level on dumb ways to die."

    "You and Laura start your rounds and simataneously hear 4 sounds coming from opposite directions."

    # This ends the game.

    return
