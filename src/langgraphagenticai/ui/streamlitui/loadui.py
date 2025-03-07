import streamlitui as st
import os 
from datetime import date

from langchain_core.messages import AIMessage, HumanMessage
from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamLitUI:
    def __init__(self):
        self.config= Config() #config
        self.user_controls = {}
    
    def initialize_session(self):
        return {
            "current_step":"requirements",
            "requirements": "",
            "user_stories": "",
            "po_feedback": "",
            "generated_code": "",
            "review_feedback": "",
            "decision": None
    }
  
    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False

        with st.sidebar:
            #get options from config
            llm_options = self.config.get_llm_options()
            usecase_options=self.config.get_usecase_options()

            #LLM selection
            if self.user_controls["selected_llm"] == 'Groq':
                #Model selection
                model_options= self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectedbox("Select Model", model_options)
                #API key input
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")

                #Validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")

            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()

        return self.user_controls

