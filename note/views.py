# views.py
import base64
import mimetypes

from django.core.files.base import ContentFile
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from note.models import Note
from note.forms import NoteForm


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'note_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

    def form_valid(self, form):
        form.instance.user = self.request.user

        # Vérifier si un fichier est téléchargé
        if 'file' in self.request.FILES:
            uploaded_file = self.request.FILES['file']
            mime_type, encoding = mimetypes.guess_type(uploaded_file.name)

            if mime_type:
                # Enregistrer le fichier avant d'obtenir son URL
                note = form.save(commit=False)
                note.file = uploaded_file
                note.save()

                # Vérifier le type MIME et assigner le type de note
                if mime_type.startswith('image/'):
                    note.note_type = 'image'
                    note.content = note.file.url
                elif mime_type.startswith('video/'):
                    note.note_type = 'video'
                    note.content = note.file.url
                elif mime_type == 'text/plain':
                    note.note_type = 'text'
                    note.content = uploaded_file.read().decode('utf-8')
                elif mime_type == 'application/pdf':
                    note.note_type = 'pdf'
                    note.content = note.file.url
                else:
                    # Lever une erreur si le type de fichier n'est pas autorisé
                    form.add_error('file', 'Type de fichier non supporté.')
                    return self.form_invalid(form)

                note.save()  # Enregistrer à nouveau pour mettre à jour les champs

            else:
                form.add_error('file', 'Impossible de déterminer le type de fichier.')
                return self.form_invalid(form)

        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user

        hidden_file = self.request.POST.get('hidden_file')
        if hidden_file:
            mime_type, encoding = mimetypes.guess_type(hidden_file)
            if mime_type:
                format, imgstr = hidden_file.split(';base64,')
                ext = format.split('/')[-1]
                file = ContentFile(base64.b64decode(imgstr), name=f"temp.{ext}")

                form.instance.file = file
                if mime_type.startswith('image/'):
                    form.instance.note_type = 'image'
                    form.instance.content = file.name
                elif mime_type.startswith('video/'):
                    form.instance.note_type = 'video'
                    form.instance.content = file.name
                elif mime_type == 'text/plain':
                    form.instance.note_type = 'text'
                    form.instance.content = file.read().decode('utf-8')
                elif mime_type == 'application/pdf':
                    form.instance.note_type = 'pdf'
                    form.instance.content = file.name
                else:
                    form.add_error('file', 'Type de fichier non supporté.')
                    return self.form_invalid(form)
            else:
                form.add_error('file', 'Impossible de déterminer le type de fichier.')
                return self.form_invalid(form)

        return super().form_valid(form)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
