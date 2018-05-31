from products.models import Product

def get_menu_items(request):
    all_products = Product.objects.all()
    cat_set = list(set([(category.category).lower() for category in all_products]))
    return {'categories': cat_set }