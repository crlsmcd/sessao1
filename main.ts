basic.forever(function () {
    basic.showString("Carlos")
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
    basic.pause(200)
    basic.clearScreen()
})
