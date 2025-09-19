const API_BASE = "http://localhost:8000"; // change if using Node backend (port 3000) or remote IP
const askBtn = document.getElementById('askBtn');
const voiceBtn = document.getElementById('voiceBtn');
const queryBox = document.getElementById('query');
const answerBox = document.getElementById('answer');
const imageInput = document.getElementById('imageInput');
const historyList = document.getElementById('historyList');

function addHistory(q, a){
  const li = document.createElement('li');
  li.textContent = q + " → " + (a?.slice(0,80) || '');
  historyList.prepend(li);
}

askBtn.onclick = async ()=>{
  const q = queryBox.value.trim();
  if(!q) return;
  answerBox.textContent = "Thinking...";
  try{
    const res = await fetch(API_BASE + "/query", {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({query: q})
    });
    const j = await res.json();
    answerBox.textContent = j.answer || j.error || "No answer";
    addHistory(q, j.answer);
  }catch(e){
    answerBox.textContent = "Error: " + e.message;
  }
}

// Voice input (very basic browser SpeechRecognition)
voiceBtn.onclick = ()=>{
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if(!SpeechRecognition){ alert("Voice not supported on this browser"); return; }
  const recog = new SpeechRecognition();
  recog.lang = 'en-IN';
  recog.onresult = (ev)=>{
    const text = ev.results[0][0].transcript;
    queryBox.value = text;
  }
  recog.start();
}

// Image upload -> send to /image endpoint
imageInput.onchange = async (e)=>{
  const f = e.target.files[0];
  if(!f) return;
  answerBox.textContent = "Uploading image...";
  const fd = new FormData();
  fd.append('image', f);
  try{
    const res = await fetch(API_BASE + "/image", {method:'POST', body: fd});
    const j = await res.json();
    answerBox.textContent = j.answer || j.error || "No result";
    addHistory("Image upload", j.answer);
  }catch(err){ answerBox.textContent = "Error: "+err.message; }
}