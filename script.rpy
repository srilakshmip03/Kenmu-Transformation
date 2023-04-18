# The script of the game goes in this file.

# main
define mc = Character("Marakore")
define sis = Character("Masako")
define bro = Character("Yasumaru")
define dad = Character("Father")
define fish = Character("Akiyoshi")
define merch = Character("Nagamoto")
define arch = Character("Suekuni")

define unknown = Character("???")

define sold = Character("Soldier")
define osold = Character("Other Soldier")
define b1 = Character("Bandit")
define b2 = Character("Bandit 2")
define b3 = Character("Bandit 3")
define ret = Character("Retainer")
define exh = Character("Ex-Hostage")
define tak = Character("Takayuki")


define rival = Character("Shigefumi", color="#F00", who_outlines=[(3, "#000000", 1, 1)])

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

screen dayOne:
    text "Day One":
        align(0.5, 0.5)

init python:
    config.underlay.append(renpy.Keymap(mousedown_1=lambda: renpy.hide_screen('dayOne')))

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

    show screen dayOne
    pause
    hide screen dayOne with fade

    show black

    "Typically, there are several ways you wake up in the morning."
    "Father giving three self-assured raps at the door. Somehow this always immediately snaps your mind to attention."
    "Your brother Yasumaru ignoring the concept of knocking all together, barreling into your sleeping form, unkempt fabric catching light as he hurriedly reminds you of the events that day… as if you hadn’t already been aware of them."
    "Your sister Masako running across the wood floors, unceremoniously knocking that worn down sword into your bedroom wall as she passes."
    "You silently listen for signs of life…"
    "…before concluding that this would indeed be a special morning."
    "Light footsteps echo as you shuffle outside, where your family is dining."


    scene 
    show bg home with fade:
        zoom 1.5

    show brother at left with moveinleft

    bro "Marakore! You’re finally awake!"

    show father at right with moveinright

    dad "Seat yourself, please. A warrior contains himself."

    dad "You're awake."

    mc "Yes, Father, good morning."

    "Is there a reason the sun's so high and I'm still in my sleeping gown?"

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

    scene
    show bg home with fade:
        zoom 1.5

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
    scene bg river with fade:
        zoom 1.5

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

    menu:
        "Stat check: patience is [patience]"
        "Start trying to catch fish.":
            pass

    if patience > 5:
        $fisherman += 2
        $patience += 2
        "It takes a while. You almost wanted to give up, after what seems like half an hour, but suddenly the trap shakes. You blink, and realize there’s a fish! You grasp tightly, and hasten to pull it up strongly."
        "It doesn’t take much - you almost redden for thinking you wouldn’t be strong enough to wrestle a fish - and the fish comes flying up, landing on Yasumaru’s face. You ignore his yelling. You spot Akiyoshi laughing and grinning."
    else:
        $patience += 1
        "It takes too long. You try to wait it out, but you just can’t handle it. There’s simply no fish at all! How do fishermen catch these things?"
        "You sigh and pull back the trap. Yasumaru hasn’t caught anything, and Masako is still trying to skewer the water. You feel some disappointment, and judging by Akiyoshi’s face, so does he."

    "Despite this being one of the more relaxing atmospheres of the village, you felt there was an undercurrent of unease with Akiyoshi. You couldn’t put it into words."
    mc "Akiyoshi? I was wondering if…"

    fish "Yes?"

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

    jump rival_scene

label help_archer():
    scene 
    show bg hills with fade:
        zoom 1.5

    show brother at left with hpunch

    bro "-AHHH!"

    show sister at right

    sis "AAH! What is it?!"

    unknown "Huh."

    "From the corner of your eye you can see a shadow drop down from the treeline, trailing fabrics signaling to you the wearer’s identity."

    mc "Yasumaru are you okay?"

    bro "I could have died!"

    show archer zorder 3
    show brother at left zorder 2
    show sister at right zorder 1

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

    "Suekuni grasps a talisman and quickly offers a prayer. It feels inappropriate to stay angry at a pious man, and you suspect this guy knew it. "

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

    menu:
        "Stat check: martial is [martial]"
        "Aim carefully at the practice target, and shoot.":
            pass

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

    hide archer
    hide brother
    hide sister

    show black with fade

    scene bg hills with fade

    "After what seems like hours, you and your siblings are finally told to stop. In empathy, you and Masako decide to share Yasumaru’s extra hours. Everyone is exhausted, and your fingers feel like they’ve gone to the eight hot Naraka Hells."
    "Suekuni offers everyone a drink of water, and you’re too exhausted to drink.  He opens your mouth and pours water in. You can’t even complain."

    show sister at left

    sis "Whew… What a day. Can we do this again soon?"

    show brother at right with hpunch

    bro "No!"

    hide brother
    hide sister
    show archer

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
    "Nobody says a word. And Suekuni goes silent, and gazes solemnly at the mountains. His hand holds onto his talisman, and his mouth utters a silent prayer."
    "You remember hearing that in his youth, he was a pilgrim for years before returning to the village. You wonder what he’s thinking about."
    "At some point, you decided to return home. Suekuni nods in farewell, and your siblings and you start trekking back as the sky begins to darken. You think of the future. What shall come of you?"
    "Is a warrior’s son a warrior too? Would you live in a time of peace, never fulfilling the duty of a warrior? How peculiar, you think, is a warrior who shall never know war."

    jump rival_scene

