
// static/js/voiceRecognitionPlugin.js

class VoiceRecognitionPlugin {
    constructor(editor) {
        this.editor = editor;
    }

    init() {
        const editor = this.editor;

        editor.ui.componentFactory.add('voiceButton', locale => {
            const view = new editor.ui.view.button.ButtonView(locale);

            view.set({
                label: 'Voice Input',
                icon: '<svg class="feather feather-mic" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 1v11M18 10a6 6 0 0 1-12 0M19 22h-14M5 16v6m14-6v6"></path></svg>',
                tooltip: 'Start Voice Input'
            });

            let recognition;
            let isRecognizing = false;

            if ('webkitSpeechRecognition' in window) {
                recognition = new webkitSpeechRecognition();
                recognition.continuous = true;
                recognition.interimResults = true;
                recognition.lang = 'en-US';

                recognition.onstart = function() {
                    isRecognizing = true;
                    view.element.classList.add('active');
                };

                recognition.onend = function() {
                    isRecognizing = false;
                    view.element.classList.remove('active');
                };

                recognition.onresult = function(event) {
                    let transcript = '';
                    for (let i = event.resultIndex; i < event.results.length; i++) {
                        transcript += event.results[i][0].transcript;
                    }
                    editor.model.change(writer => {
                        const insertPosition = editor.model.document.selection.getFirstPosition();
                        writer.insertText(transcript, insertPosition);
                    });
                };

                view.on('execute', () => {
                    if (isRecognizing) {
                        recognition.stop();
                    } else {
                        recognition.start();
                    }
                });
            } else {
                view.isEnabled = false;
                view.label = 'Voice Input Not Supported';
            }

            return view;
        });
    }
}

// Exportez la classe pour l'utiliser avec CKEditor
export default VoiceRecognitionPlugin;
