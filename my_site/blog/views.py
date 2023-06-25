from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "polish-mountains",
        "image": "tree.jpg",
        "author": "Nikodem",
        "date": date(2023, 6, 25),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! There are many beautyful summits in Poland!",
        "content": """
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                    Quis saepe atque adipisci dicta officiis accusantium qui quasi quaerat magnam velit necessitatibus, consequatur illum deleniti tenetur fuga, 
                    quia, laboriosam nobis. Similique.
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                    Quis saepe atque adipisci dicta officiis accusantium qui quasi quaerat magnam velit necessitatibus, consequatur illum deleniti tenetur fuga, 
                    quia, laboriosam nobis. Similique.

                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                    Quis saepe atque adipisci dicta officiis accusantium qui quasi quaerat magnam velit necessitatibus, consequatur illum deleniti tenetur fuga, 
                    quia, laboriosam nobis. Similique.

                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                    Quis saepe atque adipisci dicta officiis accusantium qui quasi quaerat magnam velit necessitatibus, consequatur illum deleniti tenetur fuga, 
                    quia, laboriosam nobis. Similique.
                    """
    },
    {
        "slug": "coding",
        "image": "coding.jpg",
        "author": "Nikodem",
        "date": date(2023, 6, 22),
        "title": "Coding",
        "excerpt": "Coding is the best! We love it so much and you know that it's the best!",
        "content": """
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                    Quis saepe atque adipisci dicta officiis accusantium qui quasi quaerat magnam velit necessitatibus, consequatur illum deleniti tenetur fuga, 
                    quia, laboriosam nobis. Similique.
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                    Quis saepe atque adipisci dicta officiis accusantium qui quasi quaerat magnam velit necessitatibus, consequatur illum deleniti tenetur fuga, 
                    quia, laboriosam nobis. Similique.
                    
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                    Quis saepe atque adipisci dicta officiis accusantium qui quasi quaerat magnam velit necessitatibus, consequatur illum deleniti tenetur fuga, 
                    quia, laboriosam nobis. Similique.

                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                    Quis saepe atque adipisci dicta officiis accusantium qui quasi quaerat magnam velit necessitatibus, consequatur illum deleniti tenetur fuga, 
                    quia, laboriosam nobis. Similique.
                    """
    },
    {
        "slug": "minecraft",
        "image": "mine.jpg",
        "author": "Nikodem",
        "date": date(2023, 6, 15),
        "title": "Minecraft",
        "excerpt": "Did you play minecraft? So you have to love it like me!",
        "content": """
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                    Quis saepe atque adipisci dicta officiis accusantium qui quasi quaerat magnam velit necessitatibus, consequatur illum deleniti tenetur fuga, 
                    quia, laboriosam nobis. Similique.
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                    Quis saepe atque adipisci dicta officiis accusantium qui quasi quaerat magnam velit necessitatibus, consequatur illum deleniti tenetur fuga, 
                    quia, laboriosam nobis. Similique.
                    
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                    Quis saepe atque adipisci dicta officiis accusantium qui quasi quaerat magnam velit necessitatibus, consequatur illum deleniti tenetur fuga, 
                    quia, laboriosam nobis. Similique.

                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
                    Quis saepe atque adipisci dicta officiis accusantium qui quasi quaerat magnam velit necessitatibus, consequatur illum deleniti tenetur fuga, 
                    quia, laboriosam nobis. Similique.
                    """
    }
]


def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
