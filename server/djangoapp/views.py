# Required imports
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# -----------------------------
# LOGIN VIEW
# -----------------------------
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        response = {"userName": username, "status": "Authenticated"}
    else:
        response = {"userName": username, "error": "Invalid Credentials"}

    return JsonResponse(response)


# -----------------------------
# LOGOUT VIEW
# -----------------------------
@csrf_exempt
def logout_user(request):
    logout(request)  # Terminate user session
    response = {"userName": ""}
    return JsonResponse(response)


# -----------------------------
# REGISTRATION VIEW
# -----------------------------
@csrf_exempt
def registration(request):
    data = json.loads(request.body)

    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']

    username_exist = False

    try:
        User.objects.get(username=username)
        username_exist = True
    except User.DoesNotExist:
        logger.debug(f"{username} is a new user")

    if not username_exist:
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email
        )

        login(request, user)
        response = {"userName": username, "status": "Authenticated"}
    else:
        response = {"userName": username, "error": "Already Registered"}

    return JsonResponse(response)