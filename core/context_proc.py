from .models import ContactInfo


def contact_info(request):
    info = (
        ContactInfo.objects.first()
    )  # Предполагаем, что у нас есть хотя бы одна запись
    return {"contact_info": info}
