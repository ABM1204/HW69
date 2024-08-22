from django.http import JsonResponse
import json


def validate_data(data):
    if not isinstance(data, dict):
        return False, "Error. Invalid input"
    try:
        a = float(data.get("A"))
        b = float(data.get("B"))
    except (ValueError, TypeError):
        return False, "A and B must be numbers."
    return True, (a, b)


def add_view(request):
    data = json.loads(request.body)
    valid, result = validate_data(data)
    if not valid:
        return JsonResponse({"error": result}, status=400)
    a, b = result
    return JsonResponse({"answer": a + b})

def subtract_view(request):
    data = json.loads(request.body)
    valid, result = validate_data(data)
    if not valid:
        return JsonResponse({"error": result}, status=400)
    a, b = result
    return JsonResponse({"answer": a - b})

def multiply_view(request):
    data = json.loads(request.body)
    valid, result = validate_data(data)
    if not valid:
        return JsonResponse({"error": result}, status=400)
    a, b = result
    return JsonResponse({"answer": a * b})

def divide_view(request):
    data = json.loads(request.body)
    valid, result = validate_data(data)
    if not valid:
        return JsonResponse({"error": result}, status=400)
    a, b = result
    if b == 0:
        return JsonResponse({"error": "You divide num by zero!"}, status=400)
    return JsonResponse({"answer": a / b})


