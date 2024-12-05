# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define fd = Character("Front Desk Worker")

define lr = Character("Laura")

define PKFlag = False

define SPacket = False
define CPhone = False
define bag_flag = False
define wii_done = False

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

    "You and Laura are about to start your rounds when you hear a scream coming from upstairs"

    hide laura smile

    show laura nervous at double_size

    lr "Oh shit what should we do?"

    yn "We have to go check it out! We need to make sure they're ok"

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
    label ind:
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

            yn "Shit! I'm sorry, Laura I'll call 911!"

            hide bodhi angry

            "The residents watch you call 911 but now look at you with a suspicious gaze"

            jump sc_investigate

    label sc_investigate:
        "You notice that a small crowd has formed around the scene and you realize you should start investigating and questioning witnesses"

        menu:
            "Question witness 1":
                define em = Character("Emma")

                em "I was just walking in one of the hallways when I heard a loud explosion and a scream coming from this room"

                em "I ran over to the noise and saw Gabi running away, I assumed she'd be getting some help. I got to the room and
                    saw Tori on the ground and I screamed. Is she going to be ok?"

                jump sc_i_2
            "Question witness 2":
                define ar = Character("Armani")

                ar "I was in my dorm room when I heard an explosion, then I heard someone scream"
            
                ar "I opened my door to see smoke in the hallway, and I saw you and Laura"

                ar "I've seen you around though, weren't you at Tori's dorm last night?"

                jump sc_i_2
            "Inspect the microwave":

                transform packet_size:
                    xpos 400
                    ypos -100
                    zoom 2 #adjust as needed

                show evidence packet at packet_size

                "You find traces of an explosive powder hidden inside the seasoning packet, and it smells like burnt sulfur."

                "{i}Seasoning Packet added to inventory!{/i}"

                $ SPacket = True

                hide evidence packet

                jump sc_i_2
            "Examine the body":
                menu:
                    "Check Upper Body":
                        "There was blood running down her forehead and her head seemed bashed-in"
                        "You notice something by the victim's head. Leaning down, you see it's a cell phone"
                        "The screen is cracked and a bunch of instagram messaged from Gabbi fill the screen"
                        "{i}Cracked Phone added to inventory!{/i}"
                        $ CPhone = True
                        jump sc_i_2
                    "Check Lower Body":
                        "You see slight burn marks on the body, and noodles splattered around"
                        "You notice something in the victim's pocket. Reaching in you pull out a cell phone"
                        "The screen is cracked and a bunch of instagram messaged from Gabbi fill the screen"
                        "{i}Cracked Phone added to inventory!{/i}"
                        $ CPhone = True
                        jump sc_i_2

    label sc_i_2:

        "Alerted by all the commotion, a third resident arrives in the door and lets out a scream upon seeing the body"

        "You realize that as an RA, you probably need to talk to them and manage the situation"

        define ha = Character("Hannah")

        menu:
            "Be Reassuring":
                yn "I understand ... it's a lot to take in. But anything you can tell us might really help. I promise we'll keep this confidential."
                ha "I... I just don't want any trouble. I didn't do anything!"
                jump sc_i_3
            "Be Direct":
                yn "Look, we need to know exactly what's going on here. Any details, big or small, could make a difference."
                ha "I had nothing to do with this!"
                jump sc_i_3
        label sc_i_3:
            "You realize that a small crowd is starting to form in the hallway"
            menu:
                "Continue questioning Hannah":
                    menu:
                        "Ask about anything unusual":
                            yn "Did you notice anything unusual around the time of the scream? Any strange sounds, or anyone acting suspicious?"
                            ha "I was just studying in my room when I heard something that sounded like a pop or a small explosion."
                            ha "At first, I thought maybe someone dropped something heavy or, like, something weird with the microwave."
                            jump sc_i_3
                        "Ask about people in the hallway":
                            yn "Who did you see out here? Did anyone else come by before the scream?"
                            ha "I saw Gabbi hanging around in the hallway last night. She was sort of loitering by Tori's door. I didn't think much of it at first-but it was kinda odd since she's always usually at B Tower"
                            jump sc_i_3
                        "Ask about the smell":
                            yn "Do you remember smelling anything weird around the time this happened? It's just that... there's this burning smell lingering in the hallway now."
                            ha "You mean, like, burning sulfur?  If that's important... I think I smelled it down in the laundry room last night."
                            ha "Could someone have been using something down there? It didn't seem like just burnt food."
                            jump sc_i_3
                "Address the hallway":
                    "You turn towards the crowd, full of murmers of fear and curiosity"
                    yn "Alright everyone, get back to your rooms!"
                    "The crowd slowly dissapates as people return to their dorms"
                    "You and Laura glance around, taking in the damage from the explosion."
                    "There's debris scattered everywhere: fragments of ceramic from the microwave, charred bits of paper, and what might have once been part of a notebook."
                    lr "You smell that? It's not just burnt noodles. It smells... smoky"
                    yn "Yeah. Something isn't right. Let's look around; it might tell us more about what happened."
                    "Among the scattered debris, your eye lands on something"
                    yn "What's this?"
                    menu:
                        "Pick up note":
                            "You pick up a charred and crumpled note. You're barely able to make out the words"
                            define no = Character("Charred Note")
                            no "{i}You don't deserve him{/i}"
                            "{i}Charred Note added to inventory!{/i}"
                            "You and Laura both lean in to investigate the note further"
                            lr "What the hell?! Is this some kind of... threat?"
                            yn "It must be. But to Tori? Sounds like a love triangle gone wrong?"
                            lr "It's creepy, that's for sure. Maybe Tori was dating someone on the side? But who...?"
                            "You glance at the note again, and it's impossible to shake the feeling that it's connected to whatever happened here."
                            yn "Hmm... let's see what else we can find"    
                            jump y_path
                        "Pick up broken Wii Remote" if wii_done:
                            "Your foot nudges something small and plastic. You look down and see a cracked, burnt Wii remote, partially melted at one end."
                            "{i}Burnt Wii Remote added to inventory!{/i}"
                            yn "This... doesn't belong here..."
                            lr "A Wii remote? I didn't even know anyone still had one of those."
                            lr "Hey, do you see this dried blood on one edge?"
                            yn "Woah... that's... weird. Let's keep looking around."
                            lr "Wait but this changes things. If there's blood on the remote, could that mean someone hit her with it?"
                            ha "Someone murdered her?!?!"
                            yn "I'm not sure, but let's keep keep looking around"
                            jump done
        jump done

