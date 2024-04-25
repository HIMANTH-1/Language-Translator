import whisper

model = whisper.load_model("base")

transcription = model.transcribe("C://Users//dwith//OneDrive//Documents//Tesseract_txt extraction//Record.mp3")

print(transcription["text"])
