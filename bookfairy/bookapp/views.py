from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from forms import BookForm

def index(request):
    # Code to lookup book availability
    if request.method == 'POST': # If the form has been submitted...
        print "in post"
        form = BookForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            print "in is_valid"
            book_title = form.cleaned_data['book_title']
            print book_title
            # TODO: Add code htere to lookup if the book is checked in
            
            # TODO: is the bookchecked in?
            is_checked_in = True
            return render(request, 'booklist.html', { 'book_title': book_title, 'is_checked_in': is_checked_in } )
    else:
        form = BookForm() # An unbound form

    return render(request, 'index.html', {
        'form': form,
    })
    #return render(request, 'index.html')
    #return HttpResponse("Hello, world. You're at the book fairy.")

def booklist(request):
    return render(request,'booklist.html')
