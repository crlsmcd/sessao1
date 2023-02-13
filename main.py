def on_forever():
    basic.show_leds("""
        # # # # #
                # . . . .
                # . . . .
                # . . . .
                # # # # #
    """)
    basic.show_leds("""
        . . # . .
                . . . . .
                . # # # .
                . . . . .
                # . . . #
    """)
    basic.show_leds("""
        # # # # #
                # . . . #
                # # # # #
                # . # . .
                # . . # .
    """)
    basic.show_leds("""
        # . . . .
                # . . . .
                # . . . .
                # . . . .
                # # # # #
    """)
    basic.show_leds("""
        # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
    """)
    basic.show_leds("""
        # # # # #
                # . . . .
                # # # # #
                . . . . #
                # # # # #
    """)
    basic.clear_screen()
    basic.pause(2000)
basic.forever(on_forever)
