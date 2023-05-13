label day_two_travels():
        
    scene bg travel with fade:
        zoom 1.5
    
    "Ah, Kanto. The great east of the land of sunrise."
    "Ancient mountains whose whispers speak of long-forgotten kami and monsters."
    "Azure skies, the dawnbreak piercing."
    "Trees with trunks centuries wide, and with roots that may stretch beyond belief."

    "Ah, Kanto."
    "Where you are bored out of your mind."
    "You’ve lost track of how long it has been."
    "At this point, all you can do is ride the horse painfully slowly until you see another station."
    "Well, no one ever said Japan was small. Well, maybe China has. You’ve heard it’s pretty big."

    "The barely-visible road enters a forest."
    "Thankfully, daylight reaches inside, though shadows swarm the trees."
    "You could throw a pebble and you would never see it again."

    "Minutes pass."
    "The earlier allure of the forest has faded, leaving only the pain of horse riding."

    "You hear a sound."
    "What was that? It sounded high pitched."
    "Wildlife? A person? It came from a deeper part of the forest."

    "A part of you considers ignoring it, but you know you’ll never forgive yourself if you left a person to die."

    menu:
        "I'm no hero, just a man with decency in an indecent world.":
            pass

    "You disembark Ma, and after tying him to a nearby tree, you head off into the direction the sound came from."
    "You bring a bow and quiver in case it’s needed."
    "You also make sure to mark trees with an arrow as you pass them to make sure you know the way back."

    "As you get closer, the sound gets quieter, and you realize it’s also moving."

    "What's going on?"

    "Then, a clearing! It’s not much, and it’s difficult to gaze in these woods, but you think you’ve found the origin."
    "Slowly, you sneak forward, ready to leap and run back."

    "There’s a muffled sound. Now closer, you notice it’s a man!"

    "He’s bound with ropes, including around his mouth, and he is tied next to a tree."
    "Around him are six men with cloaks and hoods."

    "Rudimentary masks cover their lower face. Two of them are clearing out the hostage’s bag."

    "The other four, with weapons drawn, keep a perimeter."
    "Bandits!"

    menu:
        "Your points: martial [martial], charisma [charisma], patience [patience]."

        "Fight: Oh, bless me, Hachiman, god of war! Smite them!":
            jump bandits_fight
        "Talk: Approach them slowly. Words and morals shall triumph.":
            jump bandits_rizz
        "Hold Out: Circle around them; a new angle could be key.":
            jump bandits_circ

screen deathScr:
    text "You died.":
        align(0.5, 0.5)

init python:
    config.underlay.append(renpy.Keymap(mousedown_1=lambda: renpy.hide_screen('deathScr')))

label bandits_fight():
    if martial > 4:
        "Let evil tremble!"
        "You quickly get into an archery position at a distance of around 10 meters, aim, and shoot at one of the bandits keeping watch."
        "The arrow flies true, piercing his neck."
        "You ignore the bile that is building up inside your throat, and quickly notch another arrow."
        "You shoot quickly, as the bandits jump in surprise, and this one hits another’s chest."
        "He goes down."

        "With the element of surprise lost, you drop the bow and grab your sword."
        "You jump forward to meet them in battle."

        "They are not trained, nor are they well-equipped."
        "One rushes forward, screaming, with a pike."

        "You dodge and slice the wooden shaft in half."
        "You block another’s sword slash and slash that assailant's throat."

        "They tried to swarm you with numbers, but they’re getting in the way of each other. A quick stab takes another one down."
        "With three left, they seem to panic, and in that moment you slice another one’s chest."

        "The remaining two seem to recognize their fate, and begin running away."

        "Your blood is pumping, and you start chasing them when men come rushing from the trees."
        "You freeze, thinking reinforcements have come, but their weapons are not aimed at you."
        "The two bandits stop and are quickly rushed by the men, cut down quickly."

        "It looks like everything is taken care of now. You count four newcomers, and their attire seems elegant."

        $martial += 1

        return

    else:
        "Courage, don’t fail now. With a valiant shout, you rush at them."
        
        mc "Hirasada Marakore!"

        "Your sword manages to take out a surprised guard, whose eyes stare at you in sheer shock."
        "But before you can fight off the rest, a pikeman lunges forward, and your breath stops."
        "Cold metal pierces into your stomach."
        "Weakly, you swing at them."
        "But another bandit’s sword swings."
        "You watch the blade coming closer to your head."

        mc "Father, Masako, Yasumaru, I’m sorry. I’m so sorry."

        show black with fade

        "The blade finds its mark."

        show screen deathScr
        pause
        hide screen deathScr with fade

        $renpy.full_restart()

