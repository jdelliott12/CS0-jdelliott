import string

def analyze_text(text):

    no_punct = text.translate(str.maketrans('', '', string.punctuation))

    words = no_punct.split()

    e_words = [word for word in words if 'e' in word.lower()]

    print("The text contains {} words, and out of those words {} ({:.1f}%) have the letter \"e\".".format(len(words), len(e_words), len(e_words) / len(words) * 100))


text = """
Old man, look at my life
I'm a lot like you were
Old man, look at my life
I'm a lot like you were                                                                                                                                             
Old man, look at my life
Twenty-four, and there's so much more
Live alone in a paradise
That makes me think of two                                                                                                                               
Love lost, such a cost
Give me things that don't get lost
Like a coin that won't get tossed
Rolling home to you                                                                                                                                                
Old man, take a look at my life, I'm a lot like you
I need someone to love me the whole day through
Ah, one look in my eyes and you can tell that's true
"""

analyze_text(text)  