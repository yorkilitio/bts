def NRZBitstoSignal(bits):
    signal=" "
    for x in bits:
        if x== "1":
            signal = signal + "+"
        else:
            signal = signal + "-"
    return(signal)



def NRZSignaltoBits(signal):
    bits=" "
    for x in signal:
        if x== "+":
            bits = bits + "1"
        else:
            bits = bits + "0"
    return(bits)

def nrzibitstosignal(bits):
    signal=" "
    for x in bits:
        if x == "1":
            bits = bits + "1"
        elif x== "0":
            bits

def NRZIBitstoSignal(bits):
    signal = " "
    counter = "-"
    for x in bits:
        if x == "1" and counter == "-":
            signal = signal + "+"
            counter = "+"
        elif x == "1" and counter == "+":
            signal = signal + "-"
            counter = "-"
        elif x == "0" and counter == "-":
            signal = signal + "-"            
        elif x == "0" and counter == "+":
            signal = signal + "+"
    return signal        
            

def NRZISignaltoBits(signal):
    bits="1"
    counter="1"
    for x in signal[1:]:
        if x == "+" and counter == "1":
            bits = bits + "0"
            counter = "0"
        elif x == "+" and counter == "0":
            bits = bits + "1"
            counter = "1"
        elif x == "-" and counter == "0":
            bits = bits + "0"
        elif x == "-" and counter == "1":
            bits = bits + "1"
    return bits
    
name="Samuel"
print(name[1:])
    
    
