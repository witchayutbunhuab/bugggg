import io
import sys
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas

# Create your views here.
def home(request):
    response = HttpResponse('Welcome to Thailand')
    return response

def students(request):
    context = {}
    context['object_list'] = Student.objects.all()[:10]
    context['object_list'] = Student.objects.filter(name='jack Daniels')
    return render(request, 'myapp/students.html', context)

def info(request):
    r = HttpResponse(sys.version)
    return r

def data(request):
    d = {
        '67000000': { 
            'first_name': 'Anna',
            'last_name': 'Aaaaa'
        },
        '67000001': {
            'first_name': 'Benedict',
            'last_name': 'Bbbbbbb'
        }
    }
    return JsonResponse(d)

def pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "I am a PDF.")
    
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")