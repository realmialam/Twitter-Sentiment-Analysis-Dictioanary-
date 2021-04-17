punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def strip_punctuation(string):
    temp_str = string[:]
    for char in temp_str:
        if char in punctuation_chars:
            string=string.replace(char,'')
    return string
def get_pos(string):
    # strings defines one or more sentences.
    string = strip_punctuation(string)
    content = string.split()
    positive_word_count=0
    for word in content:
        if word in positive_words:
            positive_word_count = positive_word_count+1
    return positive_word_count
def get_neg(string):
    # string contain one or more sentences.
    string = strip_punctuation(string)
    contents=string.split()
    negative_word_count=0
    for word in contents:
        if word in negative_words:
            negative_word_count +=1
    return negative_word_count



fileref = open("project_twitter_data.csv",'rw')
outfile = open("resulting_data.csv",'w')
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write('\n')
lines = fileref.readlines()
for line in lines[1:]:
    line = line.strip().split(',')
    no_retweet = line[1]
    no_replies = line[2]
    #print(line[0])
    pos_score = get_pos(line[0])
    
    neg_score = get_neg(line[0])
    
    net_score = pos_score - neg_score
    #print(pos_score,end=" ")
    #print(neg_score,end=" ")
    #print(net_score)
    row_string="{},{},{},{},{}".format(no_retweet,no_replies,pos_score,neg_score,net_score)
    #print(row_string)
    outfile.write(row_string)       
    outfile.write('\n') 
