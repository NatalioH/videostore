from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Movie
from .forms import MovieForm

def video_list(request):
    q = request.GET.get("q", "")
    movies = Movie.objects.all().order_by("-release_year", "movie_title")
    if q:
        movies = movies.filter(movie_title__icontains=q)
    return render(request, "videos/movie_list.html", {"movies": movies, "q": q})

def video_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "videos/movie_detail.html", {"movie": movie})

def video_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            messages.success(request, "Movie added.")
            return redirect("videos:detail", pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, "videos/movie_form.html", {"form": form, "mode": "Create"})

def video_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, "Movie updated.")
            return redirect("videos:detail", pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, "videos/movie_form.html", {"form": form, "mode": "Update", "movie": movie})

def video_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        messages.success(request, "Movie deleted.")
        return redirect("videos:list")
    return render(request, "videos/movie_confirm_delete.html", {"movie": movie})
