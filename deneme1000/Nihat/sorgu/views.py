from django.shortcuts import render,get_object_or_404                        # elave edilmeyen sual ve ya cavab olduqda 404 susmaya qarsi

from django.http import HttpResponseRedirect                                 # elaqe funksiyasi dasiyir

from django.urls import reverse                                              # urlde yaratdigimiz name sablon adlarindan istifade ucun

from .models import Sual,Cavab                                               # modelde yaratdigimiz sual,cavab modellerinin tanitimi


def esas(request):                                                           # esas sehife funksiyam
    latest_question_list = Sual.objects.order_by('-cap_tarixi')[:5]          # qeyd olunan en son 5 sual

    context = {'latest_question_list': latest_question_list}

    return render(request, 'sorgu/esas.html', context)                       # html file ile etrafli(detail) sehifeye kecidin yaradilmasi


def etrafli(request, question_id):                                           # etrafli yeni cavablarin oldugu sehife
    question = get_object_or_404(Sual, pk=question_id)

    return render(request, 'sorgu/etrafli.html', {'question': question})


def netice(request, question_id):                                            # sesvermeden sonra acilan sehife
    question = get_object_or_404(Sual, pk=question_id)

    return render(request, 'sorgu/netice.html', {'question': question})


def vote(request, question_id):                                              # vote(sesverme) sehifesi
    question = get_object_or_404(Sual, pk=question_id)

    try:

        selected_choice = question.cavab_set.get(pk=request.POST['cavab57'])

    except (KeyError, Cavab.DoesNotExist):

        return render(request, 'sorgu/etrafli.html', {                       # sesvermenin netice sehifesine yansimasi ucun kecid
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    else:

        selected_choice.votes += 1

        selected_choice.save()

        return HttpResponseRedirect(reverse('sorgu:netice', args=(question.id,)))