const editor_container = document.querySelector(".ck-editor-container");
const panel_audio = document.createElement("div");
const button_audio = document.createElement("button");
const button_tts = document.createElement("button");
panel_audio.classList.add("w-100", "py-2");


function VoiceRecognition() {
    let recognition;
    let isRecognizing = false;
    const editor = document.querySelector(".ck-content");
    let editorInstance = editor.ckeditorInstance;

    if ('webkitSpeechRecognition' in window) {
        initButtonRecognition(editor_container);
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


function initButtonRecognition(parent) {
    let toggle = false;
    button_audio.classList = "mr-2 mt-2 mb-2 p-2 text-gray-400 bg-gray-50 border-2 rounded-full border-gray-300 hover:text-violet-500 hover:border-violet-500 hover:border-2";
    button_audio.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-mic-off"><line x1="1" y1="1" x2="23" y2="23"></line><path d="M9 9v3a3 3 0 0 0 5.12 2.12M15 9.34V4a3 3 0 0 0-5.94-.6"></path><path d="M17 16.95A7 7 0 0 1 5 12v-2m14 0v2a7 7 0 0 1-.11 1.23"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>'

    panel_audio.appendChild(button_audio);
    parent.appendChild(panel_audio);
}

function initButtonTTS(parent) {
    let toggle = false;
    button_tts.classList = "mr-2 mt-2 mb-2 p-2 text-gray-400 bg-gray-50 border-2 rounded-full border-gray-300 hover:text-violet-500 hover:border-violet-500 hover:border-2";
    //button_tts.innerHTML ='<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"  className="feather feather-volume-2">  <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>  <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path> </svg>'
    button_tts.innerHTML = '<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"feather feather-volume-x\"><polygon points=\"11 5 6 9 2 9 2 15 6 15 11 19 11 5\"></polygon><line x1=\"23\" y1=\"9\" x2=\"17\" y2=\"15\"></line><line x1=\"17\" y1=\"9\" x2=\"23\" y2=\"15\"></line></svg>'
    panel_audio.appendChild(button_tts);
    parent.appendChild(panel_audio);
}


function TTS_Voice() {
    let msg;
    const editor = document.querySelector(".ck-content");
    let editorInstance = editor.ckeditorInstance;
    let editorContent = editorInstance.getData();
    let tempDiv = document.createElement("div");
    // Insérez le contenu HTML dans l'élément temporaire
    tempDiv.innerHTML = editorContent;
    // Utilisez textContent pour obtenir le texte brut
    let text = tempDiv.textContent || tempDiv.innerText || "";
    //let editorContent = editorInstance.model.document.getRoot().getChild(0).getText();
    button_tts.addEventListener('click', () => {
        event.preventDefault();
        event.stopPropagation();
        if (!msg) return;
        window.speechSynthesis.speak(msg);
        button_tts.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"  className="feather feather-volume-2">  <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>  <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path> </svg>'
    })
    //button_tts.innerHTML ='<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"feather feather-volume-x\"><polygon points=\"11 5 6 9 2 9 2 15 6 15 11 19 11 5\"></polygon><line x1=\"23\" y1=\"9\" x2=\"17\" y2=\"15\"></line><line x1=\"17\" y1=\"9\" x2=\"23\" y2=\"15\"></line></svg>'
    if ('speechSynthesis' in window) {
        initButtonTTS(editor_container);

        msg = new SpeechSynthesisUtterance();
        msg.onend = function (event) {
            button_tts.innerHTML = '<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"feather feather-volume-x\"><polygon points=\"11 5 6 9 2 9 2 15 6 15 11 19 11 5\"></polygon><line x1=\"23\" y1=\"9\" x2=\"17\" y2=\"15\"></line><line x1=\"17\" y1=\"9\" x2=\"23\" y2=\"15\"></line></svg>'
        };
        msg.text = text;
        msg.voice = speechSynthesis.getVoices()[2];
        msg.rate = 1;
        msg.pitch = 1;
        msg.volume = 1;

    } else {
        console.log("Ce navigateur ne supporte pas le TTS");
    }

}

function hideCounter() {
    const wordCountElement = document.querySelector('.ck.ck-word-count');
    if (wordCountElement) {
        wordCountElement.style.display = 'none';
    }
}