# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define fd = Character("Front Desk Worker")

define lr = Character("Laura")

define PKFlag = False

define SPacket = False
define CPhone = False

transform half_size:
    xpos 100
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

        #"Go towards the crash":
            #jump crash_path

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

        transform half_size_down:
            xpos 100
            ypos -200
            zoom 0.5 #adjust as needed

        scene bg dorm body at half_size_down

        play music "dark_ambient.mp3" fadeout 1

        ""

        define v1 = Character("Dying Student")

        menu:
            "Immediately call 911":
                "The paramedics arrive and take away the student's body. It is soon discovered that this wasn't a freak accident. It was a homicide."

                jump sc_investigate

            "Try to help the student":
                jump scream_help

            "Stand in shock":
                jump scream_shock

        label scream_help:
            "You run over to the student's body and begin to try and give CPR"

            "The student slowly opens their eyes"

            v1 "This is your fault..."

            yn "What the fuck are you talking about?!"

            "The resident dies in your arms, leaving you confused and waiting for the paramedics"

            "The only thing you know is this is somehow connected to you"

            jump sc_investigate

        label scream_shock:
            "The residents watch you standing in shock and grow increasingly frustrated"

            show bodhi angry

            bd "Why aren't you doing something?!"

            yn "Shi! I'm sorry, Laura I'll call 911!"

            hide bodhi angry

            "The residents watch you call 911 but now look at you with a suspicious gaze"

            jump sc_investigate

    label sc_investigate:
        "You notice that a small crowd has formed around the scene and you realize you should start investigating and questioning witnesses"

        menu:
            "Question witness 1":
                define w1 = Character("Witness 1")

                w1 "I was just walking in one of the hallways when I heard a loud explosion and a scream coming from this room"

                w1 "I ran over to the noise and saw 'Yandere' running away, I assumed she'd be getting some help. I got to the room and
                    saw Towi on the ground. I couldn't help but scream."

                jump sc_i_2
            "Question witness 2":
                define w2 = Character("Witness 2")

                w2 "I was in my dorm room when I heard an explosion, then I heard someone scream"
            
                w2 "I opened my door to see smoke in the hallway, and I saw you and Laura"

                w2 "You look familiar though, weren't you at Tori's dorm last night?"

                jump sc_i_2
            "Inspect the microwave":
                "You find traces of an explosive powder hidden inside the seasoning packet, and it smells like burnt sulfur."

                "{i}Seasoning Packet added to inventory!{/i}"

                $ SPacket = True

                jump sc_i_2
            "Examine the body":
                menu:
                    "Check Upper Body":
                        "There was blood running down her forehead and her head seemed bashed-in"
                        jump sc_i_2
                    "Check Lower Body":
                        "You see slight burn marks on the body, and noodles splattered around"
                        "You notice something in the victim's pocket. Reaching in you pull out a cell phone"
                        "The screen is cracked and a bunch of instagram messaged from Yandere fill the screen"
                        "{i}Cracked Phone added to inventory!{/i}"
                        $ CPhone = True
                        jump sc_i_2

    label sc_i_2:

        "Alerted by all the commotion, a third resident arrives in the door and lets out a scream upon seeing the body"

        "You realize that as an RA, you probably need to talk to them and manage the situation"

        define w3 = Character("Witness 3")

        menu:
            "Be Reassuring":
                yn "I understand ... it's a lot to take in. But anything you can tell us might really help. I promise we'll keep this confidential."
                w3 "I... I just don't want any trouble. I'm not involved with this"
                jump sc_i_3
            "Be Direct":
                yn "Look, we need to know exactly what's going on here. Any details, big or small, could make a difference."
                w3 "I had nothing to do with this!"
                jump sc_i_3
        label sc_i_3:
            "You realize that a small crowd is starting to form in the hallway"
            menu:
                "Continue questioning witness 3":
                    menu:
                        "Ask about anything unusual":
                            yn "Did you notice anything unusual around the time of the scream? Any strange sounds, or anyone acting suspicious?"
                            w3 "I was just studying in my room when I heard something that sounded like a pop or a small explosion."
                            w3 "At first, I thought maybe someone dropped something heavy or, like, something weird with the microwave."
                            jump sc_i_3
                        "Ask about people in the hallway":
                            yn "Who did you see out here? Did anyone else come by before the scream?"
                            w3 "I saw Yandere hanging around in the hallway last night. She was sort of loitering by Tori's door. I didn't think much of it at first-but it was kinda odd since she's always usually at B Tower"
                            jump sc_i_3
                        "Ask about the smell":
                            yn "Do you remember smelling anything weird around the time this happened? It's just that... there's this burning smell lingering in the hallway now."
                            w3 "You mean, like, burning sulfur?  If that's important... I think I smelled it down in the laundry room last night."
                            w3 "Could someone have been using something down there? It didn't seem like just burnt food."
                            jump sc_i_3
                "Address the hallway":
                    "You turn towards the crowd, full of murmers of fear and curiosity"
                    yn "Alright everyone, get back to your rooms!"
                    "The crowd slowly dissapates as people return to their dorms"
                    "You and Laura glance around, taking in the damage from the explosion."
                    "There's debris scattered everywhere: fragments of ceramic from the microwave, charred bits of paper, and what might have once been part of a notebook."
                    lr "You smell that? It's not just burnt noodles. It smells... chemical"
                    yn "Yeah. Something isn't right. Let's look around; it might tell us more about what happened."
                    "Among the scattered debris, your eye lands on something"
                    yn "What's this?"
                    menu:
                        "Pick up note":
                            "You pick up a charred and crumpled note. You're barely able to make out the words"
                            define no = Character("Charred note")
                            no "{i}You don't deserve him{/i}"
                            jump done
                        "Pick up broken Wii Remote":
                            "Your foot nudges something small and plastic. You look down and see a cracked, burnt Wii remote, partially melted at one end."
                            "{i}Burnt Wii Remote added to inventory!{/i}"
                            jump done
        jump done

    label crash_path:
        show laura nervous at double_size

        lr "Oh shit where should we go?"

        yn "To the crash! We need to figure out what the hell made that sound!"

        hide laura nervous



        jump done

    label done:
        stop music fadeout 1

        "To be continued..."

    # This ends the game.

    return
