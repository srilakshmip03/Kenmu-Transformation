# The script of the game goes in this file.

# main
define mc = Character("Marakore")
define sis = Character("Masako")
define bro = Character("Yasumaru")
define dad = Character("Father")
define fish = Character("Akiyoshi")
define merch = Character("Nagamoto")

define arch = Character("Suekuni")

define r = Character("Rival", color="#F00", who_outlines=[(3, "#000000", 1, 1)])

### reputation variables ###
default fisherman = 0
default archerrep = 3
default merchant = 2


### skill variables ###
default patience = 0
default martial = 0
default erudition = 0
default charisma = 0


### character select screen ###
# Prepare the list:
define characters = [
    {
        "name": "The Warrior",
        "picture": "images/choiceone.jpeg"
    },
    {
        "name": "The Diplomat",
        "picture": "images/choicetwo.jpeg"
    },
    {
        "name": "The Sage",
        "picture": "images/choiceone.jpeg"
    },
    {
        "name": "The Scholar",
        "picture": "images/choicetwo.jpeg"
    }
]

# Define the screen to select characters:
screen character_select():
    frame:
        xfill True
        yfill True
        background "#ffddb7"
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 9            
            # Iterate through the list:
            for butt in characters:
                button:
                    size_group "character_buttons"
                    background "#2d2522"
                    hover_background "#963"
                    vbox:
                        add butt["picture"]
                        label butt["name"]:
                            text_size 40
                            text_color "#FFF"
                    action Return(butt["name"])


screen actOne:
    text "Act One":
        align(0.5, 0.5)

init python:
    config.underlay.append(renpy.Keymap(mousedown_1=lambda: renpy.hide_screen('actOne')))

# The game starts here.
label start():
    call screen character_select
    if _return == "The Warrior":
        $patience += 4
        $martial += 8
        $erudition += 1
        $charisma += 2

    elif _return == "The Diplomat":
        $patience += 3
        $martial += 2
        $erudition += 3
        $charisma += 7

    elif _return == "The Sage":
        $patience += 7
        $martial += 3 
        $erudition += 3
        $charisma += 2

    elif _return == "The Scholar":
        $patience += 3
        $martial += 1 
        $erudition += 8
        $charisma += 3


    "You are [_return]. Your patience stat is [patience], your martial stat is [martial], your erudition stat is [erudition], and your charisma stat is [charisma]."

label house():

    show black
    show screen actOne
    pause

    hide screen actOne with fade
    scene bg home with fade

    "*Knock knock*"

    mc "I guess it's time to get up."

    scene bg home

    show brother at left with moveinleft

    bro "Marakore! You’re finally awake!"

    show father at right with moveinright

    dad "Seat yourself, please. A warrior contains himself."

    dad "You're awake."

    mc "Yes, Father, good morning."

    "Is there a reason the sun's so high and I'm still in my sleeping gown?"

    bro "Yes: you overslept, and then forgot to change."

    hide brother with moveoutleft

    show sister at left with moveinleft

    mc "Ack-!"

    sis "I’m starving! Why does he get to sleep in and we have to wait for our meal??"

    dad "These are delicate times; you never know when you’d need to keep your strength up."
    dad "Collecting that strength during resting hours is more important than you know."

    dad "And each of you had the chance to do so this morning."
    dad  "Please sit and stop fiddling with your robe."

    show black with fade
    # play sound "cutlery.mp3"

    scene bg home

    show father at right zorder 3
    show sister at left zorder 2
    show brother zorder 1

    dad "Nagamoto obtained new wares yesterday."

    mc "Oh?"

    sis "Wow, so interesting."

    dad "New shipment of waraji for this one."

    bro "It was an accident… the heat made me drowsy and unable to see…"

    sis "You were inside! And it’s not like the cold would make you more alert."

    dad "Southern weather works differently. Village works tirelessly every year to make sure everyone's needs are being met"
    dad "As a matter of fact…"
    
    mc "It shouldn’t be too late in the day for us to lend our hands. Our FOCUSED hands."

    dad "Exactly. I know Akiyoshi is looking for extra hands to help catch fish."
    dad "He may only be a mere fisherman, but he is extremely well-liked by the village."
    dad "He’s at the foreground of every festival, wedding, and funeral as a volunteer."
    dad "He is the key to earning the trust of the villagers."

    dad "Of course, our… friend… by the field could always use some help."

    sis "Suekuni is always so busy! Do you really think he’d allow me to practice today?!"

    dad "Practice sharpening arrows, most definitely. But then again, I’m sure he’d enjoy some shooting company."

    mc "And I’m sure that with such a recent shipment of goods, Nagamoto would need help organizing and documenting."

    dad "What a long year, this is. Soldiers need armor and weapons if they are to make it through."

    mc "Well, here’s to hoping for a peaceful and prosperous year."

    hide father with moveoutright
    hide sister with moveoutleft
    hide brother with moveoutleft

    menu:
        "What should I do today?"

        "Help the fisherman.":
            jump help_fisherman

        "Sharpen arrows with the archer.":
            jump help_archer

        "Organize shipments with the merchant.":
            jump help_merchant

