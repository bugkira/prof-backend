from .models import Article, ContactInfo, Section


def contact_info(request):
    info = (
        ContactInfo.objects.first()
    )  # Предполагаем, что у нас есть хотя бы одна запись
    return {"contact_info": info}


def breadcrumbs(request):
    path = (request.path[1:]).split("/")
    lst = []
    for i in range(0, len(path) - 1):
        part_path = "/".join(j for j in path[: i + 1])
        lst.append({"link": "/" + part_path, "cat_name": path[i]})
    return {"breadcrumbs": lst}


def dfs(request):
    return {"nodes": Section.objects.all()}
