from fastapi import FastAPI, File, UploadFile
import whisper
import tempfile

app = FastAPI()
model = whisper.load_model("base")

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    result = model.transcribe(tmp_path)
    return {"text": result["text"]}
