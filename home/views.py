from django.shortcuts import render

# Create your views here.


def index(request):
    template_data = {}

    template_data["title"] = "Movies Store"
    return render(request, "home/index.html", {"template_data": template_data})


def about(request):
    template_data = {}

    template_data["title"] = "About"
    unused_variable = 42  # Variable sin usar

    return render(request, "home/about.html", {"template_data": template_data})
