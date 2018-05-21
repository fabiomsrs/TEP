from rest_framework import generics


class ViewList(generics.ListCreateAPIView):
	pass
	

class ViewDetail(generics.RetrieveUpdateDestroyAPIView):
	pass
	