label bandits_rizz():

    if charisma > 5:
        "Perhaps a diplomatic approach is what’s necessary here."
        "You slowly walk out into the clearing, your hands are raised to show you’re unarmed."

        mc "Hello!"

        "The bandits turn to face you. They look surprised. Quickly, they raise their weapons at you."

        b1 "Who are you?"

        mc "Only a simple traveler! I was traveling west when I heard a scream. I thought someone was in danger, and I ran to help."

        b1 "Well, this doesn’t concern you. It’s personal business."
        b2 "Yeah! Go away, bozo!"
        b3 "Bozo? Is that seriously the best you could come up with?"
        b3 "Hey, lay off me, guys. I was just trying-"
        b1 "Shut up!"
        b1 "You, this is personal business."

        mc "I’m only interested in making sure people are safe. Can you promise to let him go after this?"
       
        b1 "Well, we weren’t trying to kill him in the first place."

        mc "That’s good to hear, but you guys still shouldn't resort to banditry. It’s not a very safe occupation."

        b2 "We ain’t bandits! We’re just trying to - err..."

        mc "Huh?"

        b1 "Like I said, personal business."

        "You look closer to the hostage, whose terrified eyes are boring into you. More specifically, you look at his clothes."

        mc "Wait a minute - isn’t that an imperial courtier?"

        "The bandits don’t answer, some glancing at each other uncomfortably."

        b1 "Look, if you gotta know, it’s ‘cause of what he’s carrying."
        b1 "See, this guy is carrying a land deed for some guy called Tanaka. He’s a real mess. No one back home likes him."

        b2 "Aye! Not like Murayama. He’s the old man who was lord before."

        b1 "That’s right. But Tanaka somehow got the emperor to give him the land."

        b2 "And if he becomes the new lord, that ain’t good."

        mc "…That’s all well and good, but what will happen once Kyoto learns of this?"
        mc "You can’t expect that they’ll let this be. You assaulted a courtier. You stole legal documents."

        b1 "Then we’ll fight them off. I’ve seen this whole thing happen elsewhere."
        b1 "Some guy gets land. Or he loses it. Or the temple does. We’re not the only ones taking up arms to fight for ourselves."

        mc "True as that may be, you’re also the first I’ve heard off that dared to attack the messenger."
        mc "A messenger from Kyoto, who’s expected to return too."
        mc "You could have waited for them to hand over the message, and then kill this Tanaka."

        mc "Actually, why don’t you just let him go?"
        mc "Hey, do you promise to let these fellows go unharmed if they let you go?"

        "You hear muffled, but enthusiastic agreement."

        mc "You promise? Yeah, he’s promising it. Plus, he doesn’t know who you guys are. So…"

        "The bandits take the hint. After a quick look at each other, they come to an understanding."
        "With one last glare at the hostage, they sprint off into the woods."
        "As the bandits abandon the clearing, four men leap into it. Better dressed, they calmly walk towards you and the hostage."

        sold "No worries! We're with him."

        $charisma += 3

        return

    elif charisma > 2:
        "You slowly walk out into the clearing, your hands are raised to show you’re unarmed."

        mc "Hello!"

        "The bandits turn to face you. They look surprised. Quickly, they raise their weapons at you."

        b1 "Who are you?"

        mc "That doesn’t matter, but you need to let him go! Or else!"

        b1 "Or else?"

        "They point their weapons at you. Well, you tried."

        menu:
            "Run for the forest. The courtier can take care of himself.":
                pass

        "But just as you exit the clearing, a quick hiss catches your attention."

        unknown "Who the hell are you?"

        "Looking at you are four men hiding behind trees. They’re armed, and completely dumbfounded at your presence here."

        mc "I heard some screams, and I was checking it out. Are you guys going to rescue them?"

        ret "We're his retainers."

        mc "Doesn’t seem like you’ve done a good job."

        ret "Oh, shut up. They got him in the middle of the road."
        ret "We’ve been chasing them for like an hour. These guys were waiting for us to get close to the forest to jump us."
        ret "We don’t know who they are, or why they’re doing this."
        ret "We’re in the midst of planning a rescue operation, as you can see."

        mc "And how’s that going? Not so great?"

        ret "Could say the same for you."

        mc "Want to team up?"

        ret "Well, if you’re offering…"

        mc "Ok, I’ve got a plan…"

        "It’s really not that much of one, but they listen. Soon, you all take your positions."
        "You begin. You notch an arrow and shoot it to the first bandit, hitting his chest."
        "The five remaining bandits are all lackluster, but the four retainers aren’t the most courageous either."
        "Your group is better trained, though."
        "Quickly, you overpower your opponent. With regret that you push down, you cut him down with your sword."

        "You see that the others continue their fight."
        "For a second, you contemplate letting them finish their own."
        "But the possibility they might fail pushes you towards defeating the bandits from the back."
        "Soon enough, the six bandits lie dead, and everyone scrambles to untie the hostage."

        $charisma += 1

        return
    
    else:
        "You slowly walk out into the clearing, your hands are raised to show you’re unarmed."

        mc "Hello!"

        "The bandits turn to face you. They look surprised. Quickly, they raise their weapons at you."

        b1 "Who are you?"

        "You strike a heroic pose."

        mc "I am the emissary of justice! Hero of the land! The voice of the weak!"
        mc "Scourge of the earth - harken my words: release your prisoner, or face my righteous wrath!"
        mc "It is I - the Maskless Rider!"

        "Wait, are they starting an attack?"
        "Before you can react, their weapons pierce you."

        scene black with fade

        "In your final moments, you can but wish that maybe you needed better speech-writing skills."

        show backg:
            zoom 2
        show screen deathScr
        pause

        $renpy.full_restart()

