# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sumire")
define e = Character("Eri", who_color="#017a01ff")
define r = Character("Rina", who_color="#b56d26")
define es = Character("Sumire & Eri", who_color="#090501")
default watched_tv = False
default floor_sumire_unchanged = True
default floor_rina_unchanged = True
default floor_eri_unchanged = True

# A smooth dissolve over 2 seconds
define dissolve_2 = Dissolve(2)

# Custom transformations for positioning
transform tleft:
    xpos -0.3
transform tright:
    xpos 0.3


# The game starts here.

label start:
    scene bg bedroom door
    "It was a normal weekend like any other for Sumire. She just got home from doing her daily chores when she finds a box on her doorstep."

    show sumire standing holding box
    s "That's strange, no return address. I don't remember ordering anything."

    jump start_bedroom


label start_bedroom:
    scene bg bedroom

    show sumire standing thinking

    s "Oh well, time to relax now that I've got all of that out of the way."
    menu:

        "See what's inside the box.":
            jump open_box

        "Lay in bed":
            jump lay_in_bed

        "Turn on the TV.":
            jump turn_on_tv

label bedroom_after_tv:
    scene bg bedroom

    show sumire standing surprised

    s "What the hell was that! Is this for real!?"
    menu:

        "See what's inside the box.":
            jump open_box

        "Lay in bed":
            jump lay_in_bed

        "Call sister.":
            jump call_sister

label open_box:
    scene bg bedroom floor
    show sumire heels 01
    "Curiosity gets the best of her, and Sumire opens the box to find a pair of bright pink pumps with some rather steep heels."
    s "I definitely didn't order these things."
    "Despite not knowing where the shoes came from, Sumire felt oddly compelled to put them on."

    show sumire heels 02a
    "She gently slides her right foot into the first heel. It fits perfectly."

    show sumire heels 02b
    "Without wobbling at all, she manages to get her left foot in with equal ease."

    scene bg bedroom floor up
    show sumire heels 03
    s "Wow, these are surprisingly comfortable, despite those enormous heels. Oh well, better take them off."

    scene bg bedroom floor
    show sumire heels 02b
    "But before she can take them off, something starts to change."

    show sumire heels 04
    with dissolve_2
    s "Wait, was I, like, always wearing these sexy stockings?  Teehee, at least they go with my hot new shoes!"

    scene bg bedroom floor up
    show sumire heels 05
    s "Like, I've gotta go show these off to my friends!"

    jump end

label lay_in_bed:
    scene bg bedroom bed
    show sumire bed 01

    "Sumire lays down in the bed, without a care in the world."
    "But while she's sleeping, someone enters the room."

    show dildo 01
    with dissolve
    "Sumire doesn't even register that anyone has come in."

    show sumire bed 02
    "The stranger explodes all over Sumire's body, staying completely silent. Still unconcious, Sumire's body responds to the smell of the semen that's now covering her whole body. Her nose wrinkles and her mouth opens."

    show sumire bed 03
    with dissolve_2
    "Sumire suddenly undergoes multiple changes. Her hair extends into long blonde locks. Her skin becomes more tan. Makeup appears on her face. Her eyelashes grow longer."

    show sumire bed 04
    with dissolve_2
    "Next sexy lingerie, see-through finger gloves, manicured fingernails, and gold hoop earrings adorn her body."

    show sumire bed 05
    "Sumire awakens, completely taken by the bimbo virus. Large pink hearts stand in the center of her eyes, the telltale sign of the disease. The only thing she can do now is properly greet her guest."

    s "Like, hey there! Heehee, would you like to go another round?"

    scene bg bedroom bed 02
    show sumire bed bj 01
    "Sumire grabs ahold of the stranger member and doesn't hesitate to pull it straight into her mouth while looking up at him excitedly."

    scene bg bedroom bed 03
    show sumire bed sex 01
    "It doesn't take long before Sumire is on her back receiving the full service.  She can't control the pleasure, and her eyes roll back into her head while her tongue sticks out as she has her first orgasm as a bimbo."

    jump end

