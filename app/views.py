from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render

from .forms import UploadFileForm
from .models import File


@login_required
def profile_details(request):
    files = File.objects.filter(profile=request.user)
    return render(request, 'profile.html', {
        'profile': request.user, 'files': files
    })


MAX_UPLOAD_SIZE = "5242880"


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data.get('file')
            if file.size > int(MAX_UPLOAD_SIZE):
                return HttpResponseBadRequest
            file_model = File(
                title=form.cleaned_data.get('title'),
                profile=request.user,
                upload=file
            )
            file_model.save()
            return HttpResponseRedirect('/all_files')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


@login_required
def all_files(request):
    files = File.objects.all()
    return render(request, 'files.html', {'files': files})
