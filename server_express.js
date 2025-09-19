// server_express.js
const express = require('express');
const multer = require('multer');
const fs = require('fs');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
app.use(bodyParser.json());
const upload = multer({ dest: 'tmp/' });

const KB = JSON.parse(fs.readFileSync(path.join(__dirname,'kb.json')));

function simpleRetrieve(q){
  const ql = q.toLowerCase();
  const hits = KB.filter(d=>{
    return d.title.toLowerCase().includes(ql) || d.content.toLowerCase().includes(ql);
  }).map(d=>d.content);
  return hits.length ? hits.slice(0,3) : KB.slice(0,2).map(d=>d.content);
}

app.post('/query', (req, res)=>{
  const q = (req.body.query || '').trim();
  if(!q) return res.json({ error: "empty query" });
  const retrieved = simpleRetrieve(q);
  let answer = "Found:\n\n" + retrieved.join("\n\n") + "\n\nSuggestion: ";
  if(q.toLowerCase().includes('blight')) answer += 'Remove infected leaves and use copper fungicide.';
  else if(q.toLowerCase().includes('water')) answer += 'Adjust irrigation as per crop stage.';
  else answer += 'See above; contact agri officer if unsure.';
  res.json({ answer, retrieved });
});

app.post('/image', upload.single('image'), (req, res)=>{
  // placeholder
  res.json({ answer: "Image received (demo). Implement TF/OpenCV here.", path: req.file.path });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, ()=>console.log("Server running on", PORT));