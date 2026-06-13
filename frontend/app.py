import streamlit as st
import requests
import traceback

# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)


# =====================================
# Title
# =====================================

st.title("📄 AI Resume Screening System")

st.write("Upload your resume and analyze it against a job description.")


# =====================================
# Resume Upload
# =====================================

resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if resume_file:

    st.success(f"Uploaded: {resume_file.name}")

    # =====================================
    # Job Description
    # =====================================

    job_description = st.text_area(
        "Paste Job Description",
        height=250
    )

    if job_description:

        st.success("Job Description Added")

        analyze_btn = st.button("🔍 Analyze Resume")

        if analyze_btn:

            st.info("Analysis Started...")

            try:

                # =====================================
                # Upload Resume API
                # =====================================

                files = {
                    "file": (
                        resume_file.name,
                        resume_file.getvalue(),
                        "application/pdf"
                    )
                }

                upload_response = requests.post(
                    "http://127.0.0.1:8000/upload-resume",
                    files=files
                )

                if upload_response.status_code != 200:
                    st.error("Resume Upload Failed")
                    st.write(upload_response.text)
                    st.stop()

                resume_data = upload_response.json()
                resume_id = resume_data["resume_id"]

                # =====================================
                # Analyze Resume API
                # =====================================

                analyze_response = requests.post(
                    "http://127.0.0.1:8000/analyze-direct",
                    json={
                        "resume_id": resume_id,
                        "job_description": job_description
                    }
                )

                if analyze_response.status_code != 200:
                    st.error("Analysis API Failed")
                    st.write(analyze_response.text)
                    st.stop()

                result = analyze_response.json()
                st.write(result)

                # =====================================
                # Success Message
                # =====================================

                st.success("✅ Analysis Completed!")

                # =====================================
                # Result Metrics
                # =====================================

                st.subheader("📊 Analysis Result")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("ATS Score", f"{result['ats_score']}%")
                    st.progress(int(result["ats_score"]))

                with col2:
                    st.metric("Final AI Score", f"{result['final_ai_score']}%")

                with col3:
                    st.metric(
                        "Selection Probability",
                        f"{result['selection_probability']}%"
                    )
                    st.progress(int(result["selection_probability"]))

                # =====================================
                # Similarity Score
                # =====================================

                similarity_score = result.get("similarity_score", 0)

                st.subheader("📈 Similarity Score")
                st.progress(min(int(similarity_score), 100))
                st.write(f"{similarity_score}%")

                # =====================================
                # Matched Skills
                # =====================================

                st.subheader("✅ Matched Skills")

                matched_skills = result.get("matched_skills", [])

                if matched_skills:
                    for skill in matched_skills:
                        st.success(skill)
                else:
                    st.warning("No matched skills found.")

                # =====================================
                # Missing Skills
                # =====================================

                st.subheader("❌ Missing Skills")

                missing_skills = result.get("missing_skills", [])

                if missing_skills:
                    for skill in missing_skills:
                        st.error(skill)
                else:
                    st.success("No missing skills found.")

                # =====================================
                # Recommendations
                # =====================================

                st.subheader("💡 Recommendations")

                recommendations = result.get("recommendations", [])

                if recommendations:
                    for recommendation in recommendations:
                        st.info(recommendation)
                else:
                    st.success(
                        "Your resume is already well aligned with the job description."
                    )
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.code(traceback.format_exc())