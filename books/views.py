from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from books.models import Books
from books.forms import BookForm


def home(request):
    return render_to_response("index.html")


def bookall(request):
    books = Books.objects.all()
    context = {
        'books': books
    }
    return render_to_response('books/bookall.html', context)


def bookdetail(request, pk):
    book = Books.objects.get(pk=pk)
    context = {
        'book': book
    }

    return render_to_response('books/bookdetail.html', context)


def booknew(request):
    # generic 'old' way
    if 'POST' == request.method:
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book:list')
    else:
        form = BookForm()

    return render_to_response('books/booknew.html', {
        'form': form
    }, context_instance=RequestContext(request))


def bookedit(request, pk):
    book = get_object_or_404(Books, pk=pk)
    # best practice
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('book:detail', pk=book.id)
    return render_to_response('books/bookedit.html', {
        'form': form,
        'book': book
    }, context_instance=RequestContext(request))


def bookdelete(request, pk):
    book = Books.objects.get(pk=pk)

    if 'POST' == request.method:
        book.delete()
        return redirect('book:all')

    return render_to_response('books/confirmdelete.html', {'object': book})
