<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>KrishiMitra — Farmer Assistant</title>
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <style>
    /* Reset & base */
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', Tahoma, sans-serif;
      background: linear-gradient(135deg, #f4fbf4, #e2f0e9);
      color: #333;
      line-height: 1.6;
    }

    /* Header */
    /*.header {
      text-align: center;
      padding: 2rem 1rem;
      background: #2e7d32;
      color: white;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }*/

    .header {
        text-align: left;
        padding: 2rem 1rem;
        background: #2e7d32;
        color: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15) ;
    }
    .header h1 {
      font-size: 2.2rem;
      margin-bottom: 0.5rem;
    }
    .header p {
      font-size: 1.1rem;
      opacity: 0.9;
    }

    /* Container layout */
    .container {
      max-width: 900px;
      margin: 2rem auto;
      padding: 0 1rem;
      display: grid;
      gap: 2rem;
    }

    .navbar a {
    text-align: left;
    font-size: 1.7rem;
    color: white;
    margin-left: 4rem;
    transition: .3s;
    }

    .navbar a:hover,
    .navbar a.active{
        color: white;
    }

    .navbar.active {
        position: fixed;
        width: 100%;
        height: 45vh;
        left: 0;
        padding: 1rem 3%;
        background: var(--bg-color);
        border-top: .1rem solid rgba(0, 0, 0, .2);
        box-shadow: 0 .5rem 1rem rgba(0, 0, 0, .2);
        text-align: center;
        transition: all .5s ease;
    }
    .navbar a {
        display: block;
        font-size: 2rem;
        margin: 3rem 0;
    }




    /* Card-like sections */
    .input-box, .answer-box, .history-box, .chatbot-box {
      background: #fff;
      border-radius: 14px;
      padding: 1.5rem;
      box-shadow: 0 4px 12px rgba(0,0,0,0.08);
      transition: transform 0.2s ease-in-out;
    }
    .input-box:hover, .answer-box:hover, .history-box:hover, .chatbot-box:hover {
      transform: translateY(-3px);
    }

    /* Input area */
    #query {
      width: 100%;
      padding: 1rem;
      border-radius: 10px;
      border: 1px solid #ccc;
      font-size: 1rem;
      resize: none;
      margin-bottom: 1rem;
      transition: border 0.2s;
    }
    #query:focus {
      outline: none;
      border-color: #2e7d32;
      box-shadow: 0 0 0 3px rgba(46, 125, 50, 0.2);
    }

    /* Controls row */
    .controls {
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
    }
    .btn {
      padding: 0.7rem 1.4rem;
      border: none;
      border-radius: 10px;
      cursor: pointer;
      font-size: 0.95rem;
      transition: background 0.3s, transform 0.2s;
    }
    .btn.primary {
      background: #2e7d32;
      color: white;
    }
    .btn.primary:hover {
      background: #256628;
      transform: translateY(-2px);
    }
    .btn.secondary {
      background: #e0e0e0;
      color: #333;
    }
    .btn.secondary:hover {
      background: #ccc;
      transform: translateY(-2px);
    }
    .file-label {
      background: #f0f0f0;
      padding: 0.7rem 1.4rem;
      border-radius: 10px;
      cursor: pointer;
      font-size: 0.95rem;
      display: inline-block;
      transition: background 0.3s, transform 0.2s;
    }
    .file-label:hover {
      background: #ddd;
      transform: translateY(-2px);
    }
    .file-label input {
      display: none;
    }

    /* Answer box */
    .answer-box h2 {
      margin-bottom: 1rem;
      color: #2e7d32;
    }
    .answer {
      background: #f9f9f9;
      padding: 1rem;
      border-radius: 10px;
      border: 1px solid #ddd;
      min-height: 80px;
      font-size: 0.95rem;
      color: #444;
    }

    /* History */
    .history-box h3 {
      margin-bottom: 1rem;
      color: #2e7d32;
    }
    #historyList {
      list-style: none;
    }
    #historyList li {
      padding: 0.5rem 0;
      border-bottom: 1px solid #eee;
      font-size: 0.95rem;
    }
    #historyList li:last-child {
      border-bottom: none;
    }

    /* Chatbot styles */
    .chatbot-box h2 {
      margin-bottom: 1rem;
      color: #2e7d32;
    }
    .chat-window {
      background: #f9f9f9;
      border: 1px solid #ddd;
      border-radius: 10px;
      height: 300px;
      overflow-y: auto;
      padding: 1rem;
      margin-bottom: 1rem;
      font-size: 0.95rem;
    }
    .chat-message {
      margin-bottom: 1rem;
      padding: 0.6rem 0.9rem;
      border-radius: 10px;
      max-width: 75%;
      line-height: 1.4;
    }
    .chat-message.user {
      background: #e2f0e9;
      margin-left: auto;
      text-align: right;
    }
    .chat-message.bot {
      background: #e8f5e9;
      margin-right: auto;
    }
    .chat-input {
      display: flex;
      gap: 0.5rem;
    }
    .chat-input input {
      flex: 1;
      padding: 0.8rem;
      border-radius: 8px;
      border: 1px solid #ccc;
      font-size: 0.95rem;
    }
    .chat-input button {
      background: #2e7d32;
      color: white;
      border: none;
      padding: 0.8rem 1.2rem;
      border-radius: 8px;
      cursor: pointer;
      transition: background 0.3s;
    }
    .chat-input button:hover {
      background: #256628;
    }
  </style>
</head>
<body>
  <header class="header">
    <h1>🌾 KrishiMitra</h1>
    <p>Your offline farming assistant</p>
    
  </header>

  <main class="container">
    <section class="input-box">
      <textarea id="query" placeholder="Ask a question about crops, pests, subsidies..." rows="3"></textarea>
      <div class="controls">
        <button id="askBtn" class="btn primary">Ask</button>
        <button id="voiceBtn" class="btn secondary">🎤 Voice</button>
        <label class="file-label">
          📷 Image <input id="imageInput" type="file" accept="image/*">
        </label>
      </div>
    </section>

    <section class="answer-box">
      <h2>Answer</h2>
      <div id="answer" class="answer">Type a question to see results.</div>
    </section>

    <section class="history-box">
      <h3>Recent Questions</h3>
      <ul id="historyList"></ul>
    </section>

    <!-- Chatbot mockup -->
    <section class="chatbot-box">
      <h2>🤖 Chatbot</h2>
      <div class="chat-window" id="chatWindow">
        <div class="chat-message bot">Hello! I am KrishiMitra. How can I help you today?</div>
        <div class="chat-message user">Give me tips for paddy cultivation.</div>
        <div class="chat-message bot">Sure! Ensure proper irrigation and apply nitrogen fertilizer this week.</div>
      </div>
      <div class="chat-input">
        <input type="text" id="chatInput" placeholder="Type a message...">
        <button id="sendBtn">Send</button>
      </div>
    </section>
  </main>

  <script src="app.js"></script>
</body>
</html>
