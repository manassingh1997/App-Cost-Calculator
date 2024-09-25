from django.shortcuts import render

from django.http import JsonResponse

APP_FEATURES = {
    "ecommerce": {
        "Product Listing": 30,
        "Payment Integration": 25
    },
    "social_media": {
        "User Profiles": 30,
        "Chat System": 40
    },
    "cloud_kitchen": {
        "Menu Display": 25,
        "Online Ordering": 40
    }
}


def calculate_cost(request):
    selected_category = request.GET.get('category')
    selected_features = request.GET.getlist('features[]')  # Array of selected features

    if not selected_category :
        return JsonResponse({'error': 'Please select a category and at least one feature'}, status=400)
    
    if not selected_features or all(feature == '' for feature in selected_features):
        return JsonResponse({'error': 'Please select at least one feature'}, status=400)

    # Check if the selected_category exists in APP_FEATURES
    
    total_hours = sum(APP_FEATURES[selected_category][feature] for feature in selected_features)
    total_cost = total_hours * 10

    return JsonResponse({'total_cost': total_cost})

def showCalculator(request):
    return render(request,'cost_calculator.html')