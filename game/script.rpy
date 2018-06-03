# You can place the script of your game in this file.

init:
    $ e = Character('Eileen', color="#c8ffc8")

    image eileen happy = "eileen_happy.png"
    image bg table = "Assets/Backgrounds/TableBackground.jpg"
    image dim = "#0008"

    # Some styles for show text.
    $ style.centered_text.drop_shadow = (2, 2)
    $ style.centered_text.drop_shadow_color = "#000b"

label start:

    scene bg table

    python:
        k = Belote(1)
        k.set_sensitive(False)
        k.show()

label continue:

    hide dim
    hide eileen
    with dissolve

label quick_continue:

    while True:

        python:

            ui.textbutton("Give Up", ui.jumps("giveup"), xalign=.02, yalign=.98)
            k.set_sensitive(True)
            event = k.interact()

            if event:
                renpy.checkpoint()

        if event == "win":
            jump win

label win:

    show dim
    show eileen happy
    with dissolve

    "Congratulations!"

    jump newgame

label giveup:

    $ k.set_sensitive(False)

    show dim
    show eileen happy
    with dissolve

    menu:
        e "Are you sure you want to give up?"

        "Yes":

            "Oh well, better luck next time."

            jump newgame

        "No":

            jump continue

label newgame:

    menu:
        e "Would you like to try again?"

        "Yes":
            pass

        "No":
            e "Well, I hope to see you again soon."
            return

    e "Okay, here we go!"

    scene bg table

    python:
        k = Belote(1)
        k.sensitive = False
        k.show()

    jump continue


# This has nothing to do with card games.
label splashscreen:

    scene bg table
    $ renpy.pause(1.0)

    show text "Belote Online Client"
    with dissolve
    with Pause(5.0)
    hide text
    with dissolve
    with Pause(1.0)

    show text "Gosho now logs in!"
    with dissolve
    with Pause(4.0)
    hide text
    with dissolve
    with Pause(1.0)

    show text "Welcome back, Gosho!"
    with dissolve
    with Pause(3.0)
    hide text
    with dissolve
    with Pause(1.0)

    return
