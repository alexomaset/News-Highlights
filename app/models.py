class Sources:
    '''
    Sources class that defines source objects
    '''
    def __init__(self,id,name,author,description,url,category,urlToImage,title):
        '''
        Function that initiates the sources class
        '''
        self.id = id
        self.name = name
        self.author = author
        self.description = description
        self.url = url
        self.category = category
        self.urlToImage = urlToImage
        self.title = title
       

class Articles:
    '''
    Article class that defines the article objects
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
