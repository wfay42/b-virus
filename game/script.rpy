# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sumire")

# A smooth dissolve over 2 seconds
define dissolve_2 = Dissolve(2)

# The game starts here.

label start:
    scene bg bedroom
    show sumire standing thinking

    "Sumire thought she had been hearing strange reports of what is going on outside"
    menu:

        "See what's inside the box.":
            jump open_box

        "Lay in bed":
            jump lay_in_bed

        "Turn on the TV.":
            jump turn_on_tv

label open_box:
    scene bg bedroom floor
    show sumire heels 01
    "Sumire opens the box to find a pair of bright pink heels with some rather steep heels."
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

    return

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

    define z = Character("Zoe")
    define a = Character("Anri")
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

    jump end

label end:
    # This ends the game.

    return
