from django.shortcuts import render, redirect

from .forms import BlogForm
from core.utils.utils import prepare_content_to_save
from core.utils.github_utils import push_to_github, fetch_from_github


def blog_list(request):
    file_location = "blogs"
    
    blogs = fetch_from_github(file_location)
    return render(request, "blog/blog_list.html", {"blogs": blogs})


def create_blog(request):
    file_location = "blogs"
    
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            format_choice = form.cleaned_data["format_choice"]

            # Save to file and push to GitHub
            file_name, content = prepare_content_to_save(title, content, format_choice)
            push_to_github(file_location, file_name, content)

            return redirect("blog_list")
    else:
        form = BlogForm()

    return render(request, "blog/create_blog.html", {"form": form})