label help_merchant():
    scene 
    show bg street with fade:
        zoom 1.5

    "You decide it best to assist Nagamoto in his endeavors. After all, there’d be no better way to learn of the current happenings outside the village than by visiting the eccentric merchant."
    "Hearing your decision, Yasumaru leaps for joy, stomping his worn-down waraji on the rocky terrain."
    "You all arrive quickly to the shop, a cluttered place built using wooden shelves which contain all sorts of novel trinkets - some even distinctly Chinese!"
    "Being in the center of town provides easy access for villagers and traders alike to browse the expansive selection. The front door is wide open which surprises you, knowing how particular Nagamoto is."
    "You stall by the entryway, spotting a steady pair of gleaming yellow eyes staring from the shelf directly opposite your position. This, of course, prompts Masako to gleefully walk inside."

    show sister at left with moveinleft
    sis "Minori!"

    mc "Don’t just waltz in like you own the place!"

    show brother at right with moveinright
    bro "Nagamoto? Helloooo?"

    "You watch in disappointed acceptance as both your siblings make their way through the store anyway."
    "It seems Yasumaru doesn’t have as light a step as his sister, as the floorboards creak noisily as he enters."
    "You decide you might as well join them, and you begin scanning for the merchant."

    mc "Well, the cat’s here, so he couldn’t have gone far."

    "You pass by the cat-sized basket that you always spot the merchant wearing before embarking on extended trips. You hear a sigh from your sister."

    sis "Her name is {i}Minori{/i}, I’ll have you know."

    bro "Where could he be? I need that new cooking pot!"

    "Right as he speaks, you hear the floorboards creak once again behind you."
    "You whip around to find the merchant staring wide-eyed at all three of you."

    show merchnocat

    merch "…New cooking pot just came in."
    
    "He gestured to a wooden crate behind you, and in a flash your brother was behind you and digging through it."

    mc "Hello, Nagamoto! Father said you might need help with new shipments?"

    merch "Help, eh? Yes."

    "He shuffles around the room, picking up items from crates and stashing them in various ways. Sometimes in other crates, sometimes in displays on the shelves."

    sis "Why were you gone just now?"

    merch "Busy season."

    "Masako glances at you in confusion. You return the look but press on."

    mc "I’m guessing you need help organizing all these containers."

    merch "Already organized. I need help moving them outside for trading."

    bro "Can I wear these?"

    "He proudly holds up a new pair of waraji."

    mc "Sure. You’re paying me back when you’re older, though."

    sis "HA!"

    bro "Hmph. You'll forget by then anyway."

    "You begrudgingly hand over some coins to the merchant."
    
    mc "Pleasure doing business with you. Now come on, we’re losing daylight."

    "You and your siblings spend time hauling heavy crates and peculiar knick-knacks outside while Nagamoto sets up a large canopy."
    "You glance up and see a clear sky, and take note of the cool breeze fanning past you."
    "You wonder for a bit if the paranoid merchant was able to predict the upcoming weather, but you’re shaken from your thoughts as three men approach the store."
    "You feel like you recognize their armor from a certain city, but you couldn’t be sure."
    "The sets were clearly battered - enough so that you couldn’t be certain if you recognized their design."
    "As they approach, Nagamoto stays still, eyes wary. In contrast, both your siblings are buzzing to see soldiers so up-close. You wonder whether you should speak…"
    "One of the soldiers approaches. He looks around, as if sensing the tension."

    sold "We mean no trouble, only looking to fix some things."

    "Everyone calms down a little. You’re still a bit suspicious, but maybe they'll leave once they get what they want."
    "Nagamoto straightens and adopts a friendly mercantile persona. Seems business comes first."

    merch "Oh, sirs, that shall be no problem at all! I’ve collected great treasures and goods from all over Japan!"
    merch "What will it be today? Shoes? Boxes? Or more armor again?"

    sold "Actually, armor is precisely the reason we came."
    sold "Not for a new one, but about the ones you sold us. Say, you know the lord of this land?"

    merch "Oh, I understand sirs! No, sirs, I am not."
    merch "You want to do business with him, yes? He’s the Jito’s son."

    sold "That’s right. It’s nothing personal, but I can’t exactly trust you to be a man of your word, considering the shoddy thing you gave us."

    sis "Sounds pretty personal to me..."

    merch "Yes, sirs. Uhh, thankfully, my lord here is able to handle all business, you see."
    merch "Yes, he can. Please, thank you very much, forgive me."

    "The soldiers turn to you and bow respectfully."

    sold "This merchant sold us some armor some weeks ago. We weren’t expecting fine-grade, of course, but we at least expected it to block simple attacks from bandits."
    sold "But this guy’s material is utter trash! That’s how they got a buddy of mine. Bandits! What kind of armor can’t block a light tap?"
    sold "So, as the overseer of this town, we’ll like you to mediate this case."
    sold "We want him to pay recompensation for a bad product. And a replacement! A good one this time."

    "…What? Is that what Nagamoto was doing? Selling bad armor? You look at the soldiers’ armor, and it does appear damaged and in poor condition."
    "But was it the armor or the fighting? Nagamoto turns to look at you, and you see a panicked expression. But his eyes also have an expectant fire."
    "You know what he’s trying to say: don’t mess this up for me!"

    menu:
        "Stat check: charisma is [charisma]"
        "Walk forward, thinking about what to say.":
            pass

    if charisma > 5:
        $merchant += 1
        $charisma += 2
        mc "Welcome, guests. I apologize for our lack of preparation. I am the son of the Jito of this village."
        mc "Any business I handle will be passed to him. You wish to make a complaint about this man?"

        sold "Yes."

        mc "Yes, dangerous times and all. Not many have the wisdom to protect themselves ahead."
        mc "Thankfully, our merchant friend here has acquired a reputable source for armor, and has it currently in stock. The only question is, which did you purchase?"

        sold "Which?"

        mc "Of course, not all armor is made equal. Different material, strength, quality. Some are ceremonial, some practical."
        mc "Nagamoto, do you remember what it is you sold?"

        merch "Er, yes! It was a dō-maru made of iron and leather, made by a young armorsmith named Kurosawa."
        merch "He’s a bit inexperienced, and it was a bit rushed…"

        sold "Rushed?!"

        mc "Rushed?"

        merch "Well, I mean, I thought that, well, you see, the thing is, I thought it was necessary to have any armor at all rather than none?"

        sold "So you gave us bad armor?"

        mc "Now, wait a minute. Nagamoto, did you make it clear that this was a rushed-job?"

        merch "Well, yeah. I was trying to sell them the really good one, from a pair which was really expensive - really!"
        merch "But they wanted the cheapest one."

        mc "Is this true?"

        "The soldier reluctantly nods."

        sold "We didn’t have the funds for the best, but we expected what we got would help."

        mc "Bad armor tends to have mistakes. Armor is time-consuming and resource-heavy."
        mc "For something like this, I assume some of the scales were improperly attached, or some sides of the body left unguarded for mobility."
        mc "So what you purchased would have protected you from the majority of light blows, but all that was needed was one to sneak through."
        mc "Tell me, how did your compatriot die?"

        sold "… He was shot with an arrow from the side. Somehow, it pierced him."

        mc "I’m sorry for your loss. But considering the situation, I find it difficult to accuse this merchant of selling false-advertised armor."
        mc "He made it clear it was cheap, though I will warn him to be more transparent in future transactions. Your comrade simply had bad fortune."

        merch "However, if you’re still looking for protection, may I recommend-"

        mc "Not right now, please."

        "The soldiers quietly accept your ruling, but you don’t feel all that happy about it."
        "You offer them a night at the inn, but the soldiers politely decline and depart the village."
        "Looking at you in sheer gratefulness, Nagamoto rushes forward to thank you profusely, and your siblings clap in awe."
        "You’re not sure if they’re trying to mock you, though..."
    else:
        $charisma -= 2
        "Your brain doesn’t give any tips. Your breath hastens, and you scramble something. Being direct makes things easier, right?"

        mc "It’s not this merchant’s fault you buddy got wasted."

        sold "...I'm sorry?"

        mc "You heard me, it's not his fault."

        sold "We were trying to be respectful, but if that’s how you treat guests with grievances, we’ll just take our business elsewhere!"
        sold "Let’s go! We’ll go see your father instead. Maybe he’ll be a better arbitrator"

        osold "But Karentaro, we need-"

        sold "We will not be disrespected!"

        "The soldiers leave, and you look back at everyone. They look dumbfounded."

        bro "Well, at least what was quick."

        "Nagamoto is speechlessly lamenting over his lost transaction, and you shrug helplessly."
        "You and the rest silently decide to take a breather for what feels like an hour hoping to ignore what just happened."
        "Doesn’t help the awkwardness, though."

        "Eventually, Nagamoto stands up, and sighs. He probably hasn’t forgiven you, but maybe he’s realizing you’re not the one who’s a merchant for a living."
        "The extent of your negotiation skills is convincing Yasumaru not to tattle on you."
        "Everyone continues to help transport his products., which you all eventually manage to get done."

        merch "Well..."

    merch "I wouldn’t have been set up in time had it not been for your help today. Thank you."

    mc "It was nothing."

    merch "Appearances are… important."
    merch "Especially selling things like armor and weapons. People rely on you to sell a good product, and it really is life-or-death."
    merch "..."
    merch "One time, a soldier’s mother came to my store. It was late, and I couldn’t see her expression too well."
    merch "She grabbed me and begged me to answer about the quality of my armor. Didn’t know what to say."
    merch "I froze. And that was enough of an answer for her."

    merch "..."

    merch "Never saw her again, but I think about that night often."
    merch "What could I have said at that moment? I know my armors’ fortitudes, I know my weapons’ durabilities."

    mc "So you’re selling armor for the sake of altruism? To save lives?"

    merch "And the money, too. It might sound greedy - actually, no, it’s very greedy - but I need the money."
    merch "A merchant has to rely on selling what people need, even if it’s for a horrible situation."
    merch "I doubt gravediggers do their job because it’s all joyful parties to them."
    merch "The job needs to be done by someone, and it might as well be me."

    sis "Still, armor? That’s pretty expensive."

    merch "You’ll be surprised by what people fearing for their lives will pay. There’s been a lot of banditry and conflict lately."
    merch "That war-boom we merchants enjoyed a few years ago waned, and a lot of the smiths learned new crafts for a war that ended too soon."

    bro "Too soon? Isn’t war supposed to be bad?"

    merch "Well, yes, but for merchants like me, actually no. You see, whenever there’s a war, industries relating to war supplies get a boost in revenue."
    merch "More people need them, and producers are more than happy to supply it."
    merch "The best dyers and leatherers are in Aki, bowmakers in the west, where the good bamboo is, and the finest horses bred in the rugged pastures like Shinano."
    merch "Of course, Kyoto is at the center of this weapons trade, and you’ll find the best armorsmiths there too."
    merch "Best thing is, wars are expensive for soldiers and commanders. Which means we merchants and smiths get rich."
    merch "The biggest thing to worry about is security, but you can hire protection, and they need to buy armor and weapons too."
    merch "Plus, common goods also get pricier."

    sis "I'm not sure I like how excited you're getting."

    merch "Bah, you wouldn't get it. Which, you know, I understand."
    merch "You’re a warrior, you fight, you face danger. And the common man also faces things like starvation, or pillaging."
    merch "But that’s what’s genius about being an ever-moving merchant - you can always move out of danger."

    show black with fade

    "You suppose that’s one way of looking at conflict. Personally, all you can think of is Father’s weary expression."
    "But at least some people are making some good money off it."
    "With the job done, you and your siblings head off, saying farewell to Nagamoto."
    "The heavy topic wears down on everyone, but as Yasumaru skips with his new shoes, you hope that this town won’t have to experience anything that demands armor."

    jump rival_scene

