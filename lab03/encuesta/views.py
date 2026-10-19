from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from .models import Pregunta


def index(request):
    ultimas_preguntas = Pregunta.objects.order_by("-pub_date")[:5]

    contexto = {
        "ultimas_preguntas": ultimas_preguntas
    }

    return render(request, "encuesta/index.html", contexto)

def detalle(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)

    contexto = {
        "pregunta": pregunta
    }

    return render(request, "encuesta/detalle.html", contexto)

def votar(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)

    if request.method != "POST":
        return HttpResponseRedirect(reverse("detalle", args=(pregunta.id,)))

    opcion_id = request.POST.get("opcion")

    opcion = pregunta.opcion_set.filter(pk=opcion_id).first()

    if opcion is None:
        return HttpResponseRedirect(reverse("detalle", args=(pregunta.id,)))

    opcion.votos += 1
    opcion.save()

    return HttpResponseRedirect(reverse("resultados", args=(pregunta.id,)))

def resultados(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)

    contexto = {
        "pregunta": pregunta
    }

    return render(request, "encuesta/resultados.html", contexto)