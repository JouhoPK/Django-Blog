from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "best-monitors",
        "image": "jouho.jpg",
        "author": "Jouho",
        "date": date(2021, 12, 12),
        "title": "Best Monitors",
        "excerpt": "If you want to professionally code, or do anything on a computer really, you need a monitor. In this post, I will be recommending lots of different monitors...",
        "detail": '''Lorem ipsum, dolor sit amet consectetur adipisicing elit. Veniam blanditiis natus
        eius dolor odio officia labore porro iste a nemo, earum hic error officiis 
        assumenda eveniet vel modi incidunt et.
        
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Veniam blanditiis natus
        eius dolor odio officia labore porro iste a nemo, earum hic error officiis 
        assumenda eveniet vel modi incidunt et.
        
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Veniam blanditiis natus
        eius dolor odio officia labore porro iste a nemo, earum hic error officiis 
        assumenda eveniet vel modi incidunt et.'''
    },

    {
        "slug": "best-monitors",
        "image": "jouho.jpg",
        "author": "Jouho",
        "date": date(2021, 12, 12),
        "title": "Best Monitors",
        "excerpt": "If you want to professionally code, or do anything on a computer really, you need a monitor. In this post, I will be recommending lots of different monitors...",
        "detail": '''Lorem ipsum, dolor sit amet consectetur adipisicing elit. Veniam blanditiis natus
        eius dolor odio officia labore porro iste a nemo, earum hic error officiis 
        assumenda eveniet vel modi incidunt et.
        
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Veniam blanditiis natus
        eius dolor odio officia labore porro iste a nemo, earum hic error officiis 
        assumenda eveniet vel modi incidunt et.
        
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Veniam blanditiis natus
        eius dolor odio officia labore porro iste a nemo, earum hic error officiis 
        assumenda eveniet vel modi incidunt et.'''
    },

    {
        "slug": "best-monitors",
        "image": "jouho.jpg",
        "author": "Jouho",
        "date": date(2021, 12, 12),
        "title": "Best Monitors",
        "excerpt": "If you want to professionally code, or do anything on a computer really, you need a monitor. In this post, I will be recommending lots of different monitors...",
        "detail": '''Lorem ipsum, dolor sit amet consectetur adipisicing elit. Veniam blanditiis natus
        eius dolor odio officia labore porro iste a nemo, earum hic error officiis 
        assumenda eveniet vel modi incidunt et.
        
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Veniam blanditiis natus
        eius dolor odio officia labore porro iste a nemo, earum hic error officiis 
        assumenda eveniet vel modi incidunt et.
        
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Veniam blanditiis natus
        eius dolor odio officia labore porro iste a nemo, earum hic error officiis 
        assumenda eveniet vel modi incidunt et.'''
    },
]

def get_date(post):
    return post["date"]



def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "latest_posts": latest_posts
    })


def posts(request):
    return render(request, "blog/posts.html", {
        "all_posts": all_posts
    })


def single_post(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })