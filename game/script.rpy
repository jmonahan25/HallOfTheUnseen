# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define fd = Character("Front Desk Worker")

define lr = Character("Emma")

define PKFlag = False

define SPacket = False
define CPhone = False
define evidence_flag = False
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

    play music "cool-suspense.mp3"

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

    show emma happy at half_size

    "You turn and see Emma (your duty partner for the night)"

    yn "Don't jinx us! I heard on Saturday they had to call the paramedics 6 times because some fratboys were so mad we lost the game that they decided to mix whisky and vodka and then ate an edible."

    hide emma happy

    show emma question at half_size
    
    lr "I will never understand freshmen. It's like they're constantly trying to make a new level on dumb ways to die."

    hide emma question

    show emma happy at half_size

    stop music

    "You and Emma are about to start your rounds when you hear a loud scream coming from one of the floors above you!"

    hide emma happy

    menu:
        "Run towards the scream":
            jump scream_path

    label scream_path:
        show emma shocked at half_size

        lr "Oh shit what should we do?"

        yn "We have to find where that came from to make sure they're ok!"

        hide emma shocked

        scene bg hallway at half_size

        "You run towards the scream and see a group of residents crowded outside room 219"

        define bd = Character("Keith")

        show keith sad at half_size

        bd "Oh thank god the House Fellows are here! Please help her!"

        hide keith sad

        show emma thanks at half_size

        lr "Don't worry, we got you, what's the problem?"

        hide emma thanks

        show emma shocked at half_size

        "Emma stops in the middle of her sentence and her eyes widen"

        hide emma shocked

        transform half_size_down:
            xpos 100
            ypos -200
            zoom 0.5 #adjust as needed

        scene bg dorm body at half_size_down

        play music "spooky-horror-piano.mp3"

        ""

        define v1 = Character("Dying Student")

        menu:
            "Try to help the student":
                jump scream_help

            "Stand in shock":
                jump scream_shock

        label scream_help:
            "You run over to the student's body and begin to try and give CPR"

            "The student slowly opens their eyes"

            v1 "This is your fault..."

            yn "What the fuck are you talking about?!"

            "The resident dies in your arms, leaving you confused and lost"

            "The only thing you know is this is somehow connected to you"
            "You notice that a small crowd has formed around the scene and you realize you should start investigating and questioning witnesses"

            jump sc_investigate

        label scream_shock:
            "The residents watch you standing in shock and grow increasingly frustrated"

            show keith angy at half_size

            bd "Why aren't you doing something?!"

            yn "Shit! I'm sorry, Emma I'll call 911!"

            hide keith angy

            "The residents watch you call 911 but now look at you with a suspicious gaze"
            "You notice that a small crowd has formed around the scene and you realize you should start investigating and questioning witnesses"

            jump sc_investigate

    define invest_choice = 2
    label sc_investigate:
        menu:
            "Question first witness":
                define em = Character("Laura")

                show sweater sad at half_size

                em "I was just walking in one of the hallways when I heard a loud explosion and a scream coming from this room"

                em "I ran over to the noise and saw Gabbi running away, I assumed she'd be getting some help. I got to the room and
                    saw Tori on the ground and I screamed. Is she going to be ok?"

                hide sweater sad

                $ invest_choice -= 1
                if invest_choice:
                    jump sc_investigate
                else:
                    jump sc_i_2
            "Question second witness":
                define ar = Character("Armani")

                show armani distressed at half_size

                ar "I was in my dorm room when I heard an explosion, then I heard someone scream"
            
                ar "I opened my door to see smoke in the hallway, and I saw you and Emma"

                hide armani distressed

                show armani curious at half_size

                ar "I've seen you around though, weren't you at Tori's dorm last night?"

                hide armani curious

                $ invest_choice -= 1
                if invest_choice:
                    jump sc_investigate
                else:
                    jump sc_i_2
            "Inspect the microwave":

                transform packet_size:
                    xpos 600
                    ypos 200
                    zoom 2 #adjust as needed

                show evidence packet at packet_size

                "You find traces of an explosive powder hidden inside the seasoning packet, and it smells like burnt sulfur."

                "{i}Seasoning Packet added to inventory!{/i}"

                $ SPacket = True
                $ evidence_flag = True

                hide evidence packet

                $ invest_choice -= 1
                if invest_choice:
                    jump sc_investigate
                else:
                    jump sc_i_2
            "Examine the body":

                transform phone_size:
                    xpos 700
                    ypos 200
                    zoom 2 #adjust as needed

                menu:
                    "Check Upper Body":
                        "There was blood running down her forehead and her head seemed bashed-in"
                        "You notice something by the victim's head. Leaning down, you see it's a cell phone"

                        show evidence phone at phone_size

                        "The screen is cracked and a bunch of instagram messaged from Gabbi fill the screen"
                        "{i}Cracked Phone added to inventory!{/i}"

                        hide evidence phone

                        $ CPhone = True
                        $ evidence_flag = True
                        $ invest_choice -= 1
                        if invest_choice:
                            jump sc_investigate
                        else:
                            jump sc_i_2
                    "Check Lower Body":
                        "You see slight burn marks on the body, and noodles splattered around"
                        "You notice something in the victim's pocket. Reaching in you pull out a cell phone"
                        show evidence phone at phone_size
                        "The screen is cracked and a bunch of instagram messaged from Gabbi fill the screen"
                        "{i}Cracked Phone added to inventory!{/i}"

                        hide evidence phone

                        $ CPhone = True
                        $ evidence_flag = True
                        $ invest_choice -= 1
                        if invest_choice:
                            jump sc_investigate
                        else:
                            jump sc_i_2

    label sc_i_2:

        "Alerted by all the commotion, a third resident arrives in the door and lets out a scream upon seeing the body"

        "You realize that as an RA, you probably need to talk to them and manage the situation"

        show hannah sad at half_size

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
                            hide hannah sad
                            show hannah upset at half_size
                            ha "I was just studying in my room when I heard something that sounded like a pop or a small explosion."
                            ha "At first, I thought maybe someone dropped something heavy or, like, something weird with the microwave."
                            jump sc_i_3
                        "Ask about people in the hallway":
                            yn "Who did you see out here? Did anyone else come by before the scream?"
                            hide hannah sad
                            show hannah left at half_size
                            ha "I saw Gabbi hanging around in the hallway last night. She was sort of loitering by Tori's door. I didn't think much of it at first-but it was kinda odd since she's always usually at B Tower"
                            jump sc_i_3
                        "Ask about the smell":
                            yn "Do you remember smelling anything weird around the time this happened? It's just that... there's this burning smell lingering in the hallway now."
                            hide hannah sad
                            show hannah left at half_size
                            ha "You mean, like, burning sulfur?  If that's important... I think I smelled it down in the laundry room last night."
                            ha "Could someone have been using something down there? It didn't seem like just burnt food."
                            jump sc_i_3
                "Address the hallway":
                    hide hannah left
                    hide hannah sad
                    hide hannah upset
                    "You turn towards the crowd, full of murmers of fear and curiosity"
                    yn "Alright everyone, get back to your rooms!"
                    "The crowd slowly dissapates as people return to their dorms"
                    "You and Emma glance around, taking in the damage from the explosion."
                    "There's debris scattered everywhere: fragments of ceramic from the microwave, charred bits of paper, and what might have once been part of a notebook."
                    show emma question at half_size
                    lr "You smell that? It's not just burnt noodles. It smells... smoky"
                    yn "Yeah. Something isn't right. Let's look around; it might tell us more about what happened."
                    hide emma question
                    "Among the scattered debris, your eye lands on something"
                    yn "What's this?"
                    menu:
                        "Pick up note":
                            "You pick up a charred and crumpled note. You're barely able to make out the words"
                            define no = Character("Charred Note")
                            transform note_size:
                                xpos 700
                                ypos 200
                                zoom 2 #adjust as needed
                            show evidence note at note_size
                            no "{i}You don't deserve him{/i}"
                            "{i}Charred Note added to inventory!{/i}"
                            "You and Emma both lean in to investigate the note further"
                            hide evidence note
                            show emma crossed at half_size
                            lr "What the hell?! Is this some kind of... threat?"
                            yn "It must be. But to Tori? Sounds like a love triangle gone wrong?"
                            lr "It's creepy, that's for sure. Maybe Tori was dating someone on the side? But who...?"
                            "You glance at the note again, and it's impossible to shake the feeling that it's connected to whatever happened here."
                            yn "Hmm... let's see what else we can find"
                            hide emma crossed 
                            stop music fadeout 1.0
                            jump y_path
                        #"Pick up broken Wii Remote" if wii_done:
                            #"Your foot nudges something small and plastic. You look down and see a cracked, burnt Wii remote, partially melted at one end."
                            #"{i}Burnt Wii Remote added to inventory!{/i}"
                            #yn "This... doesn't belong here..."
                            #lr "A Wii remote? I didn't even know anyone still had one of those."
                            #lr "Hey, do you see this dried blood on one edge?"
                            #yn "Woah... that's... weird. Let's keep looking around."
                            #lr "Wait but this changes things. If there's blood on the remote, could that mean someone hit her with it?"
                            #ha "Someone murdered her?!?!"
                            #yn "I'm not sure, but let's keep keep looking around"
                            #jump done
        jump done

