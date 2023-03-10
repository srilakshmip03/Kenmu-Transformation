# things to fix
    # figure out linear command
    # why is sister floating
        # why is positioning such a PAIN
    # what's going on with the menu

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

# for a big screen with the name "ACT I", just make a file and set that as the first scene.
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

    l "Expository information."

    menu:
        "Speak with parent now.":
            jump parent
        "Do chores now.":
            jump chores
        "Patrol the land.":
            jump patrol

label chores:

    scene bg home

    show sister:
        zoom 2.0

    s "More information here."

    y "Interesting response."

    menu:
        "Speak with parent now.":
            jump parent
        "Speak with the person outside now."
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
        "Do chores now.":
            jump chores
        "Speak with the person outside."
            jump outside
        "Patrol the land.":
            jump patrol

label patrol:

    scene bg hills

    show angry with moveinleft

    r "Still refusing to leave us alone?"
    r "Soon the emperor will recognize our claims!"

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
    f "You need to defend our family. Head to the capital as soon as you can."
    f "Make this right."

    # this doesn't have to be a different image, maybe just a filter over the daytime house scene
    scene night with dissolve

    y "Freaking out about the journey that lies ahead."

    scene bg home with dissolve

    show father with moveinright

    f "Emotional moment sending you off to Kyoto."
    f "Here are some provisions as well as my beloved horse."

    show father at right

    y "Emotional response."

    jump journey

label journey

    

# end game
return
