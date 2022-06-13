from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница!')


def mariya(request):
    return HttpResponse('Ну вот, пока ты стояла, я внёс изменения в сайт! :)')
