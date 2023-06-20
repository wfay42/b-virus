# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sumire")
define e = Character("Eri", who_color="#017a01ff")
define r = Character("Rina", who_color="#b56d26")
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
            s "No, mom, wait!"

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
        "Sumire":
            jump floor_sumire
        "Eri":
            jump floor_eri

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

    jump floor_menu

label floor_eri:
    show eri floor 06
    with dissolve_2

    show rina floor 06
    with dissolve_2
    "It was too late for Sumire and her family. They were now bimbos just like everyone else. They really shouldn't have opened the door."

    return

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
