# farm_ai_fastapi.py  (fixed)
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import uvicorn, json, os

app = FastAPI(title="KrishiMitra (FastAPI)")

# CORS (allow frontend to talk to backend from any origin for demo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # fine for hackathon/demo; lock this down for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load small KB
KB_PATH = os.path.join(os.path.dirname(__file__), "kb.json")
with open(KB_PATH, "r", encoding="utf-8") as f:
    KB = json.load(f)

def simple_retrieve(q: str):
    ql = q.lower()
    hits = []
    for d in KB:
        # simple token check
        if any(tok in d["content"].lower() or tok in d["title"].lower() for tok in ql.split()):
            hits.append(d["content"])
    return hits[:3] if hits else [d["content"] for d in KB[:2]]

class Q(BaseModel):
    query: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/query")
async def query(q: Q):
    text = q.query.strip()
    if not text:
        return {"error": "empty query"}
    context = simple_retrieve(text)
    answer = "I looked into knowledge base:\n\n" + "\n\n".join(context) + "\n\nSuggestion: "
    if "blight" in text.lower() or "fungus" in text.lower():
        answer += "Remove infected leaves and use copper-based fungicide every 7-10 days."
    elif "water" in text.lower() or "irrig" in text.lower():
        answer += "Maintain consistent water levels as per crop stage; avoid water stress."
    else:
        answer += "See suggestions above. If unsure, contact local agri officer."
    return {"answer": answer, "retrieved": context}

@app.post("/image")
async def analyze_image(image: UploadFile = File(...)):
    contents = await image.read()
    tmp = "tmp_upload.jpg"
    with open(tmp, "wb") as f:
        f.write(contents)
    return {"answer": "Image received (demo). Add TF/OpenCV here.", "note": "Saved to " + tmp}

if __name__ == "__main__":
    uvicorn.run("farm_ai_fastapi:app", host="0.0.0.0", port=8000, reload=False)