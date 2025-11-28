from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Security Prompt Sentinel", version="0.1.0")

class CheckRequest(BaseModel):
    text: str

@app.get("/healthz")
def health():
    return {"ok": True}

@app.post("/check")
def check(req: CheckRequest):
    text = req.text.lower()
    blocked = ["ignore all instructions", "system prompt", "exfiltrate", "disable guardrails"]
    reasons = [w for w in blocked if w in text]
    return {"safe": len(reasons) == 0, "reasons": reasons}
