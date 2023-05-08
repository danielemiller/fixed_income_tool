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

@api_view(['GET'])
def fetch_bond_data_list(request):
    # Replace with the actual list of CUSIPs you want to fetch.
    cusip_list = ['594918AD6', '037833DE7', '9128284J6', '594918AD6']

    def fetch_and_format_bond_data(cusip):
        return format_description_data(
            parse_bond_description(
                get_bond_description(cusip)
            )
        )

    bond_data_list = [fetch_and_format_bond_data(cusip) for cusip in cusip_list]

    return JsonResponse(bond_data_list, safe=False)

