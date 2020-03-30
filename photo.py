class photo:
    
    def __init__(self, **args):
        self.date = args.get('date')
        self.explanation = args.get('explanation')
        self.hdurl = args.get('hdurl')
        self.mediaType = args.get('mediaType')
        self.title = args.get('title')
