from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from authors.models import Author
from authors.forms import AuthorForm


def authorall(request):
    authors = Author.objects.all()
    return render_to_response("authors/authorall.html", {'authors': authors})


def authordetail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render_to_response("authors/authordetail.html", {'author': author})


def authornew(request):
    form = AuthorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('author:list')

    return render_to_response("authors/authornew.html", {
        'form': form
    }, context_instance=RequestContext(request))


def authoredit(request, pk):
    author = get_object_or_404(Author, pk=pk)
    form = AuthorForm(request.POST or None, instance=author)

    if form.is_valid():
        form.save()
        return redirect("author:detail", pk=author.id)
    return render_to_response("authors/authoredit.html", {
        'author': author,
        'form': form
    }, context_instance=RequestContext(request))


def authordelete(request, pk):
    author = Author.objects.get(pk=pk)

    if 'POST' == request.method:
        author.delete()
        return redirect('author:all')

    return render_to_response('authors/confirmdelete.html', {'object': author})
