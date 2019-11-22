from django.shortcuts import render

from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy # new
from .form import PostForm
from .models import Post
from django.shortcuts import redirect
from .models import Post
from django.views import View
from django.shortcuts import get_object_or_404
##DRF
from rest_framework import viewsets
from rest_framework.response import Response
from .PostSerializer import PostSerializer,PostCreateSerializer
from django.contrib.auth import authenticate

##auth
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class HomePageView(ListView):
    model = Post
    template_name = 'post/index.html'

class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'post/new_post.html'
    success_url = reverse_lazy('home')


def addlike(request,pk):
    if request.method == 'GET':
        print(pk)
        obj  = Post.objects.get(pk=pk)
        obj.likes+=1
        obj.save()
        
    else:
        pass
        # Code block for GET request (will also match PUT, HEAD, DELETE, etc)    
    return redirect('/home')    

class PostPlus(View):
    
    template_name = 'post/postplus.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'message': 'new post'})

    def post(self, request, *args, **kwargs):
        post = PostForm(request.POST, request.FILES)  
        if post.is_valid():  
            obj = post.save(commit=False)
            obj.likes = 55
            obj.save()
        
        return render(request, self.template_name, {'message': 'new post added'})    

####DRF

class PostViewSet(viewsets.ViewSet):
    

    
    def get_permissions(self):
    
        if self.action == 'list' or self.action == 'password_reset':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)  

    def create(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            
            serializer.save()
        return Response(serializer.data)  

    def partial_update(self, request, pk=None):
        instance  = Post.objects.get(pk = pk)
        serializer = PostCreateSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            #.... Your code ....
            serializer.save()
        return Response(serializer.data)  

    def update(self, request, pk=None):
        instance  = Post.objects.get(pk = pk)
        serializer = PostCreateSerializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            #.... Your code ....
            serializer.save()
        return Response(serializer.data)   

    def destroy(self, request, pk=None):
        instance  = Post.objects.get(pk = pk)
        instance.delete()
        return Response("deleed")  


@api_view(["POST"])
#@permission_classes([IsAuthenticated])
#@authentication_classes([SessionAuthentication, BasicAuthentication])
def login_rest(request):
    username = request.data.get("username")
    password = request.data.get("password")
    
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    
    
    data = {
            'token': token.key,
            'username': user.username,
                        
                    }
    
    return Response(data)          