from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
import sys
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_paginated_qs(queryset, request, limit=10):
    paginator = LimitOffsetPagination()
    paginator.max_limit = 50
    paginator.default_limit = limit
    paginator.offset = 0

    pg_qs = paginator.paginate_queryset(
        queryset,
        request
    )

    next_link = paginator.get_next_link()
    prev_link = paginator.get_previous_link()
    if next_link:
        next_link = next_link.split('?')[1]
    if prev_link:
        prev_link = prev_link.split('?')[1]

    data = {
        'qs': pg_qs,
        'limit': paginator.limit,
        'offset': paginator.offset,
        'count': paginator.count,
        'next': next_link,
        'prev': prev_link,
    }

    # print(json.dumps(data))

    return data


def get_paginated(queryset, request, to_dict, limit=10):
    paginator = LimitOffsetPagination()
    paginator.max_limit = 50
    paginator.default_limit = limit
    paginator.offset = 0

    obj_list = paginator.paginate_queryset(
        queryset,
        request
    )

    results = to_dict(obj_list)

    next_link = paginator.get_next_link()
    prev_link = paginator.get_previous_link()
    if next_link:
        next_link = next_link.split('?')[1]
    if prev_link:
        prev_link = prev_link.split('?')[1]

    data = {
        'results': results,
        'limit': paginator.limit,
        'offset': paginator.offset,
        'count': paginator.count,
        'next': next_link,
        'prev': prev_link,
    }

    # print(json.dumps(data))

    return data


CACHE_TIME = 3600
CACHE_ENABLE = False


def get_cache_data(key):
    if CACHE_ENABLE:
        return cache.get(key.replace(" ", ""))
    else:
        return None


def set_cache_data(key, value):
    cache.set(key.replace(" ", ""), value, CACHE_TIME)


def clear_cache():
    cache.clear()




#
# @api_view(['POST'])
# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['file']:
#         raw_image = request.FILES['file']
#
#         im = Image.open(raw_image)
#         im = im.convert('RGB')
#         output = BytesIO()
#
#         # Resize/modify the media
#         # im = im.resize((300, 100))
#         im.thumbnail((800, 800), Image.ANTIALIAS)
#         # after modifications, save it to the output
#         im.save(output, format='JPEG', quality=90)
#         output.seek(0)
#
#         # change the imagefield value to be the newley modifed media value
#         raw_image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % raw_image.name.split('.')[0], 'media/jpeg',
#                                          sys.getsizeof(output), None)
#
#         AWS_ACCESS_KEY_ID = 'AKIAXWX2LQE6XYTZIPY6'
#         AWS_SECRET_ACCESS_KEY = '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'
#         AWS_STORAGE_BUCKET_NAME = 'hueys-list'
#
#         conn = boto.s3.connect_to_region('ap-southeast-2',
#                                          aws_access_key_id=AWS_ACCESS_KEY_ID,
#                                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
#                                          is_secure=True,  # uncomment if you are not using ssl
#                                          calling_format=boto.s3.connection.OrdinaryCallingFormat(),
#                                          )
#
#         bucket = conn.get_bucket(AWS_STORAGE_BUCKET_NAME)
#
#         # go through each version of the file
#
#         # create a key to keep track of our file in the storage
#
#         k = Key(bucket)
#         k.key = get_random_string(length=10) + raw_image.name.replace(' ', '')
#
#         k.set_contents_from_file(raw_image)
#
#         # we need to make it public so it can be accessed publicly
#
#         # using a URL like http://s3.amazonaws.com/bucket_name/key
#
#         k.make_public()
#         url = 'https://hueys-list.s3-ap-southeast-2.amazonaws.com/' + k.key
#         return Response({'url': str(url)},
#                         status=status.HTTP_201_CREATED)
