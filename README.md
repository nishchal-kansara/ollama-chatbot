# Ollama Chatbot

A conversational chatbot built using **Streamlit** and **Ollama**, designed to interact with users, process queries, and generate responses using AI models. It also includes the functionality to save chat conversations as **PDF files**.

## 🚀 **Features**
- **Interactive Chat Interface:** Communicate seamlessly with the chatbot.
- **Model Selection:** Choose from available AI models provided by Ollama.
- **PDF Export:** Save chat conversations as downloadable PDF files.
- **User-Friendly UI:** Responsive and clean design using Streamlit.

## 🛠️ **Tech Stack**
- **Python**: Core programming language.
- **Streamlit**: Frontend for chatbot UI.
- **Ollama**: Backend AI model provider.
- **FPDF**: PDF generation library.

## 📦 **Installation**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/ollama-chatbot.git
   cd ollama-chatbot
   ```

2. **Ollama Setup:**
    - **Download Ollama:** [Ollama Download Page](https://ollama.com/download)
    - **Explore Model Library:** [Ollama Model Library](https://github.com/ollama/ollama?tab=readme-ov-file#model-library)

3. **Install Dependencies:**
    - **Streamlit:** [Installation Guide](https://docs.streamlit.io/get-started/installation/command-line)
      ```bash
      pip install streamlit
      ```
    - **Ollama:**
      ```bash
      pip install ollama
      ```
    - **Pull and Verify Model:**
      ```bash
      ollama pull {model: model_library}
      ollama list
      ollama run {pulled_model}
      ```
    - **FPDF:**
      ```bash
      pip install fpdf
      ```

4. **Run the Application:**
   ```bash
   streamlit run chatBot.py
   ```

## 📑 **How to Use**

1. **Select an AI Model:**
   - Use the dropdown to pick an available Ollama model.

2. **Start Chatting:**
   - Type your message in the chat input field and interact with the AI.

3. **Save Chat as PDF:**
   - Click on **"Save as PDF"** to download the chat conversation.

## 📝 **Folder Structure**
```
ollama-chatbot/
├── chatBot.py        # Main application file
├── fonts/            # Folder for font files
├── response-pdf/     # Folder for saving generated PDFs
├── README.md
```

## ⚠️ **Error Handling**
- If no model is selected, an error message will prompt the user.
- Any unexpected errors will be displayed in the Streamlit interface.

## 🌐 **Resources**
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Ollama Documentation](https://ollama.com/)
- [Ollama Model Library](https://github.com/ollama/ollama?tab=readme-ov-file#model-library)
- [FPDF Documentation](https://pyfpdf.readthedocs.io/)

## 🎬 **Video Tutorial**  
Check Out Video Tutorial Here: [**Click Here to Watch Video Tutorial**](https://youtu.be/PX7e-Ku9wJo)

Enjoy building with Ollama Chatbot! 🤖✨

## 👤 **Author**
Developed by [**Nishchal Kansara**](https://nishchal-kansara.web.app/) using [**Ollama**](https://ollama.com/)

### Check out My Projects & Resume
1. **Personal Website:** [https://nishchal-kansara.web.app/](https://nishchal-kansara.web.app/)
2. **Resume:** [https://nishchal-kansara.web.app/resume.html](https://nishchal-kansara.web.app/resume.html)


**Connect with me on LinkedIn:** [Nishchal Kansara](https://www.linkedin.com/in/nishchal-kansara/)
