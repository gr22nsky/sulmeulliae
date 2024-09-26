from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from.models import Evaluation, Review
from.serializers import EvaluationSerializer, ReviewSerializer

# Create your views here.
class EvaluationListView(APIView):
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
        images = evaluation.images.all()
        serializer = EvaluationSerializer(evaluation)
        return Response(serializer.data)
    
class ReviewListView(APIView):
    
    def get_object(self, pk):
        return get_object_or_404(Evaluation, pk=pk)
    
    def get(self, request, pk):
        evaluation = self.get_object(pk)
        reviews = evaluation.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk):
        evaluation = self.get_object(pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(evaluation=evaluation, author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class ReviewDetailView(APIView):
    
    def get_object(self, pk):
        return get_object_or_404(Review, pk=pk)
    
    def put(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response(status=204)
