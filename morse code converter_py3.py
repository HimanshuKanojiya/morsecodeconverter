#International Morse Codes:

letters = {"A":".-","B":"-...","C":"-.-.","D":"-..",
           "E":".","F":"..-.","G":"--.","H":"....","I":"..",
           "J":".---","K":"-.-","L":".-..","M":"--",
           "N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.",
           "S":"...","T":"-","U":"..-","V":"...-","W":".--",
           "X":"-..-","Y":"-.--","Z":"--..",0:"-----",1:".----",
           2:"..---",3:"...--",4:"....-",5:".....",6:"-....",7:"--...",
           8:"---..",9:"----.",'!': '-.-.--', '@': '.--.-.',
           '"': '.-..-.', "'": '.----.', '&': '.-...', ')': '-.--.-',
           '(': '-.--.', '+': '.-.-.', '-': '-....-', ',': '--..--',
           '/': '-..-.', '.': '.-.-.-', ':': '---...', '=': '-...-',
           '?': '..--..','<AA>': '.-.-', '<SK>': '...-.-', '<KN>': '-.--.',
           'CL': '-.-..-..', '<DO>': '-..---', 'SOS': '...---...',
           'BK': '-...-.-', 'BT': '-...-', 'AS': '.-...', '<SN>': '...-.',
           '<AR>': '.-.-.', 'CT': '-.-.-'}


"""
Imp Variables
"""
single_space = " " #for spacing between characters
double_space = "  " #for spacing between words
#end of imp


class morsecoders:
    def __init__(self,your_input):
        self.your_input = your_input


    def encoders(mce):
        cipher = ""
        unencrypt = str(mce.your_input)
        len_of_code = int(len(unencrypt) - 1)
        for text in unencrypt:
            if text != single_space:
            
                if text.isalpha() == True:
                    text = text.upper()
                elif text.isalnum() == True:
                    text = int(text)


                if text in letters.keys():
                
                    try:
                    
                        if str(unencrypt.upper()).index(text) == len_of_code:
                            cipher = cipher + str(letters[text])
                        elif str(unencrypt.upper()).index(text) != len_of_code:
                            cipher = cipher + str(letters[text]) + str(" ")
                        elif unencrypt.index(text) == len_of_code:
                            cipher = cipher + str(letters[text])
                        elif unencrypt.index(text) != len_of_code:
                            cipher = cipher + str(letters[text]) + str(" ")

                    except:
                        cipher = cipher + str(letters[text]) + str(" ")

            
                else:
                    print("Not Found")

            elif text == single_space:
                cipher = cipher + str(double_space)
            
        return cipher.rstrip()


    def decoders(mcd):
        decrypt = ""
        encrypt = str(mcd.your_input)
        total_space = encrypt.count(single_space)

        if total_space == 0:
            for key in letters.items():
                if encrypt == key[1]:
                    decrypt = key[0]
                    return decrypt
                else:
                    continue

        elif total_space != 0:
            space_count = total_space
            cipher = ""
            decode = ""
            single_spaces = [0]
            double_spaces = [0]

            encrypt = encrypt + str(single_space + "f")
            sp_c = encrypt.count(single_space)

            i = [0]

            for encrypts in encrypt:
                if single_space not in encrypts:
                
                    if i[0] == 1:
                        for keys in letters.items():
                            if cipher == keys[1]:
                                chars = keys[0]
                                decode = decode + str(chars)

                            else:
                                continue
                            
                        
                        i[0] = 0
                        cipher = ""
                        cipher = cipher + encrypts
                    
                    elif i[0] == 3:
                        for keys in letters.items():
                            if cipher == keys[1]:
                                chars = keys[0]
                                decode = decode + str(chars) + str(single_space)


                        cipher = ""
                        cipher = cipher + encrypts
                        i[0] = 0


                    elif i[0] == 0:
                        cipher = cipher + encrypts

                    else:
                        print("Errors: " + str(encrypts))
                    
                

                elif single_space in encrypts:
                    cur = i[0]
                    i[0] = cur + 1
                    sp_c = sp_c - 1

        

            return decode



def main_launcher():
    print("Morse Coder Encoder/Generator")
    menu = "Available Choices are: \n 1. Convert Your Text into Morse Code\n 2. Convert Morse Code into Readable Text"
    print(menu)

    try:
        your_choice = int(input("Enter Your Choice > "))

        if your_choice == 1:

            try:
                your_text = str(input("Enter Your Text to Convert > "))
                access = morsecoders(your_text)
                output = access.encoders()
                print("Converted Text > " + str(output))
                
            except Exception as Error:
                print(Error)
    
        elif your_choice == 2:

            try:
                your_text = str(input("Enter Your Morse Code to Convert > "))
                access = morsecoders(your_text)
                output = access.decoders()
                print("Converted Morce Code > " + str(output))

            except Exception as Error:
                print(Error)

        else:
            print("Unavailable Option Selected")

    except Exception as Error:
        error_1 = "is not defined"
        error_2 = "invalid literal for int() with base 10: ''"
        
        if error_1 in str(Error):
            print("Invalid Input Entered")

        elif error_2 in str(Error):
            print("You Did not Enter Anything.")

        else:
            print("You did not enter correct input")

if __name__ == '__main__':
    main_launcher()

    continue_option = str(input("Type (Y) fcr Continue > "))

    if continue_option.upper() == "Y":
        main_launcher()
    else:
        print("ShutDown")
        
    

        
