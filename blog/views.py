from django.shortcuts imp*ort render


def post_list(request):
    return render(request, 'blog/post_list.html', {})

# Create your views here.
