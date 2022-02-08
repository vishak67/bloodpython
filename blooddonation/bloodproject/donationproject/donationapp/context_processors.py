from . models import Centers, District


def menu_links(request):
    links = Centers.objects.all()
    return dict(links=links)


def list_links(request):
    dlinks = District.objects.all()
    return dict(dlinks=dlinks)
