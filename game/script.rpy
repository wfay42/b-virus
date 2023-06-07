# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sumire")
define dissolve_2 = Dissolve(2)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sumire standing thinking

    # These display lines of dialogue.

    "You thought you had been hearing strange reports of what is going on outside"

    menu:

        "Lay in bed":
            jump lay_in_bed

        "Put on shoes.":
            jump put_on_shoes

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

    jump end

label put_on_shoes:
    jump end

label end:
    # This ends the game.

    return
