from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import cv2
import numpy as np

def index(request):
    return render(request, 'face_recognition_app/index.html')

@csrf_exempt
def authenticate(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        np_img = np.fromstring(image.read(), np.uint8)
        img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
        #cv2-computer vision ,cv2.imread() uses read images ,cv2.imwrite()-write images to files
        # Dummy facial recognition logic (to be replaced with actual model)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        if len(faces) > 0:
            return JsonResponse({'status': 'success', 'message': 'Face detected!'})
        else:
            return JsonResponse({'status': 'failure', 'message': 'No face detected!'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request!'})
