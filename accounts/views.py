from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from pypaystack2 import Paystack
import uuid
import requests
from django.http import JsonResponse
import logging
import re
from datetime import datetime
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from django.conf import settings




logger = logging.getLogger(__name__)

def home(request):
    video_url = settings.MEDIA_URL + 'videos/Acage_6_Advert.mp4'
    video_url2 = settings.MEDIA_URL + 'videos/Acage_6_Social_Media.mp4'
    return render(request, 'index.html',{
        'video': video_url,
        'video2': video_url2
        })

