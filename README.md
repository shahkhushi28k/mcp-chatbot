# 🧰 MCP Chatbot with Groq + FastMCP + Streamlit

A minimal end-to-end chatbot that integrates:

* **Groq LLMs** for fast inference
* **LangChain MCP Adapters** for tool usage
* **FastMCP servers** for custom tools
* **Streamlit UI** for interactive chat

---

## 🚀 Features

* 🔌 Multi-server MCP integration (local + remote)
* 🧠 Groq-powered LLM (fast + cost-efficient)
* 🛠️ Custom tools via FastMCP (e.g., math operations)
* 🎬 Manim integration for animation generation
* 💬 Clean chat UI using Streamlit

---

## 🏗️ Project Structure

```
mcp-chatbot/
│
├── client/
│   └── client2.py        # Streamlit app (main UI)
│
├── main.py               # FastMCP math server
│
├── LLM-Project/
│   └── manim-mcp-server/
│       └── src/
│           └── manim_server.py
│
├── .env                  # API keys
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repo

```bash
git clone <your-repo-url>
cd mcp-chatbot
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit langchain langchain-groq fastmcp python-dotenv
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## 🧠 MCP Servers

### Math Server (FastMCP)

Defined in `main.py`:

* `add(a, b)`
* `multiply(a, b)`

Run manually:

```bash
uv run --active fastmcp run main.py:mcp
```

---

### Manim Server

Runs animations using Manim.

Make sure Manim is installed:

```bash
pip install manim
```

---

## ▶️ Run the App

```bash
streamlit run client/client2.py
```

---

## 💡 Example Prompts

* "Add 30 and 60"
* "Multiply 7 and 8"
* "Create a Manim animation showing vector transformation"

---

## ⚠️ Known Issues

* Groq tool-calling can sometimes fail due to formatting
* Ensure MCP servers do not print to stdout
* Use `--active` with `uv` to avoid environment mismatch

---

## 🧪 Debugging Tips

* Test MCP servers independently:

```bash
uv run --active fastmcp run main.py:mcp
```

* Check tool loading errors in Streamlit logs
* Verify paths in MCP config

---

## 🔮 Future Improvements

* Add more MCP tools (DB, APIs, etc.)
* Improve tool-calling reliability
* Add streaming responses
* Deploy as web app

---

## 🤝 Contributing

Pull requests are welcome!

---