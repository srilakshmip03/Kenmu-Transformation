# things to fix
    # how to make big screen with title "act one"
    # how to animate
    # why is sister floating
        # why is positioning such a PAIN

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

##### rename these ####
define y = Character("You")
define f = Character("Father")
define s = Character("Sister")
define r = Character("Rival", color="#F00", who_outlines=[(3, "#000000", 1, 1)])
define l = Character("Local")


# The game starts here.
# starting scene, probs prologue
label start:

    scene bg hills

    "This would be where the prologue scenes go."
    "Since there aren't any choices the player makes, I was thinking it's just a click-through sequence."

    scene bg burning

    "After a long series of brutal battles..."

    scene bg peaceful

    "More historical information leading into the main story of the game."

    show black with fade

    "Shortly after these events..."

    jump house


label house:

    scene bg home

    show sister:
        zoom 2.0

    y "Good morning!"
    s "Hey there, ready to start the day? Someone outside wanted to speak with you."

    menu:
        "I want to..."

        "Meet with the person outside.":
            $ speak = "outside"
            jump outside
        
        "Do chores with sister.":
            $ speak = "chores"
            jump chores

        "Talk to parent.":
            $ speak = "parent"
            jump parent

label outside:
    scene bg hills

    show local

    l "Expository information or something."

    menu:
        "Speak with parent now." if speak == "outside": 
            jump parent
        "Patrol the land.":
            jump patrol

label chores:
    scene bg home

    show sister:
        zoom 2.0

    s "More information here."

    y "Interesting response."

    menu:
        "Speak with the person outside now." if speak == "family":
            jump outside
        "Patrol the land.":
            jump patrol
    
label parent:
    scene bg home

    show father:
        zoom 1.5

    f "More information here."

    y "Interesting response."

    menu:
        "Speak with the person outside now." if speak == "family":
            jump outside
        "Patrol the land.":
            jump patrol

label patrol:
    scene bg hills

    show angry

    r "Still refusing to leave us alone?"
    r "Soon the emperor will recognize our claims."
    r "Until then..."

    show bg hills with hpunch

    r "We will regain our honor."

    scene bg home

    show father at left:
        zoom 1.5
    show sister at right:
        zoom 2.0

    y "Telling father what happened"
    s "I saw it happen!"
    f "..."
    f "You need to defend our honor. Head to the capital as soon as you can."
    f "Make this right."

    scene bg homeNight

    # this could be a good point to add a cool mechanic, idk what yet

    y "Freaking out about the journey that lies ahead."

# end game
return
