from parser import extract_text_from_docx, split_into_sections
from scoring import match_skills

SKILL_TO_COURSE = {
    "Quality Control": "QC Fundamentals Certification",
    "Good Laboratory Practices": "GLP Compliance Workshop",
    "Good Manufacturing Practices": "GMP Essentials Course",
    "Raw Material Testing": "Analytical Testing Bootcamp",
    "Finished Product Testing": "Analytical Testing Bootcamp",
    "In-Process Quality Checks": "QC Process Control Course",
    "Stability Testing": "Pharma Stability Studies Course",
    "pH Testing": "Lab Instrumentation Basics",
    "Viscosity Testing": "Lab Instrumentation Basics",
    "Moisture Content Analysis": "Lab Instrumentation Basics",
    "Sample Preparation": "Lab Techniques Fundamentals",
    "Batch Release Testing": "QC Process Control Course",
    "Standard Operating Procedures": "SOP Writing & Compliance Course",
    "Documentation": "Lab Documentation Best Practices",
    "Calibration": "Instrument Calibration Course"
}

def recommend_courses(missing_skills):
    recommendations = set()
    for skill in missing_skills:
        course = SKILL_TO_COURSE.get(skill)
        if course:
            recommendations.add(course)
    return list(recommendations)

if __name__ == "__main__":
    file_path = "data/resume.docx"
    raw_text = extract_text_from_docx(file_path)
    sections = split_into_sections(raw_text)

    skills_text = sections.get("Technical Skills", "")
    result = match_skills(skills_text, "QC Chemist")

    print(f"Score: {result['score']}%")
    print(f"Missing Skills: {result['missing_skills']}")

    recommendations = recommend_courses(result['missing_skills'])
    if recommendations:
        print("Recommended Courses:")
        for course in recommendations:
            print(f" - {course}")
    else:
        print("No recommendations needed — all required skills present!")

    test_recommendations = recommend_courses(["pH Testing", "Calibration"])
    print("\nTest recommendations:", test_recommendations)