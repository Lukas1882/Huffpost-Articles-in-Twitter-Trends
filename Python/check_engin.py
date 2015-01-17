# this return the possible words in a Twitter topic
# For example, put "hi JackAndJoke" into {"hi","Jack","And","Joke"}
#remove the unnecessary characters
def refineStr(str):
    while '__' in str:
        str = str.replace('__','_')
    return str

def find_word_list(topic):
    word_list=''
    key_word=[]
    #the index of the char in this topic
    i=0
    #the index of the last uppercase in the topic
    j=0
    # check the uppercase and space
    while i<len(topic):
       if topic[i].isupper():
         #add this word into word list
         word_list += topic[j:i]+'_'
         j=i
       if topic[i]==' ' :
         word_list+=topic[j:i]+'_'
         j=i+1
       i=i+1
    word_list += topic[j:i]

    if word_list[0:1] =='_':
        key_word =  [refineStr(word_list[1:])]
    else:
        key_word = [refineStr(word_list)]
    # only check the space
    i=0
    j=0
    word_list=''
    while i<len(topic):
       if topic[i]==' ' :
         word_list+=topic[j:i]+'_'
         j=i+1
       i=i+1
    word_list += topic[j:i]
    key_word += [refineStr(word_list)]
    return key_word


# check if this topic related to the tags and title.
def check_related(word_list,tags,title):
   
   
    tags = str(tags).replace(' ','_')
    title = str(title).replace(' ','_')
   
    # Check in tag list first, if there is a word appears in tags, consider it as related to it.
    for word in word_list:
        if word.lower() in title.lower():
            return True

    # Check in the article's title
        # the number of word in the topic
    num=len(word_list)
        # the number of identification
    i=0
    for word in word_list:
        if word.lower() in title.lower():
            i=i+1
    # check if the identification enough to prove the relation.
    if num%2 == 1:
        if i >= num/2 + 1:
           return True
    if num%2 == 0:
        if i>num/2:
            return True
    # no relation, return false
    return False
