from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import BookForm
# Create your views here.


def book_list(request):
    books = Book.objects.all()

    return render(request, 'book_list.html', {'books': books})

def book_create(request):
    data = dict()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Book.objects.all()
            data['html_book_list'] = render_to_string('partial_book_list.html', {
                'books': books
            })
        else:
            data['form_is_valid'] = False
    else:
        form = BookForm()

    context = {'form': form}
    data['html_form'] = render_to_string('partial_book_create.html',
        context,
        request=request
    )
    return JsonResponse(data)
