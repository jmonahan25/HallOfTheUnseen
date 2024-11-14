# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define fd = Character("Front Desk Worker")

define lr = Character("Laura")

transform half_size:
    zoom 0.5 #adjust as needed

transform quarter_size:
    xpos 500
    ypos -100
    zoom 0.3 #adjust as needed

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

    show bodhi wave at quarter_size

    # These display lines of dialogue.

    fd "How can I help you?"

    hide bodhi wave

    show bodhi neutral

    yn "Hey, I'm here to get that annoying ass duty phone, and pick up my new badge."

    hide bodhi neutral

    show bodhi wave at quarter_size

    fd "Alriiight, here you go! Good luck, it's thirsty thursday!"

    hide bodhi wave

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

    menu:
        "Go towards the scream":
            jump scream_path

        "Go towards the crash":
            jump crash_path

    label scream_path:
        show laura nervous at double_size

        lr "Oh shit where should we go?"

        yn "To the scream! We need to make sure they're ok"

        hide laura nervous

        scene bg hallway at half_size

        "You run towards the scream and see a group of residents crowded outside room 219"

        define bd = Character("Resident")

        show bodhi scared

        bd "Oh thank god the House Fellows are here! Please help her!"

        hide bodhi scared

        show laura talk at double_size

        lr "Don't worry, we got you, what's the problem?"

        hide laura talk

        show laura surprised at double_size

        "Laura stops in the middle of her sentence and her eyes widen"

        hide laura surprised

        scene bg dorm body at half_size

        play music "dark_ambient.mp3" fadeout 1

        ""

        define v1 = Character("Dying Student")

        menu:
            "Immediately call 911":
                jump scream_911

            "Try to help the student":
                jump scream_help

            "Stand in shock":
                jump scream_shock

        label scream_911:
            "The paramedics arrive and take away the student's body. It is soon discovered that this wasn't a freak accident. It was a homicide."

            jump done

        label scream_help:
            "You run over to the student's body and begin to try and give CPR"

            "The student slowly opens their eyes"

            v1 "This is your fault..."

            yn "What the fuck are you talking about?!"

            "The resident dies in your arms, leaving you confused and waiting for the paramedics"

            "The only thing you know is this is somehow connected to you"

            jump done

        label scream_shock:
            "The residents watch you standing in shock and grow increasingly frustrated"

            show bodhi angry

            bd "Why aren't you doing something?!"

            yn "Shi! I'm sorry, Laura I'll call 911!"

            hide bodhi angry

            "The residents watch you call 911 but now look at you with a suspicious gaze"

            jump done

        jump done

    label crash_path:
        scene bg laundry at half_size

        lr "Now we are in the laundry room"

        jump done

    label done:
        stop music fadeout 1

        "To be continued..."

    # This ends the game.

    return