label help_fisherman():
    scene bg river with fade
    show fisherman

    fish "Still got it after all these years!"

    show brother at right behind fisherman with moveinright
    bro "Whoa! Did you just catch that thing?!"

    show sister at left behind fisherman with moveinleft
    sis "Clearly!"

    fish "Good day, everyone! Happy to see you all once again."

    mc "Forgive us! We arrived later than we would have liked to, but we’re here to help out in any way we can."

    fish "Ah, I could use some company!"
    fish "The sun’s beatin’ down so much that the fish are cookin’ in the basket already."

    fish "Just caught those before you arrived."
    fish "Like yourselves, I’ve been preoccupied with other matters."
    fish "Settling in, you see Masako and Yasumaru playing at the riverside, throwing water at each other and laughing."

    mc "What matters would those be?"
    mc "I can imagine all that constant battling has driven your attention to more political going-ons."

    fish "Ah, well, the nonsense has been driven to my doorstep, that’s true."

    fish "But not to worry! I have helpin’ hands and a wide river."

    mc "Masako! Yasumaru! C’mon! It’s time to catch some fish."

    sis "We were catching fish!!"

    bro "Yeah! Scaring them right into our hands."

    if patience > 5:
        $fisherman += 2
        $patience += 2
        "It takes a while. You almost wanted to give up, after what seems like half an hour, but suddenly the trap shakes. You blink, and realize there’s a fish! You grasp tightly, and hasten to pull it up strongly."
        "It doesn’t take much - you almost redden for thinking you wouldn’t be strong enough to wrestle a fish - and the fish comes flying up, landing on Yasumaru’s face. You ignore his yelling. You spot Akiyoshi laughing and grinning."
    else:
        $patience += 1
        "It takes too long. You try to wait it out, but you just can’t handle it. There’s simply no fish at all! How do fishermen catch these things?"
        "You sigh and pull back the trap. Yasumaru hasn’t caught anything, and Masako is still trying to skewer the water. You feel some disappointment, and judging by Akiyoshi’s face, so does he."

    "You spent your time fishing while also corralling your unruly siblings into sitting still. Despite this being one of the more relaxing atmospheres of the village, you felt there was an undercurrent of unease with Akiyoshi. You couldn’t put it into words."
    mc "Akiyoshi? I was wondering if…"

    fish "Yes."

    mc "I was wondering if fishing for the whole village is still doable with all this unrest going on?"
    mc "At least, with so many mouths to feed."

    fish "Yes. I don’t do this alone, young one. Fishing has been my lifework since I was your age."
    fish "I’ve naturally picked up some connections along the way."
    fish "We’re a close-knit group, and those who do business with me are dear friends."

    sis "Where are they from? Why don’t we ever see your friends? Are they from the capital?!"

    bro "Is it because of Father?"

    fish "I sense that you are anxious about how I view your father. That I hold inside me resentment."
    fish "But you worry for naught, for I do not."
    fish "The truth is, I feel no enmity towards him. But loyalty I also do not feel."
    fish "I do not care who happens to be the master, or warrior, or whatever title is invoked."
    fish "All I desire is to be left alone, to fish peacefully, to survive, to keep my home safe."

    fish "But alas!"

    fish "I do not care much for political matters."
    fish "The constant battling has of course stolen my attention, but I have never had such a good excuse to be seated by this river."


    fish "Many thanks for all of your help today! This food will go to good hands and hungry bellies, I assure you."
    fish "Tell your old man I said hello!"

    if patience > 7:
        $patience += 2
        $fisherman += 1
    else:
        $patience += 1
        $fisherman += 1

    show black with fade
    "With that, he lumbers slowly away. You turn to your siblings and, to your shock, the usual spark of mischief has faded from their expressions to be replaced with a certain amount of serenity."
    "Your own serious expression gives way to a surprised giggle, as you make the decision to turn in for the night."

