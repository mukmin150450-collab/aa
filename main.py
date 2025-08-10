C = 0
B = 0
iBIT.setADC_Address(adcAddress.IBIT_V2)
OLED.init(128, 64)
R = 830
L = 700
maxrefR = -1
minrefR = 10000000
maxrefL = -1
minrefL = 10000000

def on_forever():
    global B, C
    if B == 0:
        basic.pause(400)
        B += 1
    basic.pause(10400)
    if C == 0:
        C += 1
        basic.pause(1000)
        C += 1
basic.forever(on_forever)

def on_forever2():
    global maxrefR, minrefR, maxrefL, minrefL
    basic.show_number(C)
    maxrefR = max(iBIT.read_adc(ibitReadADC.ADC0), maxrefR)
    minrefR = min(iBIT.read_adc(ibitReadADC.ADC0), minrefR)
    maxrefL = max(iBIT.read_adc(ibitReadADC.ADC1), maxrefL)
    minrefL = min(iBIT.read_adc(ibitReadADC.ADC1), minrefL)
basic.forever(on_forever2)

def on_forever3():
    global R, L, maxrefR, minrefR, maxrefL, minrefL
    if B != 0 and minrefR <= R and minrefL <= L:
        R = (maxrefR * 1.5 + minrefR) / 2
        L = (maxrefL * 1.5 + minrefL) / 2
        maxrefR = -1
        minrefR = 10000000
        maxrefL = -1
        minrefL = 10000000
        basic.pause(2000)
basic.forever(on_forever3)

def on_forever4():
    if iBIT.read_adc(ibitReadADC.ADC0) >= R and iBIT.read_adc(ibitReadADC.ADC1) >= L and (B == 0 or C == 1):
        iBIT.motor(ibitMotor.FORWARD, 100)
    elif iBIT.read_adc(ibitReadADC.ADC0) >= R and iBIT.read_adc(ibitReadADC.ADC1) >= L and (C == 0 or C == 2):
        iBIT.motor(ibitMotor.FORWARD, 53)
    elif iBIT.read_adc(ibitReadADC.ADC0) < R and iBIT.read_adc(ibitReadADC.ADC1) < L:
        iBIT.spin(ibitSpin.RIGHT, 100)
    elif iBIT.read_adc(ibitReadADC.ADC0) < R and iBIT.read_adc(ibitReadADC.ADC1) >= L and (C == 0 or C == 1):
        iBIT.turn(ibitTurn.LEFT, 70)
    elif iBIT.read_adc(ibitReadADC.ADC0) >= R and iBIT.read_adc(ibitReadADC.ADC1) < L and (C == 0 or C == 1):
        iBIT.turn(ibitTurn.RIGHT, 70)
    elif iBIT.read_adc(ibitReadADC.ADC0) < R and iBIT.read_adc(ibitReadADC.ADC1) >= L and C == 2:
        iBIT.spin(ibitSpin.LEFT, 100)
    elif iBIT.read_adc(ibitReadADC.ADC0) >= R and iBIT.read_adc(ibitReadADC.ADC1) < L and C == 2:
        iBIT.spin(ibitSpin.RIGHT, 100)
basic.forever(on_forever4)
