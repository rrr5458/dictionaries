# Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word. For example:

# $ python3 letter_histogram.py
# Please enter a word: banana
# {'a': 3, 'b': 1, 'n': 2}

word_input = input("Please enter a word: ")

def letter_summary(word):
    dictionary = {}
    for letter in word_list:
        count = word.count(letter)
        dictionary[letter] = count
    return dictionary

print(letter_summary(word_input))

#sentnece histogram

sentence_input = """Pop the trunk I open up I sold my soul for a good price
Outta' sight, and my hoe got talent right
Whole squad ran through that shit yikes
What can I say I'm a business man I did my business man
But 'Imma bend it down and I'mma lick her up, then dick her down
She gon' turn around then I'm gon' kick her out
She gon' talk that shit but say
How you make it up, how you fake a love?
Holy son, I was the chosen one of she gon' kiss and tell
She keep my wishes well (but) I don't need her, well
How my enemy a friend of me?
Why yall feed off my energy, like I ain't dead yet
Higher entity foreign bitch that thinks she into me with the foreign very viciously
Why these dudes wanna take pics with me?
She said she gay but still into me, said she gay but still into me
Said that she hates that I'm in the streets
And said that I hate that I'm in the streets
I wanna blow up and make history
And she said that she hates my Insta feed
Xans don't make you
Xans gon' take you
Xans gon' fake you and
Xans gon' betray you
Xans don't make you
Xans gon' take you
Xans gon' fake you and
Xans gon' betray you
And her pussy tastes like skittles, what?
Yeah, ayy, and you can really taste the rainbow, what? (hah, no)
Yo' bitch just like a crayola (what, ayy)
You can draw her on the table, flip her like some yola
Heart shaped kisses
I really miss my mistress
666, evil bitches want my mentions
Heart shaped kisses
I really miss my mistress, and the
666, evil bitches want my mentions
Xans don't make you
Xans gon' take you
Xans gon' fake you and
Xans gon' betray you
Xans don't make you
Xans gon' take you
Xans gon' fake you and
Xans gon' betray you
Xans gon' fake you
Xans gon' betray you
Xans gon' take you
Xans gon' betray you
Xans gon' take you
Xans gon' take you
What, what aye
Xans gon' take you, xans gon' take you
Xans gon'
Xans' gon take you
Xans' gon take you
 """

def word_summarry(word):
    sentence_list_one = sentence_input.split()
    dictionary_sentence = {}
    for word in sentence_list_one:
        count = sentence_input.count(word)
        dictionary_sentence[word] = count
    sorted_list = [("a", 0), ("b", 0), ("c", 0)]
    for key in dictionary_sentence: 
        if dictionary_sentence[key] > sorted_list[0][1]:
            sorted_list[0] = [key, dictionary_sentence[key]]
    for key in dictionary_sentence: 
        if dictionary_sentence[key] < sorted_list[0][1] and dictionary_sentence[key] > sorted_list[1][1]:
            sorted_list[1] = [key, dictionary_sentence[key]]
    for key in dictionary_sentence: 
        if dictionary_sentence[key] < sorted_list[1][1] and dictionary_sentence[key] > sorted_list[2][1]:
            sorted_list[2] = [key, dictionary_sentence[key]]
    num_one = sorted_list[0]
    num_two = sorted_list[1]
    num_three = sorted_list[2]
    print(f'''Your top three most used words are:
    {num_one[0]} : {num_one[1]}
    {num_two[0]} : {num_two[1]}
    {num_three[0]} : {num_three[1]}
    ''')
    return sorted_list

 

word_summarry(sentence_input)





