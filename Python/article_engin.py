from search_articles import get_articles_name

def get_articles(sections):
	i=1
	outdata=''
	for section in sections:
		outdata += str(get_articles_name(str(section)))
		#outdata += [get_articles_name(str(section)]
		 

	return  outdata
		