from multiprocessing import Value


def decimal_to_binary(number):

    bit_list = []
    while number > 0:
        bit_list.append(str(number%2))
        number = number//2
    bit_list.reverse()

    return bit_list

def encode(numbers):

    VLQ_result = []
    for number in numbers: #obtain a single decimal value to convert to VLQ

        #exception for when the number is 0
        if number == 0:
            VLQ_result.append(0)
            continue
        bit_list = decimal_to_binary(number)

        #obtain binary bytes with VLQ continuation flags
        i = 1 #simple counter to identify beginning of loop
        byte_list = []
        while len(bit_list) > 0:
            if i == 1: #for the final byte of VLQ notation (which is the first right-to-left)
                byte = "0" + "".join(bit_list[-7:])
                del bit_list[-7:]
                print(byte)
            elif len(bit_list) >= 7: #for in-between bytes
                byte = "1" + "".join(bit_list[-7:])
                del bit_list[-7:]
                print(byte)
            else: #for remaining bits that don't fit to a 7-bit structure
                byte = "1000000"[:8-(len(bit_list))] + "".join(bit_list)
                bit_list = []
                print(byte)
            byte_list.append(byte) #append the byte obtained per loop
            i += 1
        byte_list.reverse() #since the bytes are appended backwards, the list needs to be reversed

        VLQ_result.extend([int(byte, 2) for byte in byte_list]) #convert bytes to decimal and append to the result list
    
    return VLQ_result


def decode(bytes_):

    binary_bytes = [decimal_to_binary(number) for number in bytes_]
    print(binary_bytes)

    #replace empty lists of bits with 0 equivalent bytes
    for i, byte in enumerate(binary_bytes):
        if byte == []:
            binary_bytes[i] = "00000000"
        elif len(byte) < 8:
            binary_bytes[i] ="0000000"[:8-len(byte)] + "".join(byte)
        else:
            binary_bytes[i] = "".join(byte)
    
    print(binary_bytes)

    #number conversion according to MSB
    decoded_binary_bits = []
    binary_number_str = ""
    for byte in binary_bytes:
        if byte[0] == "1": #accumulate bits of an incomplete sequence
            binary_number_str += byte[1:]
        else: #append obtained number of a single completed sequence
            binary_number_str += byte[1:]
            decoded_binary_bits.append(int(binary_number_str,2))
            binary_number_str = ""

    #decoded numbers are only appended if sequences are completed. Empty decoded list == incomplete sequence
    if decoded_binary_bits == []:
        raise ValueError("incomplete sequence")

    return decoded_binary_bits