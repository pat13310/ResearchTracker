const editor_container = document.querySelector(".ck-editor-container");
const panel_audio = document.createElement("div");
const button_audio = document.createElement("button");


function VoiceRecognition() {
    let recognition;
    let isRecognizing = false;
    const editor = document.querySelector(".ck-content");
    let editorInstance = editor.ckeditorInstance;

    if ('webkitSpeechRecognition' in window) {
        initButton(editor_container);
        recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.MaxAlternatives = 1;
        recognition.lang = 'fr-FR';  // Changez la langue si nécessaire

        recognition.onstart = function () {
            isRecognizing = true;
            button_audio.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-mic"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>';
        };

        recognition.onend = function () {
            isRecognizing = false;
            button_audio.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-mic-off"><line x1="1" y1="1" x2="23" y2="23"></line><path d="M9 9v3a3 3 0 0 0 5.12 2.12M15 9.34V4a3 3 0 0 0-5.94-.6"></path><path d="M17 16.95A7 7 0 0 1 5 12v-2m14 0v2a7 7 0 0 1-.11 1.23"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>'
        };

        recognition.onresult = (e) => {
            let transcript = '';
            transcript = e.results[0][0].transcript + " ";
            console.log(transcript);
            editorInstance.model.change(writer => {
                const insertPosition = editorInstance.model.document.selection.getFirstPosition();
                writer.insertText(transcript, insertPosition);
            });
            isRecognizing = true;
            button_audio.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-mic"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>';


        };

        recognition.onerror = function (event) {
            console.error('Speech recognition error', event);
        };

        button_audio.addEventListener('click', () => {
            event.preventDefault();
            event.stopPropagation();

            //isRecognizing = !isRecognizing;
            if (!isRecognizing) {
                if (recognition) {
                    recognition.start();
                }
            } else {
                if (recognition) {
                    recognition.stop();
                }
            }
        });


    } else {
        console.warn('Voice Recognition non supporté');
        // Vous pouvez désactiver le bouton ou montrer un message à l'utilisateur
    }
}

// Exporter la fonction pour l'utiliser dans d'autres fichiers
//export default VoiceRecognition;


function initButton(parent) {
    let toggle = false;
    panel_audio.classList.add("w-100", "py-2");
    button_audio.classList = "mt-2 mb-2 p-2 text-gray-400 bg-gray-50 border-2 rounded-full border-gray-300 hover:text-violet-500 hover:border-violet-500 hover:border-2";
    button_audio.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-mic-off"><line x1="1" y1="1" x2="23" y2="23"></line><path d="M9 9v3a3 3 0 0 0 5.12 2.12M15 9.34V4a3 3 0 0 0-5.94-.6"></path><path d="M17 16.95A7 7 0 0 1 5 12v-2m14 0v2a7 7 0 0 1-.11 1.23"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>'

    panel_audio.appendChild(button_audio);
    parent.appendChild(panel_audio);
}