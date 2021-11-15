

class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f"Blog(title{self.title}, author={self.author}," \
               f" posts={self.posts})"

    def create_post(self, title, content):
        pass

    def json(self):
        pass
