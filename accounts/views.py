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
import os




logger = logging.getLogger(__name__)

def home(request):
    video_url = f"{settings.MEDIA_URL}videos/Acage_Advert.mp4"
    video_url2 = f"{settings.MEDIA_URL}videos/Acage_Social_Media.mp4"
    print(f"Video 1 URL: {video_url}")  # Debug: should print /media/videos/Acage_6_Advert.mp4
    print(f"Video 2 URL: {video_url2}")  # Debug: should print /media/videos/Acage_6_Social_Media.mp4
    return render(request, 'index.html', {
        'video': video_url,
        'video2': video_url2
    })
