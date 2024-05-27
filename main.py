from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True 
    rating: Optional[int] = None

my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favourite foods", "content": "I like pizza", "id": 2}
]

@app.get("/")
def root():
    return {"message": "<3"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.model_dump()  # Correct usage of model_dump()
    post_dict['id'] = len(my_posts) + 1  # Assign an ID to the new post
    my_posts.append(post_dict)
    return {"data": post_dict}
