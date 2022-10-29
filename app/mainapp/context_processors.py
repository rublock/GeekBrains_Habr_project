from mainapp.models import Category


def demo_categories(request):
    demo_categories = ("Дизайн", "Веб-разработка", "Мобильная разработка", "Маркетинг")
    categories = Category.objects.values_list("name", flat=True)
    result = all(dc in categories for dc in demo_categories)
    return {"demo_categories": not result}
