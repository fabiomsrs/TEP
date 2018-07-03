from rest_framework import permissions
from .models import Student, Professor

class IsNotAllowed(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):		
		return False

	def has_permission(self, request, view):		
		return False


class IsGradeOwner(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:												
			if Student.objects.filter(pk=self.kwargs['student_pk']):
				return True					
		return False

	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:												
			if Student.objects.filter(pk=self.kwargs['student_pk']):
				return True					
		return False


class IsProfessor(permissions.BasePermission):
	

	def has_object_permission(self, request, view, obj):		
		
		if Professor.objects.filter(username=request.user.username):
			return True
		else:
			return False

	def has_permission(self, request, view):		
		if Professor.objects.filter(username=request.user.username):
			return True
		else:
			return False