label help_archer():
    scene bg hills with fade

    bro "-AHHH!"

    sis "AAH! What is it?!"

    arch "Let's try this out, shall we?"

    arch "Over two-hundred degrees!  That's why they call me Mister Alfred Nobel!"

    mc "Yasumaru are you okay?"

    bro "I could have died!"

    arch "And what an irony of the gods that would be."

    sis "Suekuni! It’s us, we’ve come to help out! Wait, are those new arrows?!"

    arch "I felt my dear bow could do with some novelties."
    arch "See how I have added modifications to the arrows."

    mc "You’re going to be okay, you were just shaken a bit."

    bro "I got scared."

    mc "I know. You know how Suekuni is, but try not to let it bother you. I’ve got your back."

    bro "He didn’t care that I almost died!"

    mc "We can talk about it later, brother."
    mc "Shooting your own bow will brighten your spirits back up."

    arch "I’ve hoped you’ve gotten better."
    arch "Ah, you two look fine already. See, no need to worry."

    mc "I must ask not to scare us like that again."

    arch "I was hoping you two would react with more bravado. Aren’t you two sons of a warrior?"

    mc "I don’t think ambushes were how our family was trained to fight."

    arch "I recommend that you stop believing in tall tales. We archs are skirmishes."

    bro "Well, we’re warriors! We fight face to face!"

    arch "You never know, little Yasumaru. I am no lord like you; we commoners must fight however we can."
    arch "We don’t have the privilege of armor to protect us."
    arch "Only our minds and the will of the gods."

    mc "Father mentioned you needed some help."

    arch "Is that how he put it? Hmph."
    arch " informed him that the village lacked an acceptable militia."
    arch "Nakayoshi used to rally up the men and women and drill them until they were more sweat than skin."
    arch "Hahaha, oh how I miss him. I hope the gods treat him well."
    arch "Alas, now it’s just me. A man too old to fight, training kids how to fight."
    arch "That was the job the late sir gave me, and now, it’s what I do under the new steward."
    arch "And if I get my way, Niyama’s famed bowmen will remain famed."

    sis "So you want us to be the new militia! Are you going to train us?"

    arch "New militia? Hardly. I still have everybody else."
    arch "But you all need to be drilled, and everybody else is busy this time of year."
    arch "I would have preferred the farmhands. Or the hunters. They have better muscle and experience."
    arch "They’re busy planting the crops at the moment, unfortunately, so I asked your father to give me new faces that needed the training. And he sent me you three."

    bro "Marokore, why did you have to choose to come here?!"

    mc "Does the village really need a militia so urgently? I thought the fighting was far from here."

    arch "For now. When the emperor first hoisted his banners, the fighting was distant too. But Lord Fukutaka was called up soon after, and we answered the call of Kamakura."
    arch "So did your father too, but unlike us, he decided loyalty and honor wasn’t for him."

    bro "Hey! He was obeying the emperor and his edict! It’s the Hojo’s fault for opposing him. Maybe you should stop supporting the wrong side!"

    mc "Do you really hate Father for that?"

    arch "A warrior should have honor. There are some who say the family comes above all else, but what is a family dishonored by treachery?"
    arch "Our ancestors and the heavens look down at us and grant us guidance. Do you think they’ll be happy with a runt switching sides for the sake of worldly fortune?"
    arch "I don’t hate your father. For what it’s worth, he’s been a good master. But I can’t simply forgive what he did."
    arch "If anyone can, it'll have to be the Amida Buddha, who forgives all in our illusionary world."

    arch "…But that’s enough of that subject. He is still your father, and I cannot deny that your stalwart defense for your father gives me relief that this younger generation has hope."
    arch "That kid Hoshiko could learn a thing or two from you."

    sis "Mr. Suekuni, you wanted to train us, right?"

    arch "Ah, yes, thank you for reminding me. I’ve started to set up some archery targets."
    arch "I needed to check the archery equipment for the militia, and I suppose you could have the honor of testing them out."
    arch "Now, I don’t just want you three to hit the targets; I want you to become good enough to never miss them."
    arch "Moreover, I forbid chit-chatting during training. This requires perfect concentration."
    arch "Understand?"

    bro "Ugh."

    arch "I heard that. That’s one extra hour for you."

    bro "Agh!"

    arch "Make that two."

    if martial > 5:
        $archerrep += 1
        $martial += 2
        "Your prayers seem to have been answered. As you let loose, the bowstring flexes and the arrow lands on the target."
        "The arrow shakes upon arrival, and Yasumaru groans as you experience success and he does not. Masako grins, and lets out a cheer."
        "Suekuni nods in approval, and a part of you ferociously yells out inside. A warrior’s son, indeed!"

    else:
        $martial += 1
        "The gods, it seemed, are not in your corner today. You thought the angle and technique had been good enough to at least graze the tree, but the arrow swerved around it and instead decided to kiss a pair of bushes. You blush, hoping nobody else saw it."
        "Sadly, Yasumaru’s giggling confirms the opposite. From the corner of your eye, Suekuni frowns and mumbles something. You’re not as angry at him as you are of yourself. Masako looks at you with pity."
        "You go back to practicing, trying to ignore, yet you can’t shake off the feeling that this won’t be the first time you’ll miss."


    show black with fade

    scene bg hills

    "After what seems like hours, you and your siblings are finally told to stop. In empathy, you and Masako decide to share Yasumaru’s extra hours. Everyone is exhausted, and your fingers feel like they’ve gone to the eight hot Naraka Hells."
    "Suekuni offers everyone a drink of water, and you’re too exhausted to drink.  He opens your mouth and pours water in. You can’t even complain."

    show sister left

    sis "Whew… What a day. Can we do this again soon?"

    show brother at right with hpunch

    bro "No!"

    arch "You’ll have to, eventually. If this village is not protected by a force that could scare off the Mongols, then I have failed in my duty."
    arch "The late lord commanded me to protect this village. Training its denizens is, I believe, imperative to its survival."
    arch "I’m proud to say that Niyama is the pride of Kanto when it comes to archers. You’ve seen many around - you know the wonder of a shot from Kawashima, for example."
    arch "That man could surpass me if he didn’t sleep all day."
    arch "Sadly, when the late lord levied us to honor the call of the Hojo, too many winters had passed for me to go with them."
    arch "Can you imagine that? To spend a lifetime training for a moment like that, and just when it feels like I shall happen to live in a period where no great war happens, the emperor and the Hojo decide to settle things."
    arch "Niyama’s contingent was small, for we are no great city. But its sons proved to the realm our worth. Rumor is Fukuyama downed a Sugawara general with one arrow."
    arch "Our lord fell in battle. I remember the day we received the news. We were in shock. A shadow we dreaded to see covered the village."
    arch "And the emperor decided to give your father, who switched allegiances, this village. I can only wonder the next time we are called for battle. A hundred years? Two?"
    arch "I wonder to whom they shall give this village next."

    show black with fade
    "Nobody says a word. And Suekuni goes silent, and gazes solemnly at the mountains. His hand holds onto his talisman, and his mouth utters a silent prayer. You remember hearing that in his youth, he was a pilgrim for years before returning to the village. You wonder what he’s thinking about."
    "At some point, you decided to return home. Suekuni nods in farewell, and your siblings and you start trekking back as the sky begins to darken. You think of the future. What shall come of you?"
    "Is a warrior’s son a warrior too? Would you live in a time of peace, never fulfilling the duty of a warrior? How peculiar, you think, is a warrior who shall never know war."

label help_merchant():
    return
    
# end game
return