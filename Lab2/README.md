# Fine-Tuning Whisper for Italian Speech Transcription 🗪
The objective of this project is the fine-tuning of the Whisper translation model, by OpenAI, achieving the ability to efficiently transcribe Italian speech. This work has been separated into three steps.
Our reference can be found in the blog post 👉 [Fine-Tune Whisper 🤗](https://huggingface.co/blog/fine-tune-whisper). To build meaningful interactive applications, a Gradio interface was employed. 
The project does not limit itself to fine-tuning Whisper: to exploit the full capabilities of the model, we have added three functionalities, with the ultimate goal of realizing a 
Speech-to-Speech 🗪 system:
- **Speech-to-Text**: naturally performed by the fine-tuned Whisper model.
- **Summarization**: allowing the transcribed text to be summarized for clarity.
- **Translation**: turning the original Italian transcription into English to make it understandable by additional users.
- **PDF Saving**: allowing users to save the translated text into PDF and directly download the obtained file.
- **Text-to-Speech**: exploiting the pdf transcription, make it possible to turn the English text into English speech, effectively providing a complete translation of the original input file.

Every operation was performed on Google Colab. This platform has the advantages of offering a GPU for fast training and a container environment for easily handling dependencies and installations. However, its resource limitations (timed computation unit usage, limited storage space) have influenced some particular choices that were made in building the system.

## Feature Pipeline 🔊
The training dataset was obtained from 👉 [Mozilla Foundation's Common Voice 11.0 Dataset 🤗](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0/viewer/it), selecting the 'it' subset. Since the training split consists of more than 130.000 samples of audio and text transcriptions, its entire storage on Google Colab environment, and subsequently in Google Drive storage, was not deemed feasible. Instead, to ensure a comprehensive view of the dataset, a split of around 10% of the training set was chosen, after shuffling the samples and selecting them at random.
Whisper's feature extractor was leveraged to pad/truncate audio inputs to make their length 30 seconds and turn them into log-Mel spectrogram images. This operation was needed to adapt the data to the transformer's structure, which includes a convolution layer. However, **this choice will reflect its consequences on the model performance**. The text was then tokenized and combined with the feature extractor.
The audio sample rate, compared to its original of 48 kHz, has been reduced to 16 kHz for better storage exploitation, assuming not too much information was lost. 
![Audio Feature Extraction](afe.png)
This preprocessing was concluded with a mapping operation to make all training samples in the wanted format. 
💾 For easy storage and retrieval, we have employed Google Drive. The drive was mounted and accessed to upload both training and testing sets, for an overall occupation of the total Cloud storage space.

## Training Pipeline 🏋️‍♂️


## Inference Pipeline 🎙️📝



![Example](image.png)
Supports Uploads and Real-Time webcam capturing!
