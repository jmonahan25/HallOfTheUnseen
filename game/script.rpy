# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define fd = Character("Front Desk Worker")

define lr = Character("Laura")

transform half_size:
    zoom 0.5 #adjust as needed

transform double_size:
    zoom 2 #adjust as needed

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg desk at half_size

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "You're reporting for another day of being an RA, but you have to pick up a new badge."

    python:
        name = renpy.input("What's your name again?")
        name = name.strip() or "Jake Statefarm"

    define yn = Character("[name]")

    show guy talk at double_size

    # These display lines of dialogue.

    fd "How can I help you?"

    hide guy talk

    show guy smile at double_size

    yn "Hey, I'm here to get that annoying ass duty phone, and pick up my new badge."

    hide guy smile

    show guy talk at double_size

    fd "Alriiight, here you go! Good luck, it's thirsty thursday!"

    hide guy talk

    "It was a typical September Thursday."

    "The nights had started to become cooler and packs of freshman stood by the front door anxiously waiting for that one friend who's always late."

    "The sickeningly sweet smell of pink whitney fills your nose."

    define vb = Character("Voice behind you")

    vb "Welp, guess we're gonna be calling paramedics tonight"

    show laura smile at double_size

    "You turn and see Laura (your duty partner for the night)"

    yn "Don't jinx us! I heard on Saturday they had to call the paramedics 6 times because some fratboys were so mad we lost the game that they decided to mix whisky and vodka and then ate an edible."

    hide laura smile

    show laura talk at double_size
    
    lr "I will never understand freshmen. It's like they're constantly trying to make a new level on dumb ways to die."

    hide laura talk

    show laura smile at double_size

    "You and Laura start your rounds and simultaneously hear 4 sounds coming from opposite directions."

    hide laura smile

    "To be continued..."

    # This ends the game.

    return
