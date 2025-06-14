from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def usuarios(request):
    user_list = [
        {"nome": "Gabriela", "matricula": "20231181110018", "idade": "17", "cidade": "São Paulo do Potengi"},
        {"nome": "César", "matricula": "20231181110020", "idade": "17", "cidade": "São Paulo do Potengi"},
        {"nome": "Beatriz", "matricula": "20231181110029", "idade": "16", "cidade": "São Paulo do Potengi"},
        {"nome": "Matheus", "matricula": "20231181110021", "idade": "17", "cidade": "São Paulo do Potengi"},
        {"nome": "Thierry", "matricula": "20231181110002", "idade": "17", "cidade": "Riachuelo"},
    ]

    context = {
        "usuarios": user_list
    }
    
    return render(request, "usuarios.html", context)
