from connect_database import getDatabase
from check_engin import find_word_list,check_related


# search the given topic in database, then return the list of
# articles' id in database.
def search_db(topic):
    id_list =[]
    # delete'#' if "#" is at the very begining
    if topic[0]=="#":
       topic=topic[1:]
    topic=find_word_list(topic)
    print "search for",topic

    
    db = getDatabase()
    contents = db.link_content.find()
    for content in contents:
        title = content["title"]
        tags = content["tags"]

        if check_related(topic,tags,title):
          id_list.append(content["_id"]);
    return id_list


search_db("joeBiden")