label turn_on_tv:
    scene
    show tv
    "Sumire decides to kick back, relax, and watch some TV."

    define z = Character("Zoe", who_color="#ba4242")
    define a = Character("Anri", who_color="#ddacac")
    show news 01
    z "We interrupt your normal broadcast to bring you this special report."
    a "There have been reports of women suddenly changing hair color and acting ditzy."

    show news 02
    with dissolve_2
    z "People should use the utmost caution."

    show news 03
    with dissolve_2
    a "We recommend people stay indoors and don't let in any strangers."

    show news 04
    with dissolve_2
    z "But like, meeting new people is totally fun, so maybe you should do that! A pretty lady I just met gave me a big kiss on my way to work today!"

    show news 05
    with dissolve_2
    a "Teehee, no way! Same here!"

    show news 06
    with dissolve_2
    z "Yup, so like, today is a great day to go out and make some new friends!"

    show news 07
    with dissolve_2
    a "Totes! Or just make out, I mean hang out with an old friend!"

    show news 08
    "We will return after a word from our sponsors."

    $ watched_tv = True
    jump bedroom_after_tv

label call_sister:
    scene bg bedroom
    show sumire standing phone mouthclosed
    "Sumire tries calling her sister"

    show sumire standing phone mouthopen
    s "Come on Eri... Pick up!"

    scene bg momhouse
    show eri standing phone mouthopen
    e "Hey sis! What's up?"
    s "Eri, are you OK? Is mom OK?"
    e "Huh? Yeah, of course we are. What's up with you?"
    s "Haven't you seen the news? There's something weird going on."
    e "Ha, the news? You know how mom doesn't have a TV in the house. If you're so worried, you should come over."

    scene bg bedroom
    show sumire standing phone mouthopen
    s "That's a good idea, I'm heading over right now. Stay inside, don't go anywhere!"

    menu:

        "See what's inside the box.":
            s "Before I go over, I should check what's in this box."
            jump open_box

        "Lay in bed":
            s "I should lay down for just a few seconds. I'm sure they'll be fine for a few minutes."
            jump lay_in_bed

        "Head over to mom's houes":
            jump arrive_at_moms

label arrive_at_moms:
    scene bg momhouse
    "Sumire drives the short distance to her mother's house where her sister, Eri is visiting. She enters with her heart pounding."

    show eri standing smiling at tright
    show sumire standing surprised at tleft
    s "Eri! Where's mom!"
    e "Whoa, chill out, she's right here"

    show rina standing smiling
    r "Hi honey, how are you doing?"

    show sumire standing thinking at tleft
    s "Phew, you're both OK."

    e "Now can you explain what's going on? Why do you seem so spooked?"

    s "Right! I don't know why, but there's something weird going on where women are turning into blonde bimbos."
    s "On the news they recommended staying indoors and avoiding others since it seems to be transferred between people."

    show eri standing worried
    e "Are you serious right now?  This seems ridiculous."

    show rina standing worried
    r "Your sister's right, Sumire. Maybe you just need to eat something."

    show sumire standing surprised
    s "No, I'm serious!"

    "Suddenly there was a knock at the door."

    show sumire standing thinking
    show eri standing smiling
    show rina standing smiling
    r "You two sit tight while I see who that is."

    menu:
        "Let her see who is at the door.":
            jump mom_open_door

        "Stop her.":
            jump stop_mom_from_opening_door


label stop_mom_from_opening_door:
    show sumire standing surprised
    s "No, mom, wait! Didn't you listen to me, you can't just open the door for anyone!"

    show rina standing worried
    r "Fine honey, you seem pretty shaken up about this, I won't do anything if you say I shouldn't."

    show sumire standing thinking
    show rina standing smiling
    r "With that settled, can we have dinner? I'm sure you girls are starving."
    e "Let's do it! Family dinner is why we came over tonight in the first place."

    show sumire standing happy
    s "OK, I guess we can relax for a bit."

    # parallel:
    hide sumire with dissolve
    hide rina with dissolve
    hide eri with dissolve

    "The three women have a delicious home-cooked meal. They stay up and chat for a while until Rina says she wants to turn in for the night."

    show sumire standing thinking at tleft
    show rina standing smiling
    show eri standing smiling at tright

    r "Well, this has been another lovely family dinner, girls, but I'm going to get some sleep. Don't stay up too late yourselves."
    hide rina with dissolve

    e "So are you serious about this whole bimbo thing Sumire? It seems totally crazy."
    s "For the hundredth time, yes!"

    jump mom_bedroom

