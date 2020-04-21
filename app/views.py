from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UploadFileForm
from .models import File


@login_required
def profile_details(request):
    return render(request, 'profile.html', {'profile': request.user})


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = File(
                title=form.cleaned_data.get('title'),
                profile=request.user,
                upload=form.cleaned_data.get('file')
            )
            file.save()
            return HttpResponseRedirect('/my_files')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


@login_required
def my_files(request):
    files = File.objects.filter(profile=request.user)
    return render(request, 'files.html', {'files': files})
