# collect all the articles' title in a list from different sections


from search_articles import get_articles_name


def get_articles(sections):
    i = 1
    title_list = []
    for section in sections:
        for title in get_articles_name(str(section)):
            title_list += [title]
    return title_list