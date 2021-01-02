FlashInterval = 500
CharlesX = 2
CharlesY = 2
Visible= True
Led_value = False

# WhereToGo: 1 - North, 2 - West, 3 - South, 4 - East
WhereToGo = 1

basic.forever(BlikajiciBod)
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
input.on_gesture(Gesture.Shake, on_gesture_shake)

def BlikajiciBod():
    if Visible:
        led.plot(CharlesX, CharlesY)
        basic.pause(FlashInterval)
        led.unplot(CharlesX, CharlesY)
        basic.pause(FlashInterval)
    else:
        if (Led_value):
            led.plot(CharlesX, CharlesY)
        else:
            led.unplot(CharlesX, CharlesY)
    pass


def on_button_pressed_a():
    global WhereToGo

    WhereToGo = WhereToGo + 1
    if (WhereToGo > 4):
        WhereToGo = 1
    pass
    
def on_button_pressed_b():
    move_point(True)
    pass



def IncreaseX(numberX):
    y = numberX + 1
    if (y>4):
        y = 4
    return y
    pass

def DecreaseX(numberX):
    y = numberX - 1
    if (y<0):
        y = 0
    return y
    pass


def on_button_pressed_ab():
    global Visible
    Visible = not(Visible)
    pass

def on_gesture_shake():
    move_point(False)
    pass


def move_point(LeaveTrack):
    global WhereToGo
    global CharlesX
    global CharlesY
    global Visible
    global Led_value

    if (Visible):
        if (LeaveTrack):
            led.plot(CharlesX, CharlesY)
        else:
            led.unplot(CharlesX, CharlesY)

        if (WhereToGo == 1):
            CharlesY = DecreaseX(CharlesY)

        if (WhereToGo == 2):
            CharlesX = DecreaseX(CharlesX)

        if (WhereToGo == 3):
            CharlesY = IncreaseX(CharlesY)

        if (WhereToGo == 4):
            CharlesX = IncreaseX(CharlesX)
        
        #Keep track whether the LED was ON or OFF - used for toggle the Visibility
        Led_value = led.point(CharlesX, CharlesY)
    pass