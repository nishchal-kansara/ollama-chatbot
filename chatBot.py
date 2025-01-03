import ollama
import streamlit as st
from fpdf import FPDF # type: ignore
import datetime

st.set_page_config(
    page_title="Ollama Chatbot",
    layout="wide",
    initial_sidebar_state="expanded",
)

def extract_model_names(models_info: list) -> tuple:
    return tuple(model.model for model in models_info["models"])

class PDF(FPDF):
    def header(self):
        self.add_font('Poppins-Bold', '', 'fonts/Poppins-Bold.ttf', uni=True)
        self.set_font('Poppins-Bold', '', 10)
        self.set_left_margin(15)
        self.set_right_margin(15)
        
        self.cell(0, 10, "Ollama Chatbot", border=0, align="R")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.add_font('Poppins-Bold', '', 'fonts/Poppins-Bold.ttf', uni=True)
        self.set_font('Poppins-Bold', '', 10)
        self.set_left_margin(15)
        self.set_right_margin(15)

        self.cell(0, 10, "Developed by Nishchal Kansara by Using Ollama", border=0, align="L")
        self.set_y(-15)
        self.cell(0, 10, f"{self.page_no()}", border=0, align="R")

def generate_pdf(messages: list):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.add_font('Poppins-Regular', '', 'fonts/Poppins-Regular.ttf', uni=True)
    pdf.add_font('Poppins-Bold', '', 'fonts/Poppins-Bold.ttf', uni=True)
    pdf.set_font('Poppins-Regular', '', 8)

    for message in messages:
        role = message["role"]
        content = message["content"]
        role_str = "Assistant:" if role == "assistant" else "User:"
        
        pdf.ln(5)
        
        pdf.set_font('Poppins-Bold', '', 8)
        pdf.multi_cell(0, 5, role_str, border=0, align="L")
        
        pdf.set_font('Poppins-Regular', '', 8) 
        pdf.multi_cell(0, 5, content, border=0, align="L")

    timestamp = datetime.datetime.now().strftime("%H%M%S%d%m%Y")
    temp_pdf_path = rf"{folder_path}/response-pdf/response-{timestamp}.pdf"  # type: ignore

    pdf.output(temp_pdf_path)
    return temp_pdf_path

class ModelNotSelectedError(Exception):
    pass

def main():
    st.subheader("Ollama Chatbot", divider="blue", anchor=False)

    models_info = ollama.list()
    available_models = extract_model_names(models_info)

    available_models_with_empty = [""] + list(available_models)

    selected_model = st.selectbox("Select a Model First:", available_models_with_empty)

    message_container = st.container(height=300, border=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if not selected_model and not st.session_state.messages: 
        start_message = f"Hello, I'm your assistant here to help! Before we begin, make sure you've selected the right model for your system. Each model serves a different purpose, so choosing the right one will ensure everything runs smoothly. Please double-check your choice!"
        st.session_state.messages = [{"role": "assistant", "content": start_message}]
    
    if selected_model:
        if not any(msg["content"].startswith("Your Model:") for msg in st.session_state.messages):
            st.session_state.messages.append({"role": "assistant", "content": f"Your Model: {selected_model}"})
        else:
            for idx, msg in enumerate(st.session_state.messages):
                if msg["content"].startswith("Your Model:"):
                    st.session_state.messages[idx]["content"] = f"Your Model: {selected_model}"

    for message in st.session_state.messages:
        avatar = "🤖" if message["role"] == "assistant" else "😎"
        with message_container.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    with st.container():
        st.markdown("""<style>.stMainBlockContainer { padding-bottom: 96px; } .stButton > button { float: right; }</style>""", unsafe_allow_html=True)

        if prompt := st.chat_input("Message Chatbot"):
            try:
                if not selected_model:
                    raise ModelNotSelectedError("Please select a model first!")
            
                #custom_prompt = ("Custom Prompt For Eg.: Please ensure all answers come from reputable sources with citations and links." + prompt)

                st.session_state.messages.append(
                    {"role": "user", "content": prompt}) #Change "prompt to custom_prompt" If Needed.

                message_container.chat_message(
                    "user", avatar="😎").markdown(prompt)

                with message_container.chat_message("assistant", avatar="🤖"):
                    with st.spinner("Thinking... 🤔😅"):
                        options = {
                            "num_ctx": 512,
                            "num_threads": 1
                        }

                        response = ollama.chat(
                            model=selected_model,
                            messages=[{"role": m["role"], "content": m["content"]} 
                                      for m in st.session_state.messages],
                            options=options
                        )

                        st.write(response["message"]["content"])

                    st.session_state.messages.append(
                        {"role": "assistant", "content": response["message"]["content"]})

            except ModelNotSelectedError as e:
                st.session_state.messages.append({"role": "assistant", "content": str(e)})
                st.error(f"Error: {e}", icon="⛔️")
            except Exception as e:
                st.error(f"Unexpected Error: {e}", icon="⛔️")

        if st.button("Save as PDF"):
            pdf_file = generate_pdf(st.session_state.messages)
            st.success(f"PDF saved at: {pdf_file}")

        st.markdown("""<hr style="border: 2px solid #0054a3;"/><footer style="text-align: center; padding: 5px; margin-top: 0px; margin-bottom: 0px;"><p>Developed with ❤️ by <a href="https://nishchal-kansara.web.app/" target="_blank" style="text-decoration: none; color: lightblue;">Nishchal Kansara</a> by Using  <a href="https://ollama.com/" target="_blank" style="text-decoration: none; color: lightblue;">Ollama</a> </p></footer>""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()