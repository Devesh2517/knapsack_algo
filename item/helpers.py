from rest_framework.response import Response

def custom_response(result, message, status):
    return Response({
                    'data': result,
                    'message': message
                    }, status=status)
