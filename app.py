import streamlit as st
from dict_api import fetch_word_data
from response_parser import parse_dictionary_response

st.set_page_config(
    page_title="Dictionary",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("## Dictionary App")
st.caption("Type a word and press Enter")

if "search_word" not in st.session_state:
    st.session_state.search_word = ""

def on_enter():
    word = st.session_state.word_input.strip().lower()
    st.session_state.search_word = word

@st.cache_data(show_spinner=False)
def fetch_cached_word(word):
    return fetch_word_data(word)

st.text_input(
    "Search",
    placeholder="Enter a word",
    key="word_input",
    on_change=on_enter
)

if st.session_state.search_word:
    with st.spinner("Searching..."):
        data = fetch_cached_word(st.session_state.search_word)

    if data == "NETWORK_ERROR":
        st.error("Network error. Please try again later.")

    elif data is None:
        st.warning("Word not found. Please check the spelling.")

    else:
        parsed = parse_dictionary_response(data)

        st.markdown(f"### {parsed['word']}")

        if parsed["phonetics"]:
            st.write("Phonetics:", ", ".join(parsed["phonetics"]))

        st.write("")

        for meaning in parsed["meanings"]:
            with st.container():
                st.markdown(f"#### {meaning['part_of_speech'].capitalize()}")

                for definition in meaning["definitions"]:
                    st.write("- ", definition)

                if meaning["antonyms"]:
                    st.caption("Antonyms: " + ", ".join(meaning["antonyms"]))

                st.write("")
