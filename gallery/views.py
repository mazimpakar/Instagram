from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Image, GalleryLetterRecipients
from .forms import GalleryLetterForm,NewImageForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def gallery_today(request):
    date = dt.date.today()
    all_images = Image.all_images()
    images= Image.objects.all()
    print(images)
    # image = Image.today-gallery()
    if request.method == 'POST':
        form = GalleryLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            recipient = GalleryLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('gallery_today')
    else:
        form = GalleryLetterForm()
        form = NewImageForm()
    return render(request, 'todays_gallery.html', {"date": date,"letterForm":form, "ImageForm":form, "images":all_images},{'images':images})


def past_days_galley(request, past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(gallery_today)

    image = Image.days_gallery(date)
    return render(request, 'past_gallery.html',{"date": date,"image":image})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    title = 'New image'
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('todaysGallery')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form,"current_user":current_user,"title":title})