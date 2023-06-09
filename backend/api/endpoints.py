from django.http import JsonResponse
from rest_framework.decorators import api_view
from .calculation_engine import calculate_bond_metrics
from .data_processing import parse_input_data, format_output_data

@api_view(['POST'])
def process_bond_data(request):
    input_data = request.data
    print(input_data)
    parsed_data = parse_input_data(input_data)
    selected_metrics = input_data.get('selectedMetrics', {})
    calculated_metrics = calculate_bond_metrics(parsed_data, selected_metrics)
    formatted_output = format_output_data(calculated_metrics)

    return JsonResponse(formatted_output, safe=False)
