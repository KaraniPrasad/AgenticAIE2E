import streamlit as st
import json
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamLitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_results import DisplayResultStreamLit

# MAIN Function START
def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """

    # Load UI
    ui=LoadStreamLitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from UI")
        return
    
    #Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else :
        user_message = st.chat_input("Enter your message")

    
    if user_message:
        #config LLM
        try:
            obj_ll_config= GroqLLM(user_controls_input=user_input)
            model = obj_ll_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized.")
                return
            
            # initialize and setup the graph based on the use case
            usecase = user_input.get('selected_usecase')
            if not usecase:
                st.error("Error: No use case selected.")
                return
            
            ###graph builder
            graph_builder= GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamLit(usecase,graph,user_message).display_result_on_ui
            except Exception as e:
                st.error((f"Error graph setup failed with exception - {e}"))
        
        except Exception as e:
            raise ValueError(f"Error occurred with exception- {e}")
