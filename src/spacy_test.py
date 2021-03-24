import spacy_streamlit
import streamlit as st

def write():
    DEFAULT_TEXT = """Google was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a California privately held company on September 4, 1998, in California. Google was then reincorporated in Delaware on October 22, 2002."""

    spacy_model = "en_core_web_sm"

    st.title("My cool app")
    text = st.text_area("Text to analyze", DEFAULT_TEXT, height=200)
    doc = spacy_streamlit.process_text(spacy_model, text)

    spacy_streamlit.visualize_ner(
        doc,
        labels=["PERSON", "DATE", "GPE"],
        show_table=False,
        title="NER - Persons, dates and locations",
    )
    st.text(f"Analyzed using spaCy model {spacy_model}")

    models = ["en_core_web_sm"] #, "en_core_web_md"]
    default_text = "Sundar Pichai is the CEO of Google."
    spacy_streamlit.visualize(models, default_text)

if __name__ == "__main__":
    write()
