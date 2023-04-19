label rivalscene():
    scene bg rival with fade:
        zoom 1.5

    "You didn’t realize how dark it was getting as you steadily walked home, siblings trailing behind you."
    "For some reason, you felt a chill pass within you despite the warm evening air." 

    show rival zorder 3 with moveinleft
    unknown "What are the traitors doing here?"

    "Ah. That’s why."
    "Farther down the path you saw a boy around your age, sneer marring his face, as he marches towards you and your siblings."

    show brother at right zorder 2
    bro "Not again!"

    "You hold your arm out in front of him. You are going to deal with this."

    hide brother

    rival "Hear me! I am Niyama’s Fukataka Shigefumi. Rightful claimant to my father’s titles of Jito and all other held rights."
    rival "Your father stole them from mine through betraying his own and switching sides, and I shall take my vengeance."

    "Shigefumi. He’s the son of the previous land steward who died in the war."
    "Father was rewarded by the emperor with the income rights the Fukutaka family formerly held, leaving his family only the minor privilege of a notary’s income."
    "Clearly, he’s upset with Father having left Kamakura’s side in favor of the emperor’s."
    "He’s not unknown to you, but he’s never before confronted you openly."
    "Looks like he wants to make a disturbance, but you really don’t feel like doing this today."

    mc "Then let me respond. I am Hirasada Marokore, son of Hirasada Koretame, Jito of Niyama."
    mc "Ever-loyal to the emperor and country above all else, and I will defend my family, this village, and our honor."

    mc "It's late."

    rival "Too scared to talk to me after the sun goes down?"

    mc "What I meant was, why are you visiting us at this hour? Would your mother not need you at home?"

    rival "Don’t you dare speak about my mother. Don’t you dare speak anything about families."
    rival "You and your kind are nothing but dishonorable leeches on this village."
    rival "Just using Niyama to line your pockets."

    bro "Funny you mention that! I don’t remember you going out in the mornings to help the village."

    "You shush your brother quickly."

    rival "Will your little brother fight this battle for you?"

    mc "He has a point, you know. We make it known to Niyama every single day how grateful we are to be here."
    mc "We help catch fish, organize war supplies… We improve our fighting abilities to protect its people!"

    rival "Fighting abilities, eh?"

    "He has an eager glint in his eye. His enthusiasm repulses you."

    rival "Wanna test them out, traitor-spawn?"

    hide rival
    hide brother

    menu:
        "Your points: martial [martial], charisma [charisma], patience [patience]."

        "There has never been a protracted war from which a country has benefited.":
            jump rivalfight
        "The supreme art of war is to subdue the enemy without fighting.":
            jump rivalrizz
        "He will win who knows when to fight and when not to fight.":
            jump rivalpatience

label rivalfight():
    scene bg rival with fade

    if martial > 7:
        "You are a warrior. You give a nod, and rush at him while unsheathing your sword."
        show rival with hpunch
        "Shigefumi seems unprepared, unsheathing his just in time to barely cross blades."
        "You swing ferociously, barely giving him time to take the initiative."
        "Slowly, you push him back. All the while, he panics."
        "He slashes from his right. You meet the sword, and then push it to the side."
        "One bold stab misses when you sidestep to the side, and your swing takes off a hairlock."
        "Finally, after one reckless swung slash from him, you use your sword’s pummel to bluntly hit his face."
        "He goes down."
        "You don’t want to kill him."
        "You could, but you hesitate."
        "Take a life out here, in front of your family?"

        mc "Leave."
        mc "You have been beaten. This is our land."
        mc "Our home."

        $martial += 3

    elif martial > 4:
        "You are a warrior. You give a nod, and take out your sword as he reveals his."
        "You take position, and both of you creep together."
        show rival with hpunch
        "He takes the first swing."

        "You block. Then you return one with another."

        "And then he returns another. And so on."

        "One almost cuts your hand."
        "One almost takes his ear."

        "You’re both cautious. You don’t want to overstep, and neither does he."

        show sister at right with moveinright
        sis "That’s enough! Both of you, stop it!"

        "You take a deep breath. It might be wise to accept that."
        "You’re tired already, and if you die, would he kill your siblings too?"

        mc "Fine. But Shigefumi, this isn’t over yet."

        rival "I don't doubt it."

        $martial += 2

    else:
        "You are a warrior’s son. But you are not a warrior just yet."
        "You realize that just as Shigefumi swings a blade at you."
        show rival with hpunch
        "You unsheathe it just in time, but that spells the fate of this encounter."
        "You are trained. But not skilled. That’s apparent every sword clash, when your teeth crunch, and arms vibrate."
        "You're outmatched."

        "You take an aggressive slash against him, but it veers off course, and Shigefumi slaps the blade out of your hand."
        "You see in his eyes that even he didn’t expect that."
        "Your eyes pinpoint his sword’s tip."
        "Is this it?"
        "Is this how it all ends?"
        "Over a land dispute?"
        "It’s almost funny, in a morbid sense."

        sis "That’s enough!"
        sis "Leave, or I’ll leave you in so many pieces that even the maggots won’t have enough to munch on."

        "You look up in surprise, and see that she’s taken hold of your lost sword, and is pointing it at Shigefumi's back."
        "Wordlessly, he sheaths his sword. With one last glare, he slowly backs up."

        $martial -= 1

    return

