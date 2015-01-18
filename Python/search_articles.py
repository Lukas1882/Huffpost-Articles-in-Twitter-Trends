from connect_database import getDatabase
from check_engin import find_word_list,check_related


# search the given topic in database, then return the list of
# articles' id in database.
def get_articles_name(topic):

    id_list =[]
    # delete'#' if "#" is at the very begining
    if topic[0]=="#":
       topic=topic[1:]
    topic=find_word_list(topic)

    
    db = getDatabase().lyl
    contents = db.link_content.find()
    for content in contents:
        title = content["title"]
        tags = content["tags"]

        if check_related(topic,tags,title):
          id_list +=  {content["title"]};

    return id_list


