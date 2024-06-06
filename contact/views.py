import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail
from dotenv import load_dotenv

load_dotenv()


class ContactView(TemplateView):
    pass


class ContactUs(View):
    template_name = 'contact/contact-form.html'

    # 465 (SSL)/ 587 (TTLS)
    def create_mail(self):
        # Définir les informations de l'email
        sender_email = "p-garcia@laposte.net"
        sender_email = "admin@xendev.fr"
        receiver_email = "patgarcia66240@gmail.com"

        password = "Garcia66240!"
        subject = "Test Email"
        body = "Ceci est un test e-mail avec SSL pour vérifier l'envoie de message."

        # Créer le message MIME
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        host_server = "smtp.laposte.net"
        host_server = "node109-eu.n0c.com"
        # Attacher le corps du message
        message.attach(MIMEText(body, "plain"))

        # Créer le contexte SSL
        context = ssl.create_default_context()

        # Envoyer l'email
        with smtplib.SMTP_SSL(host_server, 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            self.create_mail()
            return render(request, 'contact/confirm-send.html')  # Remplacez par l'URL de redirection appropriée
        return render(request, self.template_name, {'form': form})
