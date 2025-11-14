from django.shortcuts import render, get_object_or_404
from .models import Category, Package
from .forms import PackageFilterForm

def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def category_packages(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    packages = Package.objects.filter(category=category)
    
    # Filtering logic
    form = PackageFilterForm(request.GET)
    if form.is_valid():
        package_level = form.cleaned_data.get('package_level')
        price_type = form.cleaned_data.get('price_type')
        max_price = form.cleaned_data.get('max_price')
        
        if package_level:
            packages = packages.filter(package_level=package_level)
        if price_type:
            packages = packages.filter(price_type=price_type)
        if max_price:
            packages = packages.filter(price__lte=max_price)
    
    # Group packages by level for display
    local_packages = packages.filter(package_level='local')
    vip_packages = packages.filter(package_level='vip')
    vvip_packages = packages.filter(package_level='vvip')
    
    context = {
        'category': category,
        'local_packages': local_packages,
        'vip_packages': vip_packages,
        'vvip_packages': vvip_packages,
        'form': form,
    }
    return render(request, 'category_packages.html', context)

def package_detail(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    package_images = package.packageimage_set.all()
    
    # Split includes and excludes into lists
    includes_list = package.includes.split(',') if package.includes else []
    excludes_list = package.excludes.split(',') if package.excludes else []
    
    context = {
        'package': package,
        'package_images': package_images,
        'includes_list': includes_list,
        'excludes_list': excludes_list,
    }
    return render(request, 'package_detail.html', context)