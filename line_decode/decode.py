def decode_nrzi_to_input(bits):
    input_array = []
    previous_bit = None

    for bit in bits:
        if previous_bit is None:
            if int(bit) == 0:
                input_array.append(1)
            elif int(bit) == 1:   
                input_array.append(0)
            else:
                raise ValueError("Invalid nrzi encoding. Bits should alternate between '0' and '1'.")
        else:
            if bit == previous_bit:
                input_array.append(0)
            else:
                input_array.append(1)
        
        previous_bit = bit

    return input_array

def decode_nrzl_to_input(bits):
    input_array = []
    previous_bit = None
    print(bits)
    for bit in bits:
        if bit == "1":
            input_array.append(1)
        elif bit == "0":
            input_array.append(0)
        else:
            raise ValueError("Invalid nrzl encoding. Bits should alternate between '0' and '1'.")

    return input_array

def decode_manchester_to_input(bits):
    input_array = []

    for i in range(0, len(bits), 2):
        if bits[i] == '0' and bits[i+1] == '1':
            input_array.append(1)
        elif bits[i] == '1' and bits[i+1] == '0':
            input_array.append(0)
        else:
            raise ValueError("Invalid Manchester encoding. Bits should alternate between '01' and '10'.")

    return input_array

def decode_ami_to_input(bits):
    input_array = []
    previous_polarity = None

    for bit in bits:
        if bit == '0':
            input_array.append(0)
        elif bit == '+':
            input_array.append(1)
        elif bit == '-':
            input_array.append(1)
        else:
            raise ValueError("Invalid bit value. Only '0' and '+' and '-' are allowed.")

    return input_array

def decode_pseudoternary_to_input(bits):
    input_array = []
    previous_polarity = None

    for bit in bits:
        if bit == '0':
            input_array.append(1)
        elif bit == '+':
            input_array.append(0)
        elif bit == '-':
            input_array.append(0)
        else:
            raise ValueError("Invalid bit value. Only '0' and '+' and '-' are allowed.")

    return input_array

def decode_polar_rz_to_input(bits):
    input_array = []

    for i in range(0, len(bits), 2):
        if bits[i] == '+' and bits[i+1] == '0':
            input_array.append(1)
        elif bits[i] == '-' and bits[i+1] == '0':
            input_array.append(0)
        else:
            raise ValueError("Invalid polar rz encoding. Bits should alternate between '+0' and '-0'.")

    return input_array

def decode_unipolar_nrz_to_input(bits):
    input_array = []

    for bit in bits:
        if bit == '0':
            input_array.append(0)
        elif bit == '1':
            input_array.append(1)
        else:
            raise ValueError("Invalid bit value. Only '0' and '1' are allowed.")

    return input_array

def decode_differential_manchester_to_input(bits):
    input_array = []
    previous_level = 1

    for i in range(0, len(bits), 2):
        if bits[i] == bits[i+1]:
            level = previous_level
        else:
            level = 0

        input_array.append(level)
        previous_level = level

    return input_array




# encoded_bits = "0+-000+-0"

encoded_bits = "1010100110010101"

# encoded_bits = "+0-0-0+0+0-0"
decoded_array = decode_differential_manchester_to_input(encoded_bits)
print(decoded_array)