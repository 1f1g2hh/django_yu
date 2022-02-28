from django.shortcuts import render
from googletrans import Translator
import googletrans


# Create your views here.

def index(request):
    context = {
        "ndict":googletrans.LANGUAGES
    }
    if request.method == "POST":
        bf = request.POST.get("bf").strip()
        if bf:
            fr = request.POST.get("fr")
            to = request.POST.get("to")
            translator = Translator()
            trans1 = translator.translate(bf, src=fr, dest=to)
            context.update({
                "af": trans1.text,
                "bf": bf,
                "fr": fr,
                "to": to,
            }) 
    return render(request,"trans/index.html",context)


