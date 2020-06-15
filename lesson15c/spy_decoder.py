# Variable spy_coder is predefined


def spy_decoder(string, shift):
    return spy_coder(string, -shift)


"BOX" == spy_decoder("SPY CODER", 6)
