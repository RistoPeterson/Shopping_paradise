from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def products(request):
    context = {
        'blog_entries': [
            {
                'footer': 'Black Friday Deal',
                'button': 'Order now',
            },
        ]
    }
    return render(request, "products.html", context)
