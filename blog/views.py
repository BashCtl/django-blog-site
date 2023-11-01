from django.shortcuts import render
from datetime import date
# Create your views here.

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Darko",
        "date": date(2023, 11 ,1),
        "title": "Mountain Hiking",
        "excerpt": "There's nothng like the views you get when hiking in the mountains! And I wasn't even happened while I was enjoying the view!",
        "content": """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Minus consequuntur voluptatibus beatae fugiat optio est, 
                    vero distinctio perferendis enim saepe quisquam assumenda natus, 
                    pariatur animi odio sit repudiandae quidem dolore?

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Minus consequuntur voluptatibus beatae fugiat optio est, 
                    vero distinctio perferendis enim saepe quisquam assumenda natus, 
                    pariatur animi odio sit repudiandae quidem dolore?

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Minus consequuntur voluptatibus beatae fugiat optio est, 
                    vero distinctio perferendis enim saepe quisquam assumenda natus, 
                    pariatur animi odio sit repudiandae quidem dolore?
                    """


    },
     {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Darko",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Darko",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }

]

def get_date(post):
    return post.get("date")

def home_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    context = {"posts": latest_posts}
    return render(request, "blog/index.html", context)

def posts(request):
    context = {"posts": all_posts}
    return render(request, "blog/all-posts.html", context)

def post_detail(request, slug):
    post = next(post for post in all_posts if post["slug"] == slug)
    context = {"post": post}
    return render(request, "blog/post-detail.html", context)