label rival_scene():
    call rivalscene

    scene 
    show bg rival:
        zoom 1.5
    show rival zorder 3

    "As Shigefumi turns to leave, he spits out one last remark."

    rival "You’ll regret having come here once I get my claim recognized at Kyoto."

    "Shock paralyzes you as you realize what he just said."

    show sister at left zorder 2
    sis "Claim? What claim?"

    "She has a certain disconnected look on her face which you find odd."
    "But that can wait until later. You don’t feel safe anymore."
    "You gesture for Yasumaru and Masako to follow you as you make a beeline for home."

    hide rival with moveoutright

    mc "We’ve got to tell Father!"

    "While setting a quick enough pace for your siblings to follow, you get to thinking."
    "Claim? Could he be bluffing? What does this mean for our family?"
    "Thoughts rattle around your brain until nervousness properly sets in."
    "‘I cannot let this happen’ is the conclusion you come to as you approach your lantern-lit house."
    "Your siblings don’t say a word, but you can feel the worry emanating off of them all the same."

    scene 
    show bg home with fade:
        zoom 1.5

    "You quickly take your shoes off and open the door."

    mc "Father-"

    show father at right zorder 3
    with moveinright

    dad "You're all back!"

    "He was meditating. You feel guilt wash over you as you think of how to word what just transpired."

    dad "You all seem nervous… What happened today?"

    show sister at left with moveinleft

    sis "We met Fukataka Shigefumi on the road back home from helping the villagers."
    sis "He seemed.. angrier than usual."

    bro "You study his face that much? Gross."

    mc "He said he’s going to get his claim recognized at the capitol."
    mc "I don’t know when or how, but he seemed… genuine about it."
    mc "Like it wasn’t a threat, more of a… promise."

    "Father was silent. You stare down at the floor, not being able to bear looking at him."
    "When you glance back up, you notice his face seems… resigned."
    "And the fatigue is back in full force."

    dad "I knew tensions were high with that family. The way his mother looks at me in the street…"
    dad "You must go to Kyoto."

    show bg home with hpunch

    "...What?"

    bro "What?" 
    sis "Huh?"

    dad "This is the only way."
    dad "If he takes this claim all the way to the top, then our land rights could be ripped away from us."
    dad "We obtained our position in the village through the emperor’s will, and by his will it can be taken away."
    dad "Legally, all that stands between us now and us left destitute is the emperor’s humoring."
    dad "He’s unlikely to even remember me."
    dad "If that boy somehow convinces the emperor that he would be a better, more loyal servant..."
    dad "There’s nothing that can stop it."
    dad "Unless, of course, there is someone in Kyoto that can defend us."
    dad "Until the government regains stability, we can’t be too careful about things."
    dad "I’ll give you enough supplies and advice as you need, but you must leave tomorrow."
    dad "You must ensure that our claim is the only one recognized."

    "You're stunned."
    "Father looks like he's aged a hundred years, and his voice has dried in anxiety."
    "You can but share that fear."
    "The adrenaline is helping you understand your father better, though."
    "You must do whatever it takes for your family."

    bro "I'm so excited!"
    sis "I wonder if I can test my skills on real soldiers!"

    "Father gives them a look, and you feel a weight drop in your stomach."

    dad "Marokore must do this on his own."
    dad "More of you will be… risky. I need you here, where you’ll be safe."

    "Yasumaru and Masako instantly deflate."
    "You feel torn. On one hand, this would be the first time ever separated from your family."
    "Even when Father was fighting, you three were under the care of your grandparents."
    "But Japan didn’t feel safe lately, and you worried that bringing them along would only endanger them."

    sis "Okay..."

    bro "I never get to go out to explore."

    sis "You get to explore the village!"
    
    bro "Still..."

    dad "Kyoto isn’t going anywhere. When you’re older, we’ll all take a trip there."
    dad "Right now, Marokore needs rest, however, so let’s all retire for the night."

    menu:
        "Heed his request and head to your room.":
            pass

    hide sister with moveoutleft
    hide father with moveoutright

    jump departure

