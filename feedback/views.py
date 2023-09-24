from django.shortcuts import render
from .forms import feedbackForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required()
def feedback_view(request):
    if request.method == 'POST':
        form = feedbackForm(request.POST or None)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.email = request.user.email
            form.save()
            messages.success(request, 'Form submission successful 👍')
            form = feedbackForm()
    else:
        form = feedbackForm()

    context = {'form': form}
    return render(request, 'feedback.html', context)


