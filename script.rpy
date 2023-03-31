# things to fix
    # figure out linear command
    ## why is sister floating
        # why is positioning such a PAIN
    # what's going on with the menu (chores/person/parent)
    # CHARACTER CUSTOMIZATION
        # image map for this? - current goal


# The script of the game goes in this file.

# main
define mc = Character("Main Character")
define sis = Character("Sister")
define bro = Character("Brother")
define dad = Character("Father")
define archer = Character("Old Wise Archer Dude")
define fish = Character("Fisherman")
define merch = Character("Merchant")

define hostage = DynamicCharacter("help")

define r = Character("Rival", color="#F00", who_outlines=[(3, "#000000", 1, 1)])


# create traits
default martial = 0
default charisma = 30
default erudition = 0
default patience = 0

### reputations ###

screen actOne():

    text "Act One":
        align(0.5, 0.5)

init python:

    config.underlay.append(renpy.Keymap(mousedown_1=lambda: renpy.hide_screen('actOne')))

### Add customization screen here ###

# The game starts here.
label start():

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

label house():

    show black
    show screen actOne()
    pause

    hide screen actOne with fade
    scene bg night with fade

    "*Knock knock*"

    mc "I guess it's time to get up."

    scene bg home

    show local at left with moveinleft

    bro "You're finally awake!"

    show father at right with moveinright

    dad "Seat yourself, please."

    dad "You're awake."

    mc "Yes, Father, good morning."

    "Is there a reason the sun's so high and I'm still in my sleeping gown?"

    hide local with moveoutleft

    show sister with moveinleft

    sis "I’m starving! Why does he get to sleep in and we have to wait for our meal??"

    dad "These are delicate times; you never know when you’d need to keep your strength up."
    dad "Collecting that strength during resting hours is more important than you know."

    dad "And each of you had the chance to do so this morning."
    dad  "Please sit and stop fiddling with your robe."

    show black with fade

# end game
return