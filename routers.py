from app import api

from resourses.articles_resource import ArticlesResource
api.add_resource(ArticlesResource, '/articles', '/articles/<int:article_id>')