label bandits_circ():
    "Going out into the clearing without a second-thought would be suicide."
    "With an apologetic look at the hostage, you decide to not charge."
    "But that doesn’t mean you’re giving up."
    "Instead, you decide to circle around the small clearing. Maybe there’ll be an angle where you safely snipe arrows."

    "Wait a minute."

    "Just in front of you, there are four men hiding behind some trees, tightly holding their swords."
    "They’re intently glaring at the bandits. Are they rescuers?"

    mc "Psst!"

    "They turn in surprise. You hold your hands up to show peace, and tip-toe towards them."

    mc "Hey, what's going on?"

    unknown "Who the hell are you?"

    mc "I heard some screams, and I was checking it out. Are you guys going to rescue them?"

    ret "We’re this guy’s retainers."

    mc "Doesn’t seem like you’ve done a good job."

    ret "Oh, shut up. They got him in the middle of the road."
    ret "We’ve been chasing them for like an hour. These guys were waiting for us to get close to the forest to jump us."
    ret "We don’t know who they are, or why they’re doing this."
    ret "We’re in the midst of planning a rescue operation, as you can see."

    mc "And how’s that going? Not so great?"

    ret "Could say the same for you."

    mc "Want to team up?"

    ret "Well, if you’re offering…"

    mc "Ok, I’ve got a plan…"

    "It’s really not that much of one, but they listen. Soon, you all take your positions."
    "You begin. You notch an arrow and shoot it to the first bandit, hitting his chest."
    "The five remaining bandits are all lackluster, but the four retainers aren’t the most courageous either."
    "Your group is better trained, though."
    "Quickly, you overpower your opponent. With regret that you push down, you cut him down with your sword."

    "You see that the others continue their fight."
    "For a second, you contemplate letting them finish their own."
    "But the possibility they might fail pushes you towards defeating the bandits from the back."
    "Soon enough, the six bandits lie dead, and everyone scrambles to untie the hostage."

    $martial += 2
    $charisma += 1

    return

