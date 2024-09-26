from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from.models import Evaluation
from.serializers import EvaluationSerializer

# Create your views here.
class EvaluationsListView(APIView):
    def get(self, request):
        evaluations = Evaluation.objects.all()
        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)
    
class EvaluationDetailView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        evaluation = get_object_or_404(Evaluation, pk=pk)
        evaluation.viewcount += 1
        evaluation.save(update_fields=["viewcount"])
        serializer = EvaluationSerializer(evaluation)
        return Response(serializer.data)