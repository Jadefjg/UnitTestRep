from pydantic import BaseModel,EmailStr

from src.blog.models import Article,NotFound

class AlreadyExists(Exception):
    pass

class CreateArticleCommand(BaseModel):
    author:EmailStr
    title:str
    content:str

    def excute(self) -> Article:
        try:
            Article.get_by_title(self.title)
            raise AlreadyExists
        except NotFound:
            pass

        article = Article(
            author = self.author,
            title = self.title,
            context = self.content
        ).save()

        return article


