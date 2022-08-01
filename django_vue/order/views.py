import stripe
from django.conf import settings
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import OrderSerializer


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid(True):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = 0
        for item in serializer.validated_data['book_items']:
            paid_amount += item.get('quantity') * item.get('price')

        try:
            stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency='USD',
                description='Charge from Tvtri',
                source=serializer.validated_data['stripe_token']
            )

            serializer.save(user=request.user, paid_amount=paid_amount)

            return Response([], status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
