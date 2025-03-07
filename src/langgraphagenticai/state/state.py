from typing import Annotated, Literal, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from typing import TypedDict, Annoted, List
from langchain_core.messages import HumanMessage,AIMessage

class State(TypedDict):
    """
    Representing the structure of the state used in the graph

    """

    messages: Annotated[list, add_messages]