label y_path:
    scene bg hallway at half_size

    show laura nervous at double_size

    define phone_choice = 2

    define dm_flag = False

    "The hallway is tense as you and Laura discuss your next steps. It's clear that more investigation is needed, and Gabbi might be involved."
    "You have the victim's phone in your hand"
    "The screen is cracked, and the battery is at 1%%. You manage to unlock it using Tori's birthday as the passcode."

    lr "Let's hope there's something in here that'll give us a clue. Quick, everything - messages, photos, whatever before it dies!"

    label p_loop:
        menu:
            "Examine Messages":
                "You scroll through Tori's messages, but nothing stands out. A few group chats, some conversations with family, and an order confirmation for ramen packets."
                lr "Nothing unusual in her texts. No threats, no suspicious numbers."
                $ phone_choice -= 1
                if phone_choice:
                    jump p_loop
                else:
                    "Suddenly the phone dies. Its an android, yet nobody has an android charger..."
                    jump p_dead
            "Examine Photos":
                "You open the photo gallery. It's filled with group selfies, pictures of her dorm room, and a photo of ramen from last night. Nothing stands out."
                lr "It's almost frustrating how normal this all seems. There's gotta be something here."
                $ phone_choice -= 1
                if phone_choice:
                    jump p_loop
                else:
                    "Suddenly the phone dies. Its an android, yet nobody has an android charger..."
                    jump p_dead
            "Examine Instagram Notifications":
                "The instagram notifications catch your attention. You scroll through Tori's DMs and notice a heated conversation between her and Gabbi"
                define vg = Character(">Gabbi")
                define vt = Character(">Tori")
                vg "{i}You're disgusting. How dare you spread lies about me?{/i}"
                vt "{i}It's not a lie if it's true. Everyone's starting to notice how obsessed you are. Maybe they should know the full story.{/i}"
                vg "{i}If you say one more word, I swear you'll regret it. You think I don't know you're hiding something?{/i}"
                vt "{i}You're delusional for thinking they like you{/i}"
                vg "{i}Keep your head on a swivel Tori"
                yn "Woah, Laura look at this."
                lr "Whoa, that's intense. What could this be about?"
                yn "Some feud? Over who? We need to find Gabbi. I remember her dorm is in B Tower, maybe she might be able to tell us more"
                "You pull out your phone and take a picture of the chat between Tori and Gabbi"
                "{i}Screenshot of argument added to inventory!{/i}"
                $ dm_flag = True
                $ phone_choice -= 1
                if phone_choice:
                    jump p_loop
                else:
                    "Suddenly the phone dies. Its an android, yet nobody has an android charger..."
                    jump p_dead
    label p_dead:
        lr "Of course it dies now. Guess we better split up, we need to cover more ground"
        lr "I'll stay here in A Tower and see what else I can find. You head over to B Tower."
        yn "I don't like the idea, but alright. Let's regroup in an hour. Be careful, okay?"
        lr "I will, and call me if you find anything, big or small"

        scene bg bhall at half_size

        "You stand outside Gabbi's dorm room and knock but there's no answer. You knock again."
        "Gabbi's roommate Sandra opens the door, eyes half open and yawning"
        define sn = Character("Sandra")
        sn "Oh hey, what's up?"
        label q_loop:
            menu:
                "Ask about Gabbi":
                    yn "Hey, sorry to bother you, but have you seen Gabbi around? I'm trying to find her"
                    sn "Oh uh, not really. Why?"
                    menu:
                        "Show Instagram screenshots" if dm_flag:
                            yn "Tori was murdered, and these messages give us reason to think Gabbi was involved somehow. Is there anything you can remember?"
                            sn "What? It can't be! Oh God... well now those messages make sense. She's been fighting with Tori over some lover for weeks."
                            sn "Last night I saw her grumbling about Tori while carrying a black trash bag towards the laundry room. Didn't think anything of it at the time..."
                            yn "Thanks, I'll make my way there. And I'm very sorry this is all weird to me too."
                            sn "Let me know if you find something"
                            "You make your way towards the laundry room"
                            jump laundry_path
                        "Ask Gabbi's whereabouts":
                            yn "Tori was murdered, and we think Gabbi might be involved somehow. Can you remember where you last saw her?"
                            sn "What? It can't be! I... I don't really know. She's been really tense lately, though. I think she mentioned going to the storage room for some privacy last night"
                            yn "Thanks, I'll make my way there. And I'm very sorry this is all weird to me too."
                            sn "Let me know if you find something"
                            scene bg storage at half_size
                            "The storage room is cluttered with old moving bins and cleaning supplies"
                            define storage_choice = 1
                            label s_choice:
                                menu:
                                    "Check the shelves":
                                        "You sift through shelves filled with random tools and cleaning bottles, but find nothing useful."
                                        $ storage_choice -= 1
                                        if storage_choice:
                                            jump s_choice
                                        else:
                                            yn "Dead end... nothing here"
                                            jump lobby_path
                                    "Search the bins":
                                        "You search through the bins used to help people move in, but all of them are empty."
                                        $ storage_choice -= 1
                                        if storage_choice:
                                            jump s_choice
                                        else:
                                            yn "Dead end... nothing here"
                                            jump lobby_path

                "Apologize and look elsewhere":
                    yn "Oh- I'm sorry, I thought Gabbi would be here."
                    sn "Yeah I haven't seen her since last night, sorry."
                    yn "It's okay, I was just checking up on her. I'll leave you to it."
                    jump lobby_path


        jump done
    label laundry_path:
        scene bg laundry at half_size
        "The laundry room hums quietly with not a soul in sight. A faint smell of detergent mingles wih something metallic and sharp in the air."
        yn "Augh... what was I looking for again?"
        define laundry_choice = 2
        label l_choice:
            menu:
                "Inspect behind washing machines":
                    "The faint hum of the machines catches your attention. You crouch down to peer behind one of the washers."
                    yn "{i}Sigh,{/i} Nothing but dust bunnies and a few coins. Waste of time."
                    $ laundry_choice -= 1
                    if laundry_choice:
                        jump l_choice
                    else:
                        yn "I have to be getting back to Laura..."
                        jump lobby_path
                "Inspect the detergent shelf":
                    "You glance at the detergent shelf. A sulfur-like smell is coming from this area."
                    menu:
                        "Investigate the Shelf":
                            "You find an empty box of detergent that smells faintly of sulfur, but it doesn't seem out of place."
                            yn "Just regular detergent. This isn't helping."
                            $ laundry_choice -= 1
                            if laundry_choice:
                                jump l_choice
                            else:
                                yn "I have to be getting back to Laura..."
                                jump lobby_path
                        "Move on":
                            "You leave the detergent shelf untouched, focusing on other parts of the room."
                            $ laundry_choice -= 1
                            if laundry_choice:
                                jump l_choice
                            else:
                                yn "I have to be getting back to Laura..."
                                jump lobby_path
                "Inspect behind the dryers":
                    "You spot a black trash bag tucked partially behind a drying machine."
                    menu:
                        "Open the bag":
                            "Inside, you find a charred white hoodie covered in the same explosive residue from earlier. It reeks of a sulfur-like smell."
                            "{i}Black trash bag added to inventory{/i}"
                            $ bag_flag = True
                            yn "Oh my god... I need to tell Laura about this"
                            jump lobby_path
    label lobby_path:
        scene bg lobby at half_size
        "You arrive in the lobby, spotting Laura pacing near the front desk. She looks up as you approach, her face tense."
        lr "What did you find? Please tell me it's something big..."
        if bag_flag:
            jump tell_ev
        else:
            jump tell_noth
        label tell_ev:
            yn "Look at this. Gabbi's white hoodie covered in the same powder from the microwave."
            lr "No way... this ties her directly to the crime. But there's a problem - she's nowhere to be found."
            jump lobby_resume
        label tell_noth:
            yn "No I couldn't find anything major... were you able to get any more info?"
            lr "Not really. I mean, we're pretty sure it's Gabbi, but she's nowhere to be found."
        label lobby_resume:
            "Laura pulls out her phone, showing you texts and notes she's collected during her investigation."
        lr "I talked to a couple of residents in A Tower, and none of them have seen her since this morning. She's hiding, but where?"
        lr "We need to find her before she disappears completely."
        yn "Maybe someone here saw her. Let's ask around."
        "She nods and you look around the lobby, heading back to Bodhi behind the front desk, scrolling on his phone."
        label bodhi_choice:
            menu:
                "Ask about Gabbi's habits":
                    yn "What can you tell me about Gabbi? Does she have any usual hangouts?"
                    fd "Not really. She mostly keeps to herself. Sometimes I see her in the lobby writing in a notebook."
                    menu:
                        "What kind of notebook?":
                            fd "No idea. Just a regular notebook I guess. She didn't talk about it."
                            jump bodhi_choice
                        "Does she always seem this quiet?":
                            fd "Yeah, mostly. She's always been kinda ... intense, I guess."
                            jump bodhi_choice
                "Ask about suspicious behavior":
                    yn "Have you noticed anything weird with the residents? Anyone acting off lately?"
                    fd "Weird is kinda normal here, but if you're asking about something specific..."
                    menu:
                        "We're looking into Gabbi specifically":
                            fd "Oh yeah, she was pacing the lobby early this morning. Looked over her shoulder a lot and then bolted toward the kitchen."
                            lr "Why would she be so paranoid? Was she hiding something?"
                            fd "Could be. Or maybe it's the whole thing with Tori. You know, how Tori told everyone about Gabbi liking you?"
                            yn "What? Tori... told people that?"
                            fd "eah, everyone knows. Thought you did too."
                            lr "If Gabbi thought Tori was a threat to her secret - or to you - it might explain everything. Let's go to the kitchen."
                            menu:
                                "Go to kitchen":
                                    jump kitchen_path
                                "Keep questioning":
                                    jump bodhi_choice
                        "Have you heard any news lately?":
                            fd "Nah, not really. Except for all the rumors about Gabbi liking you, I'd bet she's not happy with Tori."
                            yn "Tori started that? About Gabbi... liking me?"
                            fd "Duh. It's Sellery, man. News travels fast."
                            lr "Jealousy and rage over a secret like that... it's definitely a motive"
                            jump bodhi_choice
                "Ask about Tori's recent behavior":
                    yn "What about Tori? Did you notice anything strange about her before... uhh today?"
                    fd "Tori? Uh... maybe I guess. She was always kind of loud. What are you getting at?"
                    menu:
                        "Did she fight with anyone recently?":
                            fd "Not that I know of. But you know, Tori kind of liked to stir the pot. Wouldn't be surprised if she pissed off someone else, too."
                            lr "Do you know who?"
                            fd "Nope. Could've been anyone. People weren't exactly lining up to be her friend."
                            jump bodhi_choice
                        "Was she involved in anything dangerous?":
                            fd "Dangerous? Nah. Tori was just like, your average student. I mean she liked gossip and drama, but who doesn't?"
                            yn "So, nothing out of the ordinary?"
                            fd "Not really. Sounds like you're barking up the wrong tree."
                            jump bodhi_choice
    label kitchen_path:
        scene bg kitchen at half_size
        "You enter the kitchen, the fluorescent lights flickering overhead, casting a dim glow across the space."
        "The place is a mess with dirty dishes piled high.The faint smell of a burning aroma lingered in the air."
        lr "This place looks like a crime scene."
        yn "You smell that? Smells like the sulfur from the crime scene."
        lr "Yeah, let's look around. Maybe we can find something."
        label k_choice:
            menu:
                "Check the counter near the sink":
                    "You move towards the sink, where the clutter is at its worst. The smell of leftover food lingers, mixing with something sharper, metallic."
                    "You sift through a pile of dirty plates and glasses, trying to find anything useful."
                    "The area seems ordinary, though. Just mess and food scraps, nothing that immediately stands out."
                    yn "Nothing here"
                    jump k_choice
                "Look inside the fridge":
                    "You slide open the fridge door, a burst of cold air hitting your face."
                    "The shelves are disorganized-half-empty cartons of milk, takeout boxes stacked up, and a bottle of soy sauce tipped on its side."
                    "As you push aside the containers to see what's hidden in the back, you find nothing unusual. Just spoiled food and an unpleasant smell."
                    yn "What am I even looking for?"
                    jump k_choice
                "Search the spice cabinet":
                    "You turn and open the cabinet, your eyes scanning the shelves."
                    "The smell is stronger here, but there's nothing that looks particularly out of place… until you spot something wedged between the cans"
                    yn "What is this... a wallet?"
                    "You pull it out carefully and open it. Gunpowder residue spills out"
                    "Brushing the powder off, you see Gabbi's ID. Your heart skips a beat."
                    "{i}Gabbi's ID added to inventory{/i}"
                    yn "This doesn't make sense. Why is her ID here? And why is it covered in gunpowder?"
                    lr "Is that... Gabbi's ID?"
                    jump conclusion
    label conclusion:
        yn "This is it! We've got her ID, and there's gunpowder residue on it... she killed Tori!"
        lr "It has to be! I mean, this is the evidence we needed. No doubt about it."
        "Your hands shake as you pull out your phone, dialing 911 quickly. You try to steady your breath, your mind racing."
        menu:
            "Call 911":
                define op = Character("911 Operator")
                op "911, what's your emergency?"
                yn "Yes, this is an emergency. We've found evidence of a crime, and the suspect is a resident of Sellery Hall - Gabbi. We believe she's involved in a murder."
                op "Stay calm. We've dispatched officers to your location. Please stay where you are."
                "As you end the call, you turn to Laura, the weight of the situation finally sinking in."
        "The sound of sirens fills the air as the authorities finally arrive. Officers flood the kitchen, taking in the scene, and immediately begin to take statements."
        "They confirm the presence of gunpowder residue on Gabbi's ID and begin compiling their case."
        "A city-wide manhunt for Gabbi begins, the news spreads quickly, and everyone seems to be on edge."
        "Three days later, a breaking news update announces that Gabbi has been caught."


    label done:
        stop music fadeout 1

        "To be continued..."

    # This ends the game.

    return
