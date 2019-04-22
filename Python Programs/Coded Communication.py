#Hey there! How have you been? I've been great!
#I just learned about this really cool type of cipher called a  Caesar Cipher.
#Here's how it works:
#You take your message, something like "hello" and then you shift all of the letters by a certain offset.
#For example, if I chose an offset of 3 and a message of "hello",
#I would code my message by shifting each letter 3 places to the left (with respect to the alphabet).
#So "h" becomes "e", "e" becomes, "b", "l" becomes "i", and "o" becomes "l". Then I have my coded message,"ebiil"!
#Now I can send you my message and the offset and you can decode it. The best thing is that Julius Caesar himself used this cipher,
#that's why it's called the Caesar Cipher! Isn't that so cool! Okay,
#now I'm going to send you a longer coded message that you have to decode yourself!

#xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!

#This message has an offset of 10. Can you decode it?

alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
translated_message = ""
for letter in message:
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        translated_message += alphabet[(letter_value + 10) % 26]
    else:
        translated_message += letter
print(translated_message)

new_message = "This message will be the test to see whether I can code well! Lets give it a shot i guess.."
translated_new_message = ""
for letter in new_message:
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        translated_new_message += alphabet[(letter_value - 10) % 26]
    else:
        translated_new_message += letter
print(translated_new_message)

def decoder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message

def coder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value - offset) % 26]
        else:
            translated_message += letter
    return translated_message

first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

print(decoder(first_message, 10))
print(decoder(second_message, 14))

third_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for i in range(1,26):
    print("offset: " + str(i))
    print("\t " + decoder(third_message, i) + "\n")

fourth_message = "dfc jhjj ifyh yf hrfgiv xulk? vmph bfzo! qtl eeh gvkszlfl yyvww kpi hpuvzx dl tzcgrywrxll!"

def new_decoder(coded_message, keyword):
    keyword_repeated = ''
    while len(keyword_repeated) < len(coded_message):
        keyword_repeated += keyword
    keyword_final = keyword_repeated[0:len(coded_message)]
    translated_message = ''
    for i in range(0,len(coded_message)):    
        if not coded_message[i] in punctuation:
            ln = alphabet.find(coded_message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += coded_message[i]
    return translated_message

message = "dfc jhjj ifyh yf hrfgiv xulk? vmph bfzo! qtl eeh gvkszlfl yyvww kpi hpuvzx dl tzcgrywrxll!"
keyword = "friends"

print(new_decoder(message, keyword))

def new_coder(message, keyword):
    keyword_repeated = ''
    while len(keyword_repeated) < len(message):    
        keyword_repeated += keyword
    keyword_final = keyword_repeated[0:len(message)]
    translated_message = ''
    for i in range(0,len(message)):
        if message[i] not in punctuation:
            ln = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += message[i]
    return translated_message
