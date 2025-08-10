let C = 0
let B = 0
iBIT.setADC_Address(adcAddress.iBIT_V2)
OLED.init(128, 64)
let R = 830
let L = 700
let maxrefR = -1
let minrefR = 10000000
let maxrefL = -1
let minrefL = 10000000
basic.forever(function () {
    if (B == 0) {
        basic.pause(400)
        B += 1
    }
    basic.pause(10400)
    if (C == 0) {
        C += 1
        basic.pause(1000)
        C += 1
    }
})
basic.forever(function () {
    basic.showNumber(C)
    maxrefR = Math.max(iBIT.ReadADC(ibitReadADC.ADC0), maxrefR)
    minrefR = Math.min(iBIT.ReadADC(ibitReadADC.ADC0), minrefR)
    maxrefL = Math.max(iBIT.ReadADC(ibitReadADC.ADC1), maxrefL)
    minrefL = Math.min(iBIT.ReadADC(ibitReadADC.ADC1), minrefL)
})
basic.forever(function () {
    if (B != 0 && minrefR <= R && minrefL <= L) {
        R = (maxrefR * 1.5 + minrefR) / 2
    }
    L = (maxrefL * 1.5 + minrefL) / 2
    maxrefR = -1
    minrefR = 10000000
    maxrefL = -1
    minrefL = 10000000
    basic.pause(2000)
})
basic.forever(function () {
    if (iBIT.ReadADC(ibitReadADC.ADC0) >= R && iBIT.ReadADC(ibitReadADC.ADC1) >= L && (B == 0 || C == 1)) {
        iBIT.Motor(ibitMotor.Forward, 100)
    } else if (iBIT.ReadADC(ibitReadADC.ADC0) >= R && iBIT.ReadADC(ibitReadADC.ADC1) >= L && (C == 0 || C == 2)) {
        iBIT.Motor(ibitMotor.Forward, 53)
    } else if (iBIT.ReadADC(ibitReadADC.ADC0) < R && iBIT.ReadADC(ibitReadADC.ADC1) < L) {
        iBIT.Spin(ibitSpin.Right, 100)
    } else if (iBIT.ReadADC(ibitReadADC.ADC0) < R && iBIT.ReadADC(ibitReadADC.ADC1) >= L && (C == 0 || C == 1)) {
        iBIT.Turn(ibitTurn.Left, 70)
    } else if (iBIT.ReadADC(ibitReadADC.ADC0) >= R && iBIT.ReadADC(ibitReadADC.ADC1) < L && (C == 0 || C == 1)) {
        iBIT.Turn(ibitTurn.Right, 70)
    } else if (iBIT.ReadADC(ibitReadADC.ADC0) < R && iBIT.ReadADC(ibitReadADC.ADC1) >= L && C == 2) {
        iBIT.Spin(ibitSpin.Left, 100)
    } else if (iBIT.ReadADC(ibitReadADC.ADC0) >= R && iBIT.ReadADC(ibitReadADC.ADC1) < L && C == 2) {
        iBIT.Spin(ibitSpin.Right, 100)
    }
})
