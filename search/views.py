# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated

# Models
from users.models import User

# Serializers
from search.serializers import CurriculumSerializer

# Permissions
from users.permissions import IsRecruiterUser

from rest_framework.filters import SearchFilter


class SearchViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    filter_backends = (SearchFilter,)
    queryset = User.objects.filter(is_active=True, is_recruiter=False)
    serializer_class = CurriculumSerializer
    search_fields = (
        'extract', 
        'city', 
        'country', 
        'experience__company', 
        'experience__description', 
        'education__title', 
        'extra_education__description',
        'projects__description',
    )