from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Path, Student
from .serializers import PathSerializer, StudentSerializer


@api_view(['GET'])
def list_all_paths(request):
    all_paths = Path.objects.all()
    serializer = PathSerializer(all_paths, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_all_students(request):
    all_students = Student.objects.all()
    serializer = StudentSerializer(all_students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_new_path(request):
    sended_data = PathSerializer(data=request.data)
    if sended_data.is_valid():
        sended_data.save()
        message = {"detail": "Path başarılı bir şekilde oluşturuldu"}
        return Response(message, status=status.HTTP_201_CREATED)

    return Response(sended_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_new_student(request):
    sended_data = StudentSerializer(data=request.data)
    if sended_data.is_valid():
        sended_data.save()
        message = {"detail": "Öğrenci başarılı bir şekilde oluşturuldu"}
        return Response(message, status=status.HTTP_201_CREATED)

    return Response(sended_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_one_path(request, pk):
    one_path = get_object_or_404(Path, id=pk)
    serializer = PathSerializer(one_path)
    return Response(serializer.data)


@api_view(['GET'])
def get_one_student(request, pk):
    one_student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(one_student)
    return Response(serializer.data)


@api_view(['PUT'])
def update_one_path(request, pk):
    one_path = get_object_or_404(Path, id=pk)
    serializer = PathSerializer(instance=one_path, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {"detail": "Path başarılı bir şekilde güncellendi"}
        return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_one_student(request, pk):
    one_student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=one_student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {"detail": "Öğrenci başarılı bir şekilde güncellendi"}
        return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_one_path(request, pk):
    one_path = get_object_or_404(Path, id=pk)
    one_path.delete()
    message = {"detail": "Path başarılı bir şekilde silindi"}
    return Response(message)


@api_view(['DELETE'])
def delete_one_student(request, pk):
    one_student = get_object_or_404(Student, id=pk)
    one_student.delete()
    message = {"detail": "Öğrenci başarılı bir şekilde silindi"}
    return Response(message)


@api_view(['PATCH'])
def patch_path(request, pk):
    one_path = get_object_or_404(Path, id=pk)
    serializer = PathSerializer(
        instance=one_path, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        message = {"detail": "Path başarılı bir şekilde güncellendi"}
        return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def patch_student(request, pk):
    one_student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(
        instance=one_student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        message = {"detail": "Öğrenci başarılı bir şekilde güncellendi"}
        return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
