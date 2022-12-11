from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from .form import *
from .models import *
from account.models import Profile
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def main_page(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, pk=request.user.pk)
        context = {"tests": Test.objects.all(), 'profile': profile.submission.all()}
    else:
        context = {"tests": Test.objects.all()}

    return render(request, 'core/main.html', context)


@login_required(login_url='login')
def solution_test(request, pk):
    test = get_object_or_404(Test, pk=pk)
    profile = get_object_or_404(Profile, pk=request.user.pk)

    post_data = request.POST if request.method == "POST" else None
    form = TestForm(test, request.user.pk, request.user.username, post_data)
    if form.is_bound and form.is_valid():
        form.save()
        return redirect('main_page')

    context = {'test': test, 'form': form}
    return render(request, 'core/solution.html', context)


@login_required(login_url='login')
def result(request, title):
    result = get_object_or_404(Profile, pk=request.user.pk)

    try:
        if result.submission.get(title=title):
            result_total = result.submission.get(title=title).submission_set.filter(profile_submission=request.user).last()
            сorrect_percentage = "{0:.2f}".format(result_total.Number_of_correct_answers /
                                                  result.submission.get(title=title).question_set.count() * 100)
            context = {'result': result_total, 'сorrect_percentage': сorrect_percentage}
    except:
        return redirect('main_page')

    return render(request, 'core/result.html', context)




