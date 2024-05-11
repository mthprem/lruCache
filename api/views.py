from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from api.cache_service import LRUCache

# Dictionary to store collections
collections = {}


# /api/collections/ (param - name)
@api_view(['POST'])
def create_collection(request):
    collection_name = request.data.get('name')
    if not collection_name:
        return Response(
            {'error': f'Please provide collection_name'},
            status=status.HTTP_400_BAD_REQUEST
        )

    capacity = request.data.get('capacity', 10)  # Default capacity is 10 if not provided
    collections[collection_name] = LRUCache(capacity)
    return Response(
        {'message': f'Collection {collection_name} created with capacity {capacity}'},
        status=status.HTTP_200_OK
    )


# api/update_capacity/<collection_name>/ (param - capacity)
@api_view(['PUT'])
def update_capacity(request, collection_name):
    if collection_name not in collections:
        return Response(
            {'error': f'Collection {collection_name} not found'},
            status=status.HTTP_400_BAD_REQUEST
        )

    new_capacity = request.data['capacity']
    collections[collection_name].update_capacity(new_capacity)
    return Response(
        {'message': f'Capacity of collection {collection_name} updated to {new_capacity}'},
        status=status.HTTP_200_OK
    )


# api/collections/<collection_name>/data (param - key, value)
@api_view(['POST'])
def put_data(request, collection_name):
    key = request.data.get('key')
    value = request.data.get('value')

    if not key or not value:
        return Response(
            {'error': f'Please provide the params'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if collection_name not in collections:
        return Response(
            {'error': f'Collection {collection_name} not found'},
            status=status.HTTP_400_BAD_REQUEST
        )

    key = request.data['key']
    value = request.data['value']
    collections[collection_name].put(key, value)
    return Response(
        {'message': f'Data {value} stored with key {key} in collection {collection_name}'},
        status=status.HTTP_200_OK
    )


# api/collections/<collection_name>/data/key/ (param - Null)
@api_view(['GET'])
def get_data(request, collection_name, key):
    if collection_name not in collections:
        return Response(
            {'error': f'Collection {collection_name} not found'},
            status=status.HTTP_400_BAD_REQUEST
        )

    value = collections[collection_name].get(key)
    if value is None:
        return Response(
            {'error': f'Data not found for key {key} in collection {collection_name}'},
            status=status.HTTP_400_BAD_REQUEST
        )
    return Response({'data': value}, status=status.HTTP_200_OK)
