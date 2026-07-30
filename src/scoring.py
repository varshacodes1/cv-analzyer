from parser import extract_text_from_docx, split_into_sections

# Reference skill set for a QC Chemist role (industry-standard benchmark)
ROLE_SKILLS = {
    "QC Chemist": [
        "Quality Control",
        "Good Laboratory Practices",
        "Good Manufacturing Practices",
        "Raw Material Testing",
        "Finished Product Testing",
        "In-Process Quality Checks",
        "Stability Testing",
        "pH Testing",
        "Viscosity Testing",
        "Moisture Content Analysis",
        "Sample Preparation",
        "Batch Release Testing",
        "Standard Operating Procedures",
        "Documentation",
        "Calibration"
    ]
}

def match_skills(candidate_skills_text, role):
    required_skills = ROLE_SKILLS[role]
    candidate_text_lower = candidate_skills_text.lower()

    matched = []
    missing = []

    for skill in required_skills:
        if skill.lower() in candidate_text_lower:
            matched.append(skill)
        else:
            missing.append(skill)

    score = round((len(matched) / len(required_skills)) * 100, 2)

    return {
        "role": role,
        "score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }

if __name__ == "__main__":
    file_path = "data/resume.docx"
    raw_text = extract_text_from_docx(file_path)
    sections = split_into_sections(raw_text)

    skills_text = sections.get("Technical Skills", "")
    result = match_skills(skills_text, "QC Chemist")

    print(f"Role: {result['role']}")
    print(f"Score: {result['score']}%")
    print(f"Matched Skills: {result['matched_skills']}")
    print(f"Missing Skills: {result['missing_skills']}")