label departure(): 
    show bg home with fade:
        zoom 1.5

    "As you ponder over which clothes would be the most practical for the journey, you hear a knock on your door."
    show brother at left with moveinleft

    bro "Hey, Marokore."

    mc "Yasumaru? Are you okay?"

    bro "Could I.. come in?"

    "You gesture for him to enter, carefully watching his expression."

    "It’s rare for your brother to be so quiet outside of complying with Father’s requests."
    show brother at center with move

    
    "He walks forward, stopping in the middle of the room."
    "You notice him fiddling restlessly with the sleeve of his sleeping robe."

    bro "About Mother..."

    mc "Yasumaru. It's okay."

    bro "No, I… I was just thinking about what Suekuni said today. When he shot that arrow above me."

    mc "You never intended for her to die. How could you have?"

    bro "I know I didn’t. It’s just, it feels like what he said was a demonstration of how a lot of people see me in this village."
    bro "You knew Mother too, but you don’t see me in that way. You’re kind to me, and you want to support me."

    mc "As does Father."

    bro "Sometimes it feels like he supports me {i}too{/i} much."
    bro "My point in all this is, please come back. Safe."

    mc "You don’t need to worry about me."
    mc "I’ll be home before you know it, and with a legitimate claim that Shigefumi can’t deny."

    "Yasumaru runs up and hugs you tightly. You cherish this rare moment with him."

    mc "It's late. You should get to bed."

    bro "You too."

    show black with fade

    "He leaves."
    "You finish picking out clothes for the trip and quickly fall asleep."
    "You don’t exactly remember afterwards, but you think you dreamt of doves flying and the clashing of swords."
    "As you try to sleep, you recall once telling Mom you wanted to become a seagull, and fly all over Japan."
    "It feels like divine mocking to be able to explore Japan now..."
    "...but alone and with the burden of the family’s future weighing on your shoulders."

    jump day_two

screen dayTwo:
    text "Day Two":
        align(0.5, 0.5)

init python:
    config.underlay.append(renpy.Keymap(mousedown_1=lambda: renpy.hide_screen('dayTwo')))

label day_two():
    show black

    show screen dayTwo
    pause
    hide screen dayTwo with fade
 
    scene bg home with fade:
        zoom 1.5

    "You awake the next morning to a knock on the door."
    "Getting up was difficult after yesterday’s sleep in, but you manage anyway."
    "Your sister is there to greet you."

    show sister at left with moveinleft
    sis "Marokore! The time has come."

    mc "Hey, it sure has. How are you feeling?"

    "You can tell she’s jealous, she’s not very good at hiding it."

    sis "Ohhhh I’m good, ya know! Love this village, love it so much I may die here."

    mc "You’ll have the chance to travel at some point! There’s much to see out there that’s waiting for you."

    sis "Yasumaru also wants to come. I really think Father’s being too strict on us."

    mc "Whatever you may think, his rules are the rules. I’m very sorry though, Masako."

    sis "It’s alright. Like you said, I’ll be able to travel when I’m older."
    sis "By that point, I’ll be trained as a warrior!"

    "As she lifts her arms up in a mock fighting stance, you’re able to see the famed wooden sword hiding once again in her robes."
    "She lowers them once more to speak."

    sis "Father’s outside waiting for you. He asked me to get you."

    mc "Thank you. Come say goodbye."

    "You take a moment to yourself to dress in the day’s clothing, stretching a bit to make sure they fit nicely."
    "Then you and Masako head outside the house, Yasumaru trailing behind you both."

    show father at right with moveinright
    "Father’s waiting there by a gray horse with various pouches and bags attached to its saddle."
    "As he spots you all, he smiles softly."

    dad "Thank you for retrieving him, Masako."
    dad "How are you feeling, Marokore? I made sure to pack extra food and water, as it has…"
    dad "...been a while since I made this trip. My memory gets rusty, after all."

    "He laughed softly. You commit its sound to memory."

    mc "I’m ready, Father! Slept well, and I’m feeling strong enough."

    dad "Very good. This is Ma."
    "He gestures to the horse."

    mc "The horse is named horse?"

    dad "Your old man has never been the best at naming things, I’m afraid."

    "Another laugh. Father’s spirits are higher than they usually are. It’s very nice to see."

    dad "Don’t worry, I’ve packed some armor on Ma, so you’ll be safe."

    mc "Wait, do you mean yours? I can’t! It’s too valuable to risk it…"

    dad "You’re more valuable than some pieces of metal."
    dad "Take your sword and bow with you at the ready."
    dad "Those akuto and bandits shouldn’t dare to strike at an obviously trained Bushi, but you shouldn’t risk it."
    dad "Keep your eyes wide open. Especially when you’re preoccupied with your… business."

    mc "Father!"

    dad "Oh, I’m sorry, did I embarrass you?"

    mc "No, no! It’s just…"

    dad "I understand."
    dad "When I went to war, I feared every day would be my last. I was always thinking of you three."
    dad "What would your mother think of me dying so far away from you?"
    dad "Whatever happens, stay safe."
    dad "Our titles, our land, all of that is inconsequential compared to your wellbeing."
    dad "Don’t ever forget that."

    "You can’t say anything. Instead, you hug him, trying not to tear up."

    show sister at left zorder 3
    show brother zorder 2:
        xalign 0.4
        yalign 1.0

    show father at right with hpunch

    "Suddenly, Yasumaru and Masako both barrel into you from behind, hugging you tightly."

    mc "Ack-!"

    bro "Come home safe, Marakore. Please!"

    sis "Won’t be nearly as fun around here without you! Especially with just this runt."

    bro "Hey!"

    "You smile as they continue arguing while holding on to you."
    "But you eventually separate away from them and take the reins from Father."

    dad "The journey will be long. Don’t lose sight of your goal."

    "You take a moment to bow deeply to him."

    mc "I would never. I’ll see you soon, Father."

    dad "Safe travels, my son."
    dad "And if you run into Shigefumi on the road, try talking with him. See if you can’t change his mind at all."

    mc "I'll do my best."

    "You weren’t sure how realistic that would be."
    "But you put that thought to the side for now and say proper goodbyes to your family."

    "You hop on your new companion Ma, and head to the main road leading out of the village."

    scene black with fade

    "Heart pounding with hands gripping tightly onto the reins, you leave your village alone for the first time."

    call day_two_travels
    call getting_invitation
    jump continuation

label continuation():
    screen tbc:
    text "Act Two: to be continued...":
        align(0.5, 0.5)

    init python:
        config.underlay.append(renpy.Keymap(mousedown_1=lambda: renpy.hide_screen('tbc')))

        show black

        show screen tbc
        pause
        hide screen tbc with fade

# end game
return









