from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import os
import PyPDF2

@api_view(['GET', 'POST'])
@csrf_exempt
def summarize_text(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('pdf')
        if uploaded_file:
            # content = uploaded_file.read()
            # print(uploaded_file)
            # text = pdf_to_text(content)
            # Perform text summarization logic here
            summarized_text = "This is the summarized pdf."
            return JsonResponse({'summarized_text': summarized_text})
    elif request.method == 'GET':
        uploaded_file = request.FILES.get('pdf')
        if uploaded_file:
            content = uploaded_file.read()
            # print(request.text())
            # Perform text simplification logic here
        simplified_text = "This is the simplified text."
        return JsonResponse({'summarized_text': simplified_text})
    return JsonResponse({'error': 'Invalid request'})

@api_view(['GET', 'POST'])
@csrf_exempt
def simplify_text(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('pdf')
        if uploaded_file:
            content = uploaded_file.read()
            # Perform text simplification logic here
            simplified_text = "This is the simplified text."
            return JsonResponse({'simplified_text': simplified_text})
    return JsonResponse({'error': 'Invalid request'})


def pdf_to_text(pdf_file):
    # Open the PDF file in binary mode
    with open(pdf_file, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store the extracted text
        text = ""

        # Iterate through each page of the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Get a specific page
            page = pdf_reader.pages[page_num]

            # Extract text from the page
            page_text = page.extract_text()

            # Append the page's text to the overall text
            text += page_text

    return text