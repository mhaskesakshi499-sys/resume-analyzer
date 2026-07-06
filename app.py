import streamlit as st

from src.resume_analyzer import analyze_resume, extract_text_from_file


st.set_page_config(
    page_title="Resume Analyzer",
    layout="wide",
)


def main():
    st.title("Resume Analyzer")
    st.caption("LLM-powered resume analysis using LangChain and prompt engineering.")

    with st.sidebar:
        st.header("Input")
        uploaded_resume = st.file_uploader(
            "Upload resume",
            type=["pdf", "txt", "docx"],
        )
        analysis_mode = st.selectbox(
            "Analysis mode",
            ["Job Match", "General Review"],
        )

    job_description = st.text_area(
        "Paste job description",
        height=220,
        placeholder="Paste the job description here to compare it with the resume.",
        disabled=analysis_mode == "General Review",
    )

    if st.button("Analyze Resume", type="primary"):
        if uploaded_resume is None:
            st.warning("Please upload a resume first.")
            return

        if analysis_mode == "Job Match" and not job_description.strip():
            st.warning("Please paste a job description for job match analysis.")
            return

        with st.spinner("Reading resume and generating analysis..."):
            resume_text = extract_text_from_file(uploaded_resume)
            result = analyze_resume(
                resume_text=resume_text,
                job_description=job_description,
                analysis_mode=analysis_mode,
            )

        st.subheader("Analysis")
        st.markdown(result)

        with st.expander("Extracted resume text"):
            st.write(resume_text)

    st.info("Upload a resume, paste a job description, and click Analyze Resume.")


if __name__ == "__main__":
    main()