label rivalrizz():
    scene bg rival with fade:
        zoom 1.5

    if charisma > 7:
        show rival

        mc "Did you come here to fight? To kill me?"
        mc "I hope you’re prepared to be punished by the law. The courts do not take kindly to murder."

        rival "I came here to see how this village would fare with your family in charge."
        rival "Frankly, I’m not impressed."

        mc "You have seen. And you will see more. Wait, and you will be impressed."

        rival "What exactly are you planning?"

        mc "Right now? I’m planning on returning home with my family. It’s getting dark out here."
        mc "Soon, my father and the rest of the village will wonder where we are."
        mc "What do you think they’ll suspect when we don’t show up?"
        mc "Are you planning on cleaning our blood out here, bury our corpses?"

        rival "Must you be so grim?"
        rival "I’m not planning on killing you, no matter how much better off the village would be without you."

        mc "Then let the village come to that realization."
        mc "Kill us here, and you will be a murderer, exiled, all hopes of regaining your honor lost forever."

        rival "Our house does not need to resort to this type of dishonorable work."

        $charisma += 3

    elif charisma > 4:
        show rival

        mc "Why have you come here?"

        rival "I came here to gauge my father’s usurpers. Frankly, I’m not impressed."

        mc "Funny you should say that. I’m sure your father would say the same thing if he saw you."

        rival "You!"
        rival "You..."
        rival "Unlike your father, my father didn’t have to resort to backstabbing to steal away our land!"

        mc "Stealing! Is that what you call it?"
        mc "Your family took up arms against the emperor! Our father fought for the rightful side, and was rewarded for his loyalty!"

        rival "Rewarded for having an idiotic, moronic son!"

        mc "If he had you, father would have committed harakiri!"
        mc "Better than than seeing you grow up to be more salty and bitter than seawater!"

        rival "You son of a-"

        sis "That’s enough, you knuckleheads!"
        sis "Just get out of here! We can discuss whatever this is later."

        $charisma += 2

    else: 
        show rival

        mc "What do you want?"

        rival "I am here to reclaim my family’s honor! Our rightful land!"

        mc "Can’t you just live here happily too? Even with us around?"

        rival "And have to suffer the sight of usurpers enriched by my father’s hard work?"
        rival "Never! Never! Never! How humiliating it is to suffer this disgrace gotten by treachery."
        rival "Weren’t you happy back wherever you came from?"

        mc "Well... maybe you have a point."

        "You were beginning to feel sad about his whole situation."
        "What if you did hand the land back over to him? We could return to our old home..."

        bro "I’ve seen enough. Marokore, you gotta be better at arguing."
        bro "And you, how bored are you to pick on a moron like him!"

        mc "Hey!"

        bro "Just get out of here, Shigefumi! Or we’ll beat you up!"

        $charisma -= 1

    return

label rivalpatience():
    scene bg rival with fade:
        zoom 1.5

    show rival
    "I could fight him. Or argue with him."

    mc "Yasumaru, Masako, let’s go home."

    "Or just ignore him."
    "He wasn’t important anymore. Better to leave him to fade into obscurity."
    "We keep walking down the road."

    rival "Are you running away? Coward! Where’s your honor! Come back! I demand you to fight!"

    "Just ignore this fool. You've already heard enough of his nonsense."

    rival "Guess I should have expected this from the son of that man."
    rival "Came here to see how you were. And to be perfectly honest, I’m not impressed."
    rival "A gutless coward and cheat."

    if patience > 7:
        "He was making you mad. But so what? Better to leave him spitting at the ground, bawling insults, than to deign to respond."

        rival "…Fine! Leave, coward! But beware!"

        $patience += 3

    else:
        show rival
        "…What?"
        "Were you supposed to let that one go?"
        "What kind of son would let his father be insulted like that?"
        
        mc "Funny you should say that. I’m sure your father would say the same thing if he saw you."

        rival "You!"
        rival "You..."
        rival "Unlike your father, my father didn’t have to resort to backstabbing to steal away our land!"

        mc "Stealing! Is that what you call it?"
        mc "Your family took up arms against the emperor! Our father fought for the rightful side, and was rewarded for his loyalty!"

        rival "Rewarded for having an idiotic, moronic son!"

        mc "If he had you, father would have committed harakiri!"
        mc "Better than than seeing you grow up to be more salty and bitter than seawater!"

        rival "You son of a-"

        sis "That’s enough, you knuckleheads!"
        sis "Just get out of here! We can discuss whatever this is later."

        $patience -= 1

    return



    


