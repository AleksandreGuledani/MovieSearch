from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)  

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            
            
            html = render_to_string('contact/emails/contactform.html', {
                'name' : name,
                'email' : email,
                'content' : content
            })

           
            send_mail(
                '',  
                '',  
                'hijo@c',  
                ['a.guledani11@gmail.com'],    
                fail_silently=False,
                html_message=html  
            )

            return redirect('index')  
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {  
        'form': form  
    })