label mom_bedroom:
    scene bg none
    "Rina enters her bedroom exhausted from the day, and still unsure what Sumire had been telling her."
    show rina shoes 01
    r "What a day. I hope everything is alright with Sumire. She's been so stressed out lately, the poor dear."
    r "Oh well, tomorrow is another day. Just one more thing to do before bed."

    window hide
    show rina shoes 02
    pause
    window show
    r "I just need to try these on to see if they're my size. They might have been delivered here by accident, but someone else's loss is my gain!"

    scene bg momhouse
    show sumire standing thinking at tleft
    show eri standing smiling at tright
    s "On top of that, there was this box that got delivered to my apartment. I didn't even bother looking into it."
    e "Oh yeah? Mom said she got something too, but said she didn't know who it was from."

    show sumire standing surprised
    s "Wait really? Where is the box?"
    e "I think mom took it into her room, why?"

    show sumire standing thinking
    s "I've got a bad feeling about this..."
    e "Well, do what you want. I'm heading to bed. See you in the morning!"
    hide eri with dissolve
    s "Hmm, I can't shake the feeling I should check on mom..."

    scene bg none
    show rina shoes 03
    r "Oh my! These heels are sky-high!"

    show rina shoes 04
    r "But they sure are gorgeous! They make my legs look amazing!"

    "There is a knock at the door."

    s "Hey mom, can I come in?"

    r "Sure thing dear."

    show rina shoes 05
    s "Mom, be careful! You shouldn't accept gifts from strangers! Who knows if those are part of the thing on TV!"
    r "Sumire, these things are completely safe. They can't possibly harm me, they're just shoes."

    window hide
    show rina shoes 06a with dissolve_2
    pause
    window show
    r "Really sweet, I hope you're not jealous of these beautiful shoes. I can certainly get you your own pair."

    show rina shoes 06b
    s "Mom, NO! Your outfit changed, you look like a... like a..."

    show rina shoes 07
    r "Like a milf? Of course I do honey. You know your mumsy has always been a hottie."
    s "What!? You've never talked like this before mom. I need to go and get help..."

    show rina shoes 08
    s "Mom no! Let go of me!"
    r "Sumire deary, where are your manners? I know I taught you better than this! Like I said, I'm happy to get you some new clothes too."

    show rina shoes 09
    s "Ughhh, no! I'm not looking for new clothes! It feels like I'm burning hot, let me go before it's too late! Before..."

    window hide
    show rina shoes 10 with dissolve_2
    pause
    window show
    s "Before, like, I change and..."

    show rina shoes 11
    s "Before I say, like, thanks for the outfit mom! You always have such great taste."
    r "You're welcome sweety. Now how about we pay your sister a visit?"

    jump eri_bedroom

label eri_bedroom:
    scene bg none
    show eri shoes 01
    "Eri lays on her bed after falling asleep surprisingly quickly."

    show eri shoes 02
    "Her feel dangle off the edge of the bed."

    show eri shoes 03
    "The door opens with the slightest creak as Rina and Sumire enter."

    show eri shoes 04
    "The two women slowly make their way to the foot of the bed without making a sound. Saying nothing, they pass a knowing look to one another."

    show eri shoes 05
    "Pulling out another pair of heels found in Rina's surprise delivery, Sumire slips the beautiful shoes onto her sister's feet."
    s "(Whispering) These two are so cute! I kind of wish these were mine."

    window hide
    show eri shoes 06 with dissolve_2
    pause
    window show
    "Like her sister and mother, Eri's clothes change with the addition of the heels."

    show eri shoes 01
    "Eri remains fast asleep not noticing the change happening to her."

    window hide
    show eri shoes 07 with dissolve_2
    pause
    window show
    "The changes are fast, Eri wakes right up."

    show eri shoes 08
    e "Like, what are you two doing? Are we having a sleepover too?"

    show eri shoes 09
    e "I'd say we should totes do makeovers! Except we're already all dressed up and ready to party, so I guess we can skip that step."
    s "Finding a party, that's totally the right idea! What do you think momma, you want to come too?"
    r "Ha! You girls are so full of energy, even for this late hour."

    show eri shoes 10
    r "Alright, let's all go. Remember that your mother spent a decade dancing in shoes like these, so do try to keep up."
    es "Yes, mother!"

    jump last_end

