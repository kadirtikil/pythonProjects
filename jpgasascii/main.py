from PIL import Image
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)


def read_image(path):
    if path == "":
        return None
    else:
        return np.array(Image.open(path))

    

def main():
    # dense parts with dense ascii chars. density is determined by the color of the spot in the picture
    # so sort the asciis by how dense they appear hori and vert, then map those to color grades. 
    # then iterate through the picture in spots, then apply the fitting ascii character,
    # sounds like a plan? good. future kadir got this i know it...
    bwface = "./bwface.jpg"

    read_in_pic = read_image(bwface)

    #print((read_in_pic))
    # now we got he pictures as an array. will later handle this myself without using numpy maybe to try to see how it reads in.
    # now i got to map the ascii- the higher the number the denser it should be. so thisll take some work
    map_ascii_to_num = {
        0:"I",1: " ", 2: ".", 3: ",", 4: "'", 5: "\"", 6: "`", 7: "-", 8: "_", 9: "^", 10: "~",
        11: ":", 12: ";", 13: "(", 14: ")", 15: "[", 16: "]", 17: "{", 18: "}", 19: "<", 20: ">",
        21: "!", 22: "?", 23: "/", 24: "\\", 25: "|", 26: "@", 27: "#", 28: "$", 29: "%", 30: "^",
        31: "&", 32: "*", 33: "+", 34: "=", 35: "0", 36: "1", 37: "2", 38: "3", 39: "4", 40: "5",
        41: "6", 42: "7", 43: "8", 44: "9", 45: "a", 46: "b", 47: "c", 48: "d", 49: "e", 50: "f",
        51: "g", 52: "h", 53: "i", 54: "j", 55: "k", 56: "l", 57: "m", 58: "n", 59: "o", 60: "p",
        61: "q", 62: "r", 63: "s", 64: "t", 65: "u", 66: "v", 67: "w", 68: "x", 69: "y", 70: "z",
        71: "A", 72: "B", 73: "C", 74: "D", 75: "E", 76: "F", 77: "G", 78: "H", 79: "I", 80: "J",
        81: "K", 82: "L", 83: "M", 84: "N", 85: "O", 86: "P", 87: "Q", 88: "R", 89: "S", 90: "T",
        91: "U", 92: "V", 93: "W", 94: "X", 95: "Y", 96: "Z", 97: "ä", 98: "ö", 99: "ü", 100: "ß",
        101: "Ä", 102: "Ö", 103: "Ü", 104: "é", 105: "è", 106: "ê", 107: "à", 108: "ù", 109: "ç", 110: "É",
        111: "È", 112: "À", 113: "Ç", 114: "ñ", 115: "Ñ", 116: "€", 117: "£", 118: "¥", 119: "©", 120: "®",
        121: "™", 122: "✓", 123: "✗", 124: "•", 125: "◦", 126: "○", 127: "▲", 128: "■", 129: "♠", 130: "♣",
        131: "♥", 132: "♦", 133: "☺", 134: "☻", 135: "♪", 136: "♫", 137: "±", 138: "×", 139: "÷", 140: "√",
        141: "∞", 142: "≈", 143: "≠", 144: "≤", 145: "≥", 146: "∑", 147: "∏", 148: "π", 149: "Ω", 150: "α",
        151: "β", 152: "γ", 153: "δ", 154: "ε", 155: "ζ", 156: "η", 157: "θ", 158: "ι", 159: "κ", 160: "λ"
    }
    #print(map_ascii_to_num[160])
    # now the chars are mapped to numbers. this will be changed later on fit the theme of: the higher the number the denser the char.
    
    result = ""
    for arr in read_in_pic:
        result += "\n"
        for num in arr:
            if num <= 160:
                result += map_ascii_to_num[num] + " "
            else:
                result += "I "

    with open("output.txt", "w") as file:
        file.write(result)



main()
