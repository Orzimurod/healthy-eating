from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            print(form.errors)
    else:
        print('GET request received')
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
