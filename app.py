import os
import streamlit as st
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.rate_limiters import InMemoryRateLimiter


class Topics(BaseModel):
    """List of topics extracted from a question."""
    topics: list[str]

load_dotenv()
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")

# Load system prompt
with open("system_prompt.md", mode="r") as f:
    system_prompt: str = f.read()

# Cache the model so it persists across reruns
@st.cache_resource
def get_model():
    return ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite-preview",
        api_key=GEMINI_API_KEY,
        max_retries=5,
        thinking_level="minimal",
        rate_limiter=InMemoryRateLimiter(
            requests_per_second=15 / 60.0,
            check_every_n_seconds=0.5,
            max_bucket_size=15,
        ),
    )

llm = get_model()
structured_llm = llm.with_structured_output(Topics)

st.set_page_config(page_title="Topic Extractor Demo", layout="centered")
st.title("Topic Extractor Demo")

# Initialise topic frequency counter in session state
if "topic_counts" not in st.session_state:
    st.session_state.topic_counts = {}

question = st.text_area("Your question", height=200, placeholder="Paste or type a question here…")

if st.button("Extract Topics", type="primary"):
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Extracting topics…"):
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=question),
            ]
            result: Topics = structured_llm.invoke(messages)

        if result and result.topics:
            st.subheader("Extracted Topics")
            for topic in result.topics:
                st.markdown(f"- {topic}")
                # Update running counts
                st.session_state.topic_counts[topic] = (
                    st.session_state.topic_counts.get(topic, 0) + 1
                )
        else:
            st.info("No topics were extracted from the question.")

# Display running topic frequency in the sidebar
if st.session_state.topic_counts:
    st.sidebar.subheader("Topic Frequency")
    sorted_counts = sorted(
        st.session_state.topic_counts.items(), key=lambda x: x[1], reverse=True
    )
    st.sidebar.table(
        {"Topic": [t for t, _ in sorted_counts], "Count": [c for _, c in sorted_counts]}
    )
