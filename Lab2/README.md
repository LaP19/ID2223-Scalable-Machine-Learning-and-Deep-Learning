# Fine-Tining Whisper for Italian Speech Transcription
The objective of this project is the fine-tuning of the Whisper translation model, by OpenAI, achieving the ability to efficiently transcribe Italian speech. This work has been separated into three steps.
Our reference can be found in the blogpost 👉 [Fine-Tune Whisper 🤗](https://huggingface.co/blog/fine-tune-whisper). To build meaningful interactive applications, a Gradio interface was employed. 
The project does not limit itself to fine-tuning Whisper: in order to exploit the full capabilities of the model, we have added three functionalities, with the ultimate goal of realizing a 
Speech-to-Speech system:
- **Transcription**: naturally performed by the fine-tuned Whisper model.
- **Summarization**: allowing the transcribed text to be summarized for clarity.
- **Translation**: turning the original Italian transcription into English to make it understandable by additional users.
- **PDF Saving**: allowing users to save the translated text into PDF and directly download the obtained file.
- **Text-to-Speech**: exploiting the pdf transcription, make it possible to turn the English text into English speech, effectively providing a complete translation of the original input file.

## Feature Pipeline 


![Example](image.png)
Supports Uploads and Real-Time webcam capturing!
