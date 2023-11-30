from django.http import HttpResponse

from django.template import Template, Context

import pyrebase

config = {
    "apiKey": "AIzaSyAvKTpBpgrvFUZo-rIZytmYuQFas2J8QbQ",
    "authDomain": "felizvulnes.firebaseapp.com",
    "databaseURL": "https://felizvulnes-default-rtdb.firebaseio.com",
    "projectId": "felizvulnes",
    "storageBucket": "felizvulnes.appspot.com",
    "messagingSenderId": "278672158781",
    "appId": "1:278672158781:web:06a227431577a509b6ba54",
    # measurementId: "G-E56PH8DC2N"
}

fbase = pyrebase.initialize_app(config)
auth = fbase.auth()
bd = fbase.database()

# Página Inicio
def inicio(request):

    doc = open('FelizVulnes/template/inicio.html')
    plt = Template(doc.read())
    doc.close()

    ctx = Context()
    documento = plt.render(ctx)

    return HttpResponse(documento)



def login(request):

    doc = open('FelizVulnes/template/login.html')
    plt = Template(doc.read())
    doc.close()

    ctx = Context()
    documento = plt.render(ctx)

    return HttpResponse(documento)