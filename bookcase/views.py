from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from bookcase.models import BookCase
from bookcase.forms import BookCaseForm


def bookcaseall(request):
    bookcases = BookCase.objects.all()
    return render_to_response("bookcases/bookcaseall.html", {'bookcases': bookcases})


def bookcasesdetail(request, pk):
    bookcase = get_object_or_404(BookCase, pk=pk)
    return render_to_response("bookcases/bookcasedetail.html", {'bookcase': bookcase})


def bookcasenew(request):
    form = BookCaseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("bookcase:list")
    return render_to_response("bookcases/bookcasenew.html", {'form': form})


def bookcaseedit(request, pk):
    bookcase = get_object_or_404(BookCase, pk=pk)
    form = BookCaseForm(request.POST or None, instance=bookcase)

    if form.is_valid():
        form.save()
        return redirect("bookcase:list")
    return render_to_response("bookcases/bookcaseedit.html", {
        'bookcase': bookcase,
        'form': form
    }, context_instance=RequestContext(request))


def bookcasedelete(request, pk):
    bookcase = get_object_or_404(BookCase, pk=pk)

    if 'POST' == request.method:
        bookcase.delete()
        return redirect("bookcase:list")
    return render_to_response("bookcases/confirmdelete.html", {'object': bookcase})
