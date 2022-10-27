from mainapp.models import Category


def demo_categories(request):
    result = not (
        "Дизайн" and "Веб-разработка" and "Мобильная разработка" and "Маркетинг"
    ) in Category.objects.values_list("name", flat=True)
    return {"demo_categories": result}
