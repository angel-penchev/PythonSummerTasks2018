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

            ui.textbutton("Restart", ui.jumps("Restart"), xalign=.02, yalign=.98)
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

label Restart:

    $ k.set_sensitive(False)

    "Restart?"
    
    menu:
        "Yes":
            jump newgame

        "No":

            jump continue

label newgame:

    menu:

        "Yes":
            pass

        "No":
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
    with Pause(3.5)
    hide text
    with dissolve
    with Pause(1.0)

    with dissolve
    $ player_name = renpy.input("What do you want your screen name to be?")
    $ player_name = player_name.strip()
    with dissolve
    with Pause(0.2)

    show text "Welcome back, %s!" % player_name
    with dissolve
    with Pause(2.5)
    hide text
    with dissolve
    with Pause(0.5)

    return
