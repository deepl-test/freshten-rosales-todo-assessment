from rest_framework import generics, status, filters
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['due_date', 'created_at', 'completed']
    ordering = ['-due_date']  # Default ordering
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Ensure we're ordering by the actual datetime field
        ordering = self.request.query_params.get('ordering', None)
        if ordering:
            if ordering.endswith('due_date'):
                return queryset.order_by(ordering)
        return queryset


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'status': status.HTTP_201_CREATED,
            'message': 'Task created successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Task retrieved successfully',
            'data': serializer.data
        })

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Task updated successfully',
            'data': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'status': status.HTTP_204_NO_CONTENT,
            'message': 'Task deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)