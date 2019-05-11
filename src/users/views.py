from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from customers.models import Client
from datetime import timedelta, datetime

def hashes(times=50):
    print(times * "-")


class UserList(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        hashes()
        print("[GET ALL USERS] ", request.get_host())
        hashes()

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        hashes()
        print("[CREATE USER] ", request.get_host())
        hashes()

        data = request.data
        print(request.data)

        new_user = User.objects.create(**request.data)

        print(new_user)
        return Response({
            "status": 200,
            "message": "Successfully created user",
            "data": UserSerializer(new_user).data
        })


class UserDetail(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, pk, format=None):
        """
        Return a list of all users.
        """
        hashes()
        print("[GET SINGLE USER] ", request.get_host())
        hashes()

        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        """
        Return a list of all users.
        """
        hashes()
        print("[UPDATE USER] ", request.get_host())
        hashes()

        data = request.data 
        print(data)
        user = User.objects.get(pk=pk)
        user.name = data["name"]
        user.username = data["username"]
        user.save()
        serializer = UserSerializer(user)
        return Response({
            "data": serializer.data, **{"message": "Successfully updated user", "status": 200}
        })


def index(request):
    print("-" * 40)
    print(request.META)
    # {
    #     'TERM_PROGRAM': 'Apple_Terminal', 'SHELL': '/usr/local/bin/zsh', 
    #     'TERM': 'xterm-256color', 'TMPDIR': '/var/folders/_h/d17s0sg11q74f68sxqnvg1nm0000gn/T/', 
    #     'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.BhK0SraDmZ/Render', 
    #     'TERM_PROGRAM_VERSION': '421.1.1', 'TERM_SESSION_ID': '1A5D8461-35FA-45EC-AE8C-F4BC605375B5', 
    #     'USER': 'hygull', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.4JkDlgnD7v/Listeners', 
    #     'PATH': '/Users/hygull/Desktop/try_django_tenant_schemas/venv3.6.7.26apr/bin:/Users/hygull/bin:/usr/local/bin:/Users/hygull/Library/Python/3.6/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin', 'PWD': '/Users/hygull/Desktop/try_django_tenant_schemas/src', 
    #     'XPC_FLAGS': '0x0', 'XPC_SERVICE_NAME': '0', 'SHLVL': '1', 'HOME': '/Users/hygull', 
    #     'LOGNAME': 'hygull', 'LC_CTYPE': 'UTF-8', 'SECURITYSESSIONID': '186a7', 
    #     'OLDPWD': '/Users/hygull/Desktop/try_django_tenant_schemas', 
    #     'ZSH': '/Users/hygull/.oh-my-zsh', 'PAGER': 'less', 'LESS': '-R', 
    #     'LSCOLORS': 'Gxfxcxdxbxegedabagacad', 'VIRTUAL_ENV': '/Users/hygull/Desktop/try_django_tenant_schemas/venv3.6.7.26apr', 
    #     'PS1': '(venv3.6.7.26apr) ${ret_status} %{$fg[cyan]%}%c%{$reset_color%} $(git_prompt_info)', 
    #     '_': '/Users/hygull/Desktop/try_django_tenant_schemas/venv3.6.7.26apr/bin/python', 
    #     '__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0xF', 'DJANGO_SETTINGS_MODULE': 'proj.settings', 'TZ': 'UTC', 'RUN_MAIN': 'true', 
    #     'SERVER_NAME': '1.0.0.127.in-addr.arpa', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '9001', 
    #     'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 
    #     'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/', 'QUERY_STRING': '', 
    #     'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': 'my-domain.com:9001', 
    #     'HTTP_CONNECTION': 'keep-alive', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 
    #     'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36', 
    #     'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 
    #     'HTTP_PURPOSE': 'prefetch', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate', 
    #     'HTTP_ACCEPT_LANGUAGE': 'en-GB,en-US;q=0.9,en;q=0.8,fr;q=0.7,bn;q=0.6', 
    #     'HTTP_COOKIE': 'csrftoken=uGSspU2vSuAjKIAWJL98EpmmXIjsiHOo5KV1IJdFdVL5rfVsF82Q69esnc8yYALH; sessionid=e4hvc3195c204g5z4e2d5x40furp1ghw', 
    #     'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x103595eb8>, 
    #     'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 
    #     'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 
    #     'wsgi.multithread': True, 'wsgi.multiprocess': False, 
    #     'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>, 
    #     'CSRF_COOKIE': 'uGSspU2vSuAjKIAWJL98EpmmXIjsiHOo5KV1IJdFdVL5rfVsF82Q69esnc8yYALH'
    # }
    print("-" * 40)
    host =  request.get_host()
    if host == "my-domain.com:9001":
        return render(request, "users/login.html", {})
    else:        
        users = User.objects.all()
        return render(request, "users/index.html", {"users": users})


class UserLogin(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        response = {}
        status = 400
        
        clients = Client.objects.filter(schema_name=request.data.get("tenant"))

        try:
            if clients.exists():
                client = clients.first()
                print(client)
                response["data"] = {
                    "scheme": "http", # https/http
                    "tenant": client.schema_name,
                    "domain": "my-domain",
                    "port": 9001,
                    "extension": "com"
                }
                status = 200
                message = "Successfully logged in"  
            else:
                status = 400
                message = "User does not exist"          
        except Exception as error:
            response["message"] = str(error)

        response["status"] = status
        response["message"] = message

        return Response(response)


class CreateClient(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "users/signup.html", {})

    def post(self, request, *args, **kwargs):
        response = {}
        data = request.data
        print('Create a tenant => ', data)
        password = data.get("password", '')
        schema_name = data.get("schema_name", '') # Tenant name
        name = data.get("name", '')


        domain_url = schema_name + ".my-domain.com"
        status = 400
        if all([password, schema_name, name]):
            try:
                clients = Client.objects.filter(schema_name=schema_name, domain_url=domain_url)
                
                if client.exists():
                    message = "Entered tenant already exists"
                else:
                    now = datetime.now()
                    paid_until = (now + timedelat(days=30)).date()
                    client = Client.objects.create(
                        schema_name=schema_name, domain_url=domain_url,
                        paid_until=paid_until, on_trial=True
                    )
                    status = 200
                    message = "Successfully created the tenant"
            except Exception as error:
                message = str(error)
        else:
            message = "Please check if you are missing arn_user_id, appln_id, password, schema_name, name"

        response["message"] = message
        response["status"] = status
        return Response(response)

