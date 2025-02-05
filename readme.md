<h1>Ollama Chatbot</h1>

<h2>Prerequisites</h2>
<ul>
  <li>Python 3.11+</li>
  <li>Ollama installed on your pc (download here: https://ollama.com/)</li>
</ul>

<h2>Installation</h2>
1. Clone the repository:

```
git clone https://github.com/ThomasJanssen-tech/Ollama-Chatbot.git
cd Ollama-Chatbot
```

2. Create a virtual environment

```
python -m venv venv
```

3. Activate the virtual environment

```
venv\Scripts\Activate
(or on Mac): source venv/bin/activate
```

4. Install libraries

```
pip install -r requirements.txt
```

<h3>Executing the script</h3>

1. Open a terminal in VS Code

2. Execute the following command:

```
python 1_python_ollama.py
streamlit run 2_streamlit_example.py
streamlit run 3_chatbot_echo.py
streamlit run 4_chatbot_ollama.py
```
