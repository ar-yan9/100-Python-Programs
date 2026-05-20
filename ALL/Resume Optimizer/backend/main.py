from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pdfminer.high_level import extract_text
import shutil
import re
import os

app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ ATS Score Function
def calculate_ats_score(resume_text, job_desc):
    resume_words = set(re.findall(r'\b\w+\b', resume_text.lower()))
    job_words = set(re.findall(r'\b\w+\b', job_desc.lower()))

    matched = resume_words.intersection(job_words)
    missing = job_words - resume_words

    score = (len(matched) / len(job_words)) * 100 if job_words else 0

    return {
        "score": round(score, 2),
        "matched_keywords": list(matched)[:20],
        "missing_keywords": list(missing)[:20]
    }

# ✅ Resume Improver
def improve_resume(resume_text, missing_keywords):
    improved_text = resume_text

    if missing_keywords:
        improved_text += "\n\n--- Added Skills Section ---\n"
        improved_text += "Skills: " + ", ".join(missing_keywords)

    return improved_text

# ✅ Save Improved Resume
def save_improved_resume(text, filename="improved_resume.txt"):
    output_path = os.path.join(os.getcwd(), filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    return output_path

# ✅ Home Route
@app.get("/")
def home():
    return {"message": "Resume Optimizer Running 🚀"}

# ✅ Analyze + Improve Resume API
@app.post("/analyze/")
async def analyze_resume(file: UploadFile = File(...), job_desc: str = Form(...)):
    file_location = f"temp_{file.filename}"

    # Save uploaded file
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Extract text from PDF
        text = extract_text(file_location)
    except Exception as e:
        return {"error": str(e)}

    # ATS Analysis
    result = calculate_ats_score(text, job_desc)

    # Improve Resume
    improved_text = improve_resume(text, result["missing_keywords"])

    # Save file
    saved_file = save_improved_resume(improved_text)

    return {
        "filename": file.filename,
        "analysis": result,
        "improved_file_path": saved_file
    } 