label y_path:
    scene bg hallway at half_size

    show emma question at half_size

    play music "cool-suspense.mp3"

    define phone_choice = 2

    define dm_flag = False

    "The hallway is tense as you and Emma discuss your next steps. It's clear that more investigation is needed, and Gabbi might be involved."
    if (not CPhone):
        lr "I managed to find her phone while we were looking around, there might be something important on it!"
    "You have the victim's phone in your hand"
    "The screen is cracked, and the battery is at 1%%. You manage to unlock it using Tori's birthday as the passcode."

    hide emma question
    show emma mad at half_size

    lr "Let's hope there's something in here that'll give us a clue. Quick, everything - messages, photos, whatever before it dies!"

    hide emma mad

    label p_loop:
        
        transform phone_size:
                    xpos 700
                    ypos 200
                    zoom 2 #adjust as needed

        show evidence phone at phone_size

        menu:
            "Examine Messages":
                "You scroll through Tori's messages, but nothing stands out. A few group chats, some conversations with family, and an order confirmation for ramen packets."
                lr "Nothing unusual in her texts. No threats, no suspicious numbers."
                $ phone_choice -= 1
                if phone_choice:
                    jump p_loop
                else:
                    "Suddenly the phone dies. Its an android, yet nobody has an android charger..."
                    hide evidence phone
                    jump p_dead
            "Examine Photos":
                "You open the photo gallery. It's filled with group selfies, pictures of her dorm room, and a photo of ramen from last night. Nothing stands out."
                lr "It's almost frustrating how normal this all seems. There's gotta be something here."
                $ phone_choice -= 1
                if phone_choice:
                    jump p_loop
                else:
                    "Suddenly the phone dies. Its an android, yet nobody has an android charger..."
                    hide evidence phone
                    jump p_dead
            "Examine Instagram Notifications":
                hide evidence phone
                show evidence screenshot at phone_size
                "The instagram notifications catch your attention. You scroll through Tori's DMs and notice a heated conversation between her and Gabbi"
                define vg = Character(">Gabbi")
                define vt = Character(">Tori")
                vg "{i}You're disgusting. How dare you spread lies about me?{/i}"
                vt "{i}It's not a lie if it's true. Everyone's starting to notice how obsessed you are. Maybe they should know the full story.{/i}"
                vg "{i}If you say one more word, I swear you'll regret it. You think I don't know you're hiding something?{/i}"
                vt "{i}You're delusional for thinking they like you{/i}"
                vg "{i}Keep your head on a swivel Tori"
                yn "Woah, Emma look at this."
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
                    hide evidence screenshot
                    jump p_dead
    label p_dead:
        show emma mad at half_size
        lr "Of course it dies now. Guess we better split up, we need to cover more ground"
        lr "I'll stay here in A Tower and see what else I can find. You head over to B Tower."
        yn "I don't like the idea, but alright. Let's regroup in an hour. Be careful, okay?"
        show emma thumbs at half_size
        lr "I will, and call me if you find anything, big or small"

        hide emma thumbs

        scene bg bhall at half_size

        "You stand outside Gabbi's dorm room and knock but there's no answer. You knock again."
        "Gabbi's roommate Sandra opens the door, eyes half open and yawning"
        define sn = Character("Sandrine")
        show sandrine crossed at half_size
        sn "Oh hey, what's up?"
        label q_loop:
            menu:
                "Ask about Gabbi":
                    yn "Hey, sorry to bother you, but have you seen Gabbi around? I'm trying to find her"
                    sn "Oh uh, not really. Why?"
                    menu:
                        "Show Instagram screenshots" if dm_flag:
                            yn "Tori was murdered, and these messages give us reason to think Gabbi was involved somehow. Is there anything you can remember?"
                            show sandrine hands at half_size
                            sn "What? It can't be! Oh God... well now those messages make sense. She's been fighting with Tori over some lover for weeks."
                            show sandrine curious at half_size
                            sn "Last night I saw her grumbling about Tori while carrying a black trash bag towards the laundry room. Didn't think anything of it at the time..."
                            yn "Thanks, I'll make my way there. And I'm very sorry this is all weird to me too."
                            sn "Let me know if you find something"
                            hide sandrine curious
                            "You make your way towards the laundry room"
                            jump laundry_path
                        "Ask Gabbi's whereabouts":
                            yn "Tori was murdered, and we think Gabbi might be involved somehow. Can you remember where you last saw her?"
                            show sandrine hands at half_size
                            sn "What? It can't be! I... I don't really know. She's been really tense lately, though. I think she mentioned going to the storage room for some privacy last night"
                            yn "Thanks, I'll make my way there. And I'm very sorry this is all weird to me too."
                            show sandrine curious at half_size
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
                    hide sandrine crossed
                    jump lobby_path


        jump done
    label laundry_path:
        scene bg laundry at half_size
        stop music fadeout 2
        play music "dark-ambient.mp3"
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
                        yn "I have to be getting back to Emma..."
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
                                yn "I have to be getting back to Emma..."
                                jump lobby_path
                        "Move on":
                            "You leave the detergent shelf untouched, focusing on other parts of the room."
                            $ laundry_choice -= 1
                            if laundry_choice:
                                jump l_choice
                            else:
                                yn "I have to be getting back to Emma..."
                                jump lobby_path
                "Inspect behind the dryers":
                    "You spot a black trash bag tucked partially behind a drying machine."
                    transform bag_size:
                        xpos 700
                        ypos 200
                        zoom 2 #adjust as needed
                    show evidence trash at bag_size
                    menu:
                        "Open the bag":
                            "Inside, you find a charred white hoodie covered in the same explosive residue from earlier. It reeks of a sulfur-like smell."
                            "{i}Black trash bag added to inventory{/i}"
                            $ bag_flag = True
                            yn "Oh my god... I need to tell Emma about this"
                            hide evidence trash
                            jump lobby_path
    label lobby_path:
        stop music fadeout 1
        play music "cool-suspense.mp3"
        scene bg lobby at half_size
        "You arrive in the lobby, spotting Emma pacing near the front desk. She looks up as you approach, her face tense."
        show emma mad at half_size
        lr "What did you find? Please tell me it's something big..."
        if bag_flag:
            jump tell_ev
        else:
            jump tell_noth
        label tell_ev:
            yn "Look at this. Gabbi's white hoodie covered in the same powder from the microwave."
            show emma shocked at half_size
            lr "No way... this ties her directly to the crime. But there's a problem - she's nowhere to be found."
            show emma mad at half_size
            jump lobby_resume
        label tell_noth:
            yn "No I couldn't find anything major... were you able to get any more info?"
            lr "Not really. I mean, we're pretty sure it's Gabbi, but she's nowhere to be found."
        label lobby_resume:
            "Emma pulls out her phone, showing you texts and notes she's collected during her investigation."
        lr "I talked to a couple of residents in A Tower, and none of them have seen her since this morning. She's hiding, but where?"
        lr "We need to find her before she disappears completely."
        yn "Maybe someone here saw her. Let's ask around."
        "She nods and you look around the lobby, heading back to Bodhi behind the front desk, scrolling on his phone."
        hide emma mad
        show bodhi wave at quarter_size
        transform shrug_size:
            xpos 500
            zoom 1.1
        define fb = Character("Bodhi")
        define bodhi_count = 4
        fb "Hey, I heard a huge commotion earlier today, do y'all need help with anything?"
        label bodhi_choice:
            menu:
                "Ask about Gabbi's habits":
                    yn "What can you tell me about Gabbi? Does she have any usual hangouts?"
                    show bodhi shrug at shrug_size
                    fb "Not really. She mostly keeps to herself. Sometimes I see her in the lobby writing in a notebook."
                    menu:
                        "What kind of notebook?":
                            fb "No idea. Just a regular notebook I guess. She didn't talk about it."
                            $ bodhi_count -= 1
                            if bodhi_count:
                                show bodhi neutral
                                jump bodhi_choice
                            else:
                                hide bodhi shrug
                                jump quick_call
                        "Does she always seem this quiet?":
                            fb "Yeah, mostly. She's always been kinda ... intense, I guess."
                            $ bodhi_count -= 1
                            if bodhi_count:
                                show bodhi neutral
                                jump bodhi_choice
                            else:
                                hide bodhi shrug
                                jump quick_call
                "Ask about suspicious behavior":
                    yn "Have you noticed anything weird with the residents? Anyone acting off lately?"
                    show bodhi shrug at shrug_size
                    fb "Weird is kinda normal here, but if you're asking about something specific..."
                    menu:
                        "We're looking into Gabbi specifically":
                            fb "Oh yeah, she was pacing the lobby early this morning. Looked over her shoulder a lot and then bolted toward the kitchen."
                            hide bodhi shrug
                            show emma question at half_size
                            lr "Why would she be so paranoid? Was she hiding something?"
                            hide emma question
                            show bodhi shrug at shrug_size
                            fb "Could be. Or maybe it's the whole thing with Tori. You know, how Tori told everyone about Gabbi liking you?"
                            yn "What? Tori... told people that?"
                            fb "Yeah, everyone knows. Thought you did too."
                            hide bodhi shrug
                            show emma mad at half_size
                            lr "If Gabbi thought Tori was a threat to her secret - or to you - it might explain everything. Let's go to the kitchen."
                            hide emma mad
                            menu:
                                "Go to kitchen":
                                    stop music fadeout 1
                                    jump kitchen_path
                                "Keep questioning":
                                    $ bodhi_count -= 1
                                    if bodhi_count:
                                        show bodhi neutral
                                        jump bodhi_choice
                                    else:
                                        jump quick_call
                        "Have you heard any news lately?":
                            show bodhi neutral
                            fb "Nah, not really. Except for all the rumors about Gabbi liking you, I'd bet she's not happy with Tori."
                            yn "Tori started that? About Gabbi... liking me?"
                            show bodhi shrug at shrug_size
                            fb "Duh. It's Sellery, man. News travels fast."
                            hide bodhi shrug
                            show emma crossed at half_size
                            lr "Jealousy and rage over a secret like that... it's definitely a motive"
                            hide emma crossed
                            $ bodhi_count -= 1
                            if bodhi_count:
                                show bodhi neutral
                                jump bodhi_choice
                            else:
                                jump quick_call
                "Ask about Tori's recent behavior":
                    yn "What about Tori? Did you notice anything strange about her before... uhh today?"
                    show bodhi shrug at shrug_size
                    fb "Tori? Uh... maybe I guess. She was always kind of loud. What are you getting at?"
                    menu:
                        "Did she fight with anyone recently?":
                            fb "Not that I know of. But you know, Tori kind of liked to stir the pot. Wouldn't be surprised if she pissed off someone else, too."
                            hide bodhi shrug
                            show emma question at half_size
                            lr "Do you know who?"
                            hide emma question
                            show bodhi shrug at shrug_size
                            fb "Nope. Could've been anyone. People weren't exactly lining up to be her friend."
                            $ bodhi_count -= 1
                            if bodhi_count:
                                show bodhi neutral
                                jump bodhi_choice
                            else:
                                hide bodhi shrug
                                jump quick_call
                        "Was she involved in anything dangerous?":
                            show bodhi neutral
                            fb "Dangerous? Nah. Tori was just like, your average student. I mean she liked gossip and drama, but who doesn't?"
                            yn "So, nothing out of the ordinary?"
                            fb "Not really. Sounds like you're barking up the wrong tree."
                            $ bodhi_count -= 1
                            if bodhi_count:
                                show bodhi neutral
                                jump bodhi_choice
                            else:
                                hide bodhi_neutral
                                jump quick_call

    label quick_call:
        show emma shocked at half_size
        lr "We don't have time to keep talking! We should call 911!"
        hide emma shocked
        "You quickly make a dispatch call to the authorities, telling them everything you know, even if it isn't a lot..."
        "Three days later, you see on the news that she was finally caught"
        jump bad_end
    
    label kitchen_path:
        scene bg kitchen at half_size
        play music "dark-ambient.mp3"
        "You enter the kitchen, the fluorescent lights flickering overhead, casting a dim glow across the space."
        "The place is a mess with dirty dishes piled high.The faint smell of a burning aroma lingered in the air."
        show emma mad at half_size
        lr "This place looks like a crime scene."
        yn "You smell that? Smells like the sulfur from the crime scene."
        lr "Yeah, let's look around. Maybe we can find something."
        hide emma mad
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
                    transform id_size:
                        xpos 700
                        ypos 200
                        zoom 2 #adjust as needed
                    "You turn and open the cabinet, your eyes scanning the shelves."
                    "The smell is stronger here, but there's nothing that looks particularly out of place… until you spot something wedged between the cans"
                    yn "What is this... a wallet?"
                    "You pull it out carefully and open it. Gunpowder residue spills out"
                    "Brushing the powder off, you see Gabbi's ID. Your heart skips a beat."
                    show evidence card at id_size
                    "{i}Gabbi's ID added to inventory{/i}"
                    yn "This doesn't make sense. Why is her ID here? And why is it covered in gunpowder?"
                    hide evidence card
                    show emma shocked at half_size
                    lr "Is that... Gabbi's ID?"
                    jump conclusion
    label conclusion:
        stop music fadeout 1
        yn "This is it! We've got her ID, and there's gunpowder residue on it... she killed Tori!"
        show emma crossed at half_size
        lr "It has to be! I mean, this is the evidence we needed. No doubt about it."
        "Your hands shake as you pull out your phone, dialing 911 quickly. You try to steady your breath, your mind racing."
        hide emma crossed
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
        if (bag_flag and evidence_flag):
            jump good_end
        else:
            jump bad_end


    label good_end:
        play music "cool-suspense.mp3"
        scene bg lobby at half_size
        "She was apprehended at Dane County Airport, trying to flee the city. The authorities bring her in for questioning, and after hours of interrogation, Gabbi confesses to the crime."
        define gc = Character("Gabbi's Confession")
        show gabbi distraught at half_size
        gc "{i}I never meant for any of this to happen. It was supposed to be a mistake, but then it spiraled... I panicked, and I didn't know who to trust anymore.{/i}"
        gc "{i}I didn't want to hurt anyone, but I just couldn't stop. The pressure of everything, the rumors... I snapped.{/i}"
        hide gabbi distraught
        "The case is closed, and Gabbi is taken into custody. Justice has been served, but you can't shake the image of Gabbi - someone you once knew - being taken away in handcuffs."
        "But the day comes to a close on the end of this tragic story..."
        "The End"
        jump done


    label bad_end:
        play music "spooky-horror-piano.mp3"
        scene bg lobby at half_size
        "Without enough physical evidence to confirm her guilt, the authorities are forced to let her go. Gabbi walks free, and despite the initial relief of her capture, the case remains unsolved."
        define gr = Character("Gabbi's Statement")
        show gabbi shocked at half_size
        gr "{i}I have nothing to hide. This is just some misunderstanding. I don't know why I'm being accused of this. No one can prove I did anything.{/i}"
        hide gabbi shocked
        "She vanishes after her release, slipping through the cracks of the investigation. The case is closed temporarily, but you know that Gabbi is still out there."
        "There's an unsettling feeling of unfinished business as she disappears, nowhere to be seen."
        "The End"
        jump done


    label done:


    # This ends the game.


    return