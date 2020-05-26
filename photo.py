class Photo:
    def __init__(self, title, url, explanation, date, media_type):
        self.Title = title
        self.Url= url
        self.Explanation = explanation
        self.Date = date
        self.Media_type = media_type  
    
    
    '''def __init__(self, **args):
        self.Date = args.get('date')
        self.Explanation = args.get('explanation')
        self.Hdurl = args.get('hdurl')
        self.Media_type = args.get('mediaType')
        self.Title = args.get('title')'''