from connect_database import getDatabase
from check_engin import find_word_list, check_related
import json
import ast



# search the given topic in database, then return the list of
# articles' id in database.
def get_articles_name(topic):

    title_list = []
    # delete'#' if "#" is at the very begining
    if topic[0] == "#":
        topic = topic[1:]
    # put the topic in the pattern of " **_**_** "
    # we have two kind patterns for each topic. One takes care of space,
    # another doesn't
    topic = find_word_list(topic)

    client = getDatabase()
    db = client.lyl
    contents = db.link_content.find()
    client.close()
    for content in contents:
        title = content["title"]
        tags = content["tags"]

        if check_related(topic, tags, title):
            title_list += [content["title"]]

    return ast.literal_eval(json.dumps(title_list))