label getting_invitation():
    "As soon as the rope gagging his mouth hits the ground, the ex-hostage begins talking."

    show hostage

    exh "What took you all so long? They were an inch away from slitting my throat!"
    exh "Why did I even hire you four?"

    ret "Technically, my lord, your father did."

    exh "Of course he did, fool. My father knows all the proper precautions a well-doing courtier must take."
    exh "He taught me all his tips and knowledge."

    "He turns to you and gives a curt bow."

    exh "Oh, please forgive me for my late greeting. I was a bit preoccupied."
    exh "My name is Takayuki, pleased to meet you."

    "After a mental hiccup, Father’s etiquette lessons come crashing back. You bow deeply."

    mc "My name is Hirasada Marakore, it is a pleasure to meet you!"

    "He’s a courtier, so he’s probably high up in the chain. It wouldn’t be wise to be disrespectful."

    tak "I thank you for helping save my life. Those akuto, those evil men. Japan would be better off without them!"
    tak "Just robbers and plunderers, despoiling our great estates."
    tak "If there is anything I can do as a favor, I promise to grant it as swiftly as possible."

    mc "Oh! Your offer honors me considerably, though-"

    tak "Aha! I know what you want."

    mc "You do?"

    tak "Yes, because it’s the very thing that I would want if I were in your place. Now, do please allow me a minute."

    menu:
        "Is this an answer from the universe? You take the piece of paper he holds out.":
            pass

    mc "Oh, thank you, sir. I am honored beyond…"
    
    "You stare at the paper. Is…"
    "Is he serious?"
    "This…"

    tak "Oh, I understand your shock. I remember the first time I was granted a privilege like this."
    tak "That’s right, this is a letter of recommendation for a party hosted by the Hino family."
    tak "They’re a meika household, so it’s truly amazing for a country bumpkin like you to even be allowed to enter their estate."
    tak "It took many years even for me, and for my hard work to be recognized by Kyoto’s peers."
    tak "You are aristocratic, right?"

    mc "I am a bushi, son of a Jito."
    mc "My father holds a predominant position in the village of Niyama, granted his titles by the hand of the emperor."

    tak "Oh, amazing, to be saved by a young, dashing noble warrior from the eastern country!"
    tak "I feel giddy at this wondrous happenstance. What a perfect tale to recount to Kyoto."
    tak "Oh, what a shame I shall be absent for the foreseeable future. A messenger courtier must deliver their messages, you see."
    tak "I can only hope to finish in time to reach the party."
    tak "Trust me, country-warrior, Kyoto’s parties are a must-die for. Really, try out kemari."
    tak "You've heard of kemari, right?"

    mc "Kemari? Do you mean the game?"

    tak "Oh, so you do know it! Wow, I’m overjoyed to see that the peers afar are cultured too."
    tak "And you know how to drink tea, yes?"

    mc "Of course. I was taught the tea ceremony from a young age."

    tak "Oho, it appears I’ve just won a bet against a colleague of mine."
    tak "He claimed rural folk do not even know how to properly take their tea."
    tak "I feared that it could be possible, but bless you for winning me a gamble."

    mc "Happy to help."

    "You began to regret saving him."

    tak "The party will have everyone! Bureaucrats, warriors, temple heads."
    tak "I don’t recall the occasion at this moment, but I’m sure it’s for a great cause."
    tak "Or perhaps not. Do you need a reason to celebrate?"

    mc "Usually."

    tak "Mhm, you might be right. There’s some good, reliable rustic wisdom."
    tak "But the most I’ve found in my experience are smelly ranches and a lack of good food."
    tak "My, can you believe people actually live like that? I wouldn’t want to be a commoner."

    mc "It grows on you, I’ve found. You should try helping the fields occasionally."
    mc "Builds good strength. And character."

    tak "Yes, my brother does keep telling me to stop and smell the roses."

    "Oh, gods, why did I save him?"

    mc "I’m heading to Kyoto at this very moment, so–"

    tak "You are? Oh, I’m so sorry, I can’t believe I was stopping you from that."

    mc "And you also have a job, right? It might be best not to dither."

    tak "You’re a brilliant fellow!"

    "With a haughty laugh, Takayuki dismisses me and walks out, following his guards who look at me apologetically."
    "The leader mouths thank you, and you nod to him in recognition."

    hide hostage with moveoutright

    menu:
        "Return to Ma, following the tree trunks you had marked earlier.":
            pass

    "And with that, today comes to a strange end."
    "Untying and feeding the apathetic horse a snack as an apology, you remount your trusty companion and continue on your way."
    "Thankfully, it seems all your possessions are still on Ma."

    "You take a look at the letter Takayuki gave you."
    "It’s a short notice that includes a daring rescue that reads as more fiction than fact."

    "He made it sound like a big deal. You contemplate whether to go."
    "On one hand, it’s not directly linked with your mission."
    "However, if some bigshots attend, then you might find some crucial key for keeping your family’s claim."
    "Plus, it’s always good to be in the know of current trends."
    "Regardless, you have time to ponder more until you reach Kyoto."
    "And looking at the letter, the date appears to be some time away."
    "As you and Ma trot along the road, the forest fades into an azure-opal sky."
    "Sunset is approaching, and you look at the emerging stars. You wonder if your family is looking at them as well."

    scene black with fade

    "The wind whistles in your ears, and the grass rustles in its wake."

    return


return