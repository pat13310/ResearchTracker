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
        uploaded_file = self.request.FILES.get('file')

        if uploaded_file:
            mime_type, encoding = mimetypes.guess_type(uploaded_file.name)
            if mime_type:
                self.handle_file_upload(form, uploaded_file, mime_type)
            else:
                form.add_error('file', 'Impossible de déterminer le type de fichier.')
                return self.form_invalid(form)

        return super().form_valid(form)

    def handle_file_upload(self, form, uploaded_file, mime_type):
        note = form.save(commit=False)
        note.file = uploaded_file
        note.save()
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
            form.add_error('file', 'Type de fichier non supporté.')
            return self.form_invalid(form)
        note.save()


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        uploaded_file = self.request.FILES.get('file')

        if uploaded_file:
            mime_type, encoding = mimetypes.guess_type(uploaded_file.name)
            if mime_type:
                self.handle_file_upload(form, uploaded_file, mime_type)
            else:
                form.add_error('file', 'Impossible de déterminer le type de fichier.')
                return self.form_invalid(form)

        return super().form_valid(form)

    def handle_file_upload(self, form, uploaded_file, mime_type):
        note = form.save(commit=False)
        note.file = uploaded_file
        note.save()
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
            form.add_error('file', 'Type de fichier non supporté.')
            return self.form_invalid(form)
        note.save()


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
