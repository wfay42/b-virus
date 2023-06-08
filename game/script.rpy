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

        "Lay in bed":
            jump lay_in_bed

        "Turn on the TV.":
            jump turn_on_tv

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
    "Something is on tv"

    show news 01
    "We bring you this special report"

    show news 02
    with dissolve_2
    "We bring you this special report"
    show news 03
    with dissolve_2
    "We bring you this special report"
    show news 04
    with dissolve_2
    "We bring you this special report"
    show news 05
    with dissolve_2
    "We bring you this special report"
    show news 06
    with dissolve_2
    "We bring you this special report"
    show news 07
    with dissolve_2
    "We bring you this special report"
    show news 08
    "We bring you this special report"

    jump end

label end:
    # This ends the game.

    return
