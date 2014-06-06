
def put_text_into_list():
    f = open("twain.txt")
    filetext = f.read()
    filetext_lower = filetext.lower()
    return filetext_lower

def parse_text(char_list):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    counts = [0]*26
    for letter in char_list:
        if letter in alphabet:
            pos = alphabet.index(letter)
            counts[pos] += 1
    print counts
    ## print char_list.count(letter), letter
    #a - 4
    #b - 8

def main():
    text_in_list = put_text_into_list()
    parse_text(text_in_list)

if __name__ == "__main__":
    main()