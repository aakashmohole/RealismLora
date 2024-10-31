from django.shortcuts import render
from django.http import HttpResponse
from . import utils 
from django.core.files.storage import FileSystemStorage

# Create your views here.
def landingpage(request):
    return render(request,'landingpage.html')

def home(request):
    return render(request,'home.html')

def aboutme(request):
    return render(request, 'aboutme.html')

def textmoderation(request):
    return render(request, 'textmoderation.html')

def imagemoderation(request):
    return render(request, 'imagemoderation.html')

def submit_data(request):
    if request.method == 'POST':
        UserText = request.POST.get('inputtext')
        processedText = utils.preprocess(UserText)
        
        classifiedText = utils.classify_text(processedText)
        text = ' '.join([text for text in classifiedText['text'] if text])
        predicted_cl = classifiedText['predicted_class']
        probabilites0 = f"{classifiedText['probabilities']['appropriate'] * 100:.0f}%"
        probabilites1 = f"{classifiedText['probabilities']['inappropriate'] * 100:.0f}%"

        
        context = {
            'classification': predicted_cl,
            'clean_text': classifiedText['text'],
            'probabilities_appropriate': probabilites0,
            'probabilities_inappropriate': probabilites1
        }
        
        return render(request, 'textmoderation.html', context)        

from PIL import Image
import io

def submit_image(request):
    if request.method == 'POST':
        input_image = request.FILES.get('inputimage')

        if not input_image:
            return render(request, 'imagemoderation.html', {'error': 'No file uploaded.'})

        if not input_image.name.endswith(('.png', '.jpg', '.jpeg')):
            return render(request, 'imagemoderation.html', {'error': 'Unsupported file type.'})

        try:
            # Open the image file using PIL
            image = Image.open(input_image)
            image = image.convert('RGB')  # Convert to RGB if needed

            # Save the uploaded image
            fs = FileSystemStorage()
            filename = fs.save(input_image.name, input_image)  # Save the image
            uploaded_image_url = fs.url(filename)  # Get 

            detectedtext = utils.classify_image(image)
            classifiedTextByImage = utils.classify_text(detectedtext)

            predicted_cl = classifiedTextByImage['predicted_class']
            probabilites0 = f"{classifiedTextByImage['probabilities']['appropriate'] * 100:.0f}%"
            probabilites1 = f"{classifiedTextByImage['probabilities']['inappropriate'] * 100:.0f}%"

            context = {
                'imageview' : uploaded_image_url,
                'classification': predicted_cl,
                'clean_text': classifiedTextByImage['text'],
                'probabilities_appropriate': probabilites0,
                'probabilities_inappropriate': probabilites1
            }
            
            return render(request, 'imagemoderation.html', context)

        except Exception as e:
            return render(request, 'imagemoderation.html', {'error': f'Error processing image: {e}'})
