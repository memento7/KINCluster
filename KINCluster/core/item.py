import settings

class Item:
    def __init__(self, title, content, date, keyword):
        """
            for using raw string, just return raw string in __str__
        """
        self.title = title
        self.content = content
        self.date = date
        self.keyword = keyword

    def __str__(self):
        """
            implemente function for document
        """
        return " ".join([self.title * settings.ITEM_TITLE_RATE,
                         self.content * settings.ITEM_CONTENT_RATE,
                         self.date * settings.ITEM_DATE_RATE,
                         self.keyword * settings.ITEM_KEYWORD_RATE])

    def __repr__(self):
        return " ".join([self.title,
                        self.content,
                        self.date,
                        self.keyword])

    # custom variable
    params = {
            'ITEM_TITLE_RATE': settings.ITEM_TITLE_RATE,
            'ITEM_CONTENT_RATE': settings.ITEM_CONTENT_RATE,
            'ITEM_DATE_RATE': settings.ITEM_DATE_RATE,
            'ITEM_KEYWORD_RATE': settings.ITEM_KEYWORD_RATE,
        }