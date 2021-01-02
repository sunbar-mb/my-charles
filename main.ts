let FlashInterval = 500
let CharlesX = 2
let CharlesY = 2
let Visible = true
let Led_value = false
//  WhereToGo: 1 - North, 2 - West, 3 - South, 4 - East
let WhereToGo = 1
basic.forever(function BlikajiciBod() {
    if (Visible) {
        led.plot(CharlesX, CharlesY)
        basic.pause(FlashInterval)
        led.unplot(CharlesX, CharlesY)
        basic.pause(FlashInterval)
    } else if (Led_value) {
        led.plot(CharlesX, CharlesY)
    } else {
        led.unplot(CharlesX, CharlesY)
    }
    
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    WhereToGo = WhereToGo + 1
    if (WhereToGo > 4) {
        WhereToGo = 1
    }
    
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    move_point(true)
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    Visible = !Visible
    
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    move_point(false)
    
})
function IncreaseX(numberX: number): number {
    let y = numberX + 1
    if (y > 4) {
        y = 4
    }
    
    return y
    
}

function DecreaseX(numberX: number): number {
    let y = numberX - 1
    if (y < 0) {
        y = 0
    }
    
    return y
    
}

function move_point(LeaveTrack: boolean) {
    
    
    
    
    
    if (Visible) {
        if (LeaveTrack) {
            led.plot(CharlesX, CharlesY)
        } else {
            led.unplot(CharlesX, CharlesY)
        }
        
        if (WhereToGo == 1) {
            CharlesY = DecreaseX(CharlesY)
        }
        
        if (WhereToGo == 2) {
            CharlesX = DecreaseX(CharlesX)
        }
        
        if (WhereToGo == 3) {
            CharlesY = IncreaseX(CharlesY)
        }
        
        if (WhereToGo == 4) {
            CharlesX = IncreaseX(CharlesX)
        }
        
        // Keep track whether the LED was ON or OFF - used for toggle the Visibility
        Led_value = led.point(CharlesX, CharlesY)
    }
    
    
}