label mom_open_door:
    hide rina
    with dissolve
    r "Oh hello there, how can I help you gentlemen?"

    show sumire standing surprised
    show eri standing worried
    r "Oh, what are you doing? I didn't invite you in!"
    s "Mom?"
    e "Mom!"

    scene bg momhouse floor
    "Before they knew what was happening, the three women were brought to their knees by the three men at the door."

    show sumire floor 01
    show rina floor 01
    show eri floor 01
    s "Who the hell are you!? Get out of my mom's house."
    r "I won't stand for this!"
    e "Y... yeah, what they said."

    "The three men open their trousers to reveal themselves fully engorged. As if instinctually they begin rubbing themselves. The only thing left to wonder is who will finish first."

    jump floor_menu

label floor_menu:
    menu:
        "Sumire" if floor_sumire_unchanged:
            jump floor_sumire
        "Rina" if floor_rina_unchanged:
            jump floor_rina
        "Eri" if floor_eri_unchanged:
            jump floor_eri

    # NOTE: if the above menu has no options, logic will flow down to this line
    "It was too late for Sumire and her family. They were now bimbos just like everyone else."

    scene bg momhouse floor 02
    show floor 01
    "They really shouldn't have opened the door to those strangers."
    jump end

label floor_sumire:
    show sumire floor 02
    "One man blows his load over Sumire's face, forcing her to close an eye."
    s "Ughhh, disgusting!"

    show sumire floor 03
    with dissolve_2
    "Despite her disgust, Sumire's hair changes to a golden blonde."

    show sumire floor 04
    with dissolve
    s "Teehee, why does this, like, smell sweet?"

    show sumire floor 05
    with dissolve_2
    s "Like, I'm so glad you could finish yourself so fast!"

    show sumire floor 06
    with dissolve_2
    s "We should totes have some more fun!"

    $ floor_sumire_unchanged = False
    jump floor_menu

label floor_eri:
    show eri floor 02
    "Before she can look away, Eri gets a full facial from one of the mysterious intruders."
    e "Eww, yuck! Did you seriously do what I think you did?"

    show eri floor 03
    with dissolve_2
    e "It smells weird... It's making me kind of light headed."

    show eri floor 04
    with dissolve_2
    e "Heehee, but the feeling is kind of fun."

    show eri floor 05
    with dissolve_2
    e "Like, thanks for blowing that load all over me!"

    show eri floor 06
    with dissolve_2
    e "But I am jealous I didn't get to help you! The next one is on me!"

    $ floor_eri_unchanged = False
    jump floor_menu

label floor_rina:
    show rina floor 02
    "One intruder finishes himself, leaving his seed all over Rina's face. Rina sits unflinching, only averting her gaze slightly."
    r "Disgusting... I will not stand for this in my own home!"

    show rina floor 03
    with dissolve_2
    r "You should know I'm an attorney, and this is going to be very, very easy to prosecute."

    show rina floor 04
    with dissolve_2
    r "And, uh, my doorbell camera footage will easily... like, is it getting hot in here?"

    show rina floor 05
    with dissolve_2
    r "Like, yeah, I'm burning up!  What? I should show off more skin?"

    show rina floor 06
    with dissolve_2
    r "Teehee, like, that's such a good idea!"

    $ floor_rina_unchanged = False
    jump floor_menu

label unused_bimbo_standing:
    show rina bimbo standing smiling
    with dissolve_2
    show sumire bimbo02 standing smiling at tleft
    with dissolve_2
    show eri bimbo standing smiling at tright
    with dissolve_2
    ""

label end:
    # This ends the game.

    return

label last_end:
    scene black with dissolve
    "You got the Good Ending."

    # This ends the game.
    return
