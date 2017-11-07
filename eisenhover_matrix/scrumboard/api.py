from rest_framework.generics import ListAPIView

from .serializers import TaskSerializer
from .models import Task


class TaskApi(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
