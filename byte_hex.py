import re

def byte_to_hex(byte: str): 
    hex = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",  
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
    }
        
    return hex[byte]

def hex_to_byte(hex: str): 
    byte = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",  
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }
        
    return byte[hex]


def byte_is_binary(byte: str) -> bool: 
    return re.search("^[01]+$", byte) is not None

def character_is_hex(character: str) -> bool: 
    return re.search("^[A-F0-9]$", character) is not None

def convert_hex_string(): 
    # takes a string and turns it to binary

if __name__ == '__main__':
   print(byte_to_hex("0001"))
   print(hex_to_byte("A"))