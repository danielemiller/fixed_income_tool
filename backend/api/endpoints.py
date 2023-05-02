from django.http import JsonResponse
from rest_framework.decorators import api_view
from .calculation_engine import calculate_bond_metrics
from .data_processing import parse_input_data, format_output_data, get_bond_description, parse_bond_description, format_description_data

@api_view(['POST'])
def process_bond_data(request):
    input_data = request.data
    print(input_data)
    parsed_data = parse_input_data(input_data)
    selected_metrics = input_data.get('selectedMetrics', {})
    calculated_metrics = calculate_bond_metrics(parsed_data, selected_metrics)
    formatted_output = format_output_data(calculated_metrics)

    return JsonResponse(formatted_output, safe=False)

def fetch_bond_data_list(request):
    # Replace with the actual list of CUSIPs you want to fetch.
    cusip_list = ['123456789', '987654321']
    
    bond_data_list = []
    for cusip in cusip_list:
        raw_bond_data = get_bond_description(cusip)
        parsed_bond_data = parse_bond_description(raw_bond_data)
        formatted_bond_data = format_description_data(parsed_bond_data)
        bond_data_list.append(formatted_bond_data)

    return JsonResponse(bond_data_list, safe=False)
