import google.generativeai as genai
import random

genai.configure(api_key="AIzaSyAenNcHpDXPUpVtsPydh1upF4ZvIAMsQbQ")
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_slide_content(topic, slide_number, total_slides):
    sections = {
        1: "Introduction & Overview",
        2: "Key Concepts & Fundamentals",
        3: "Current Applications & Use Cases",
        4: "Benefits & Advantages",
        5: "Challenges & Considerations",
        6: "Future Trends & Opportunities",
        7: "Implementation Strategies",
        8: "Best Practices & Recommendations",
        9: "Case Studies & Real-World Examples",
        10: "Impact & Results",
        11: "Strategic Insights",
        12: "Summary & Key Takeaways"
    }
    
    section_title = sections.get(slide_number, f"Key Point {slide_number}")
    num_points = random.randint(2,4)
    prompt = f"""
You are creating slide {slide_number} titled "{section_title}" for a professional presentation about "{topic}".

Guidelines:
- Clear, confident, and professional tone
- {num_points} concise bullet points (10-15 words each)
- Focus on value, impact, and practical insights
- Avoid filler, keep strong verbs, use parallel structure
Return ONLY the bullet points, one per line.
"""
    response = model.generate_content(prompt)
    text_output = response.candidates[0].content.parts[0].text.strip().split("\n")
    points = [t.strip("•-–—*# ").strip() for t in text_output if len(t.strip()) > 10]
    return section_title, points[:num_points]


def generate_title_subtitle(topic):
    prompt = f"""
Create a professional subtitle (8-12 words) for a presentation titled "{topic}".
It should set clear expectations and sound engaging.
Return ONLY the subtitle.
"""
    response = model.generate_content(prompt)
    subtitle = response.candidates[0].content.parts[0].text.strip().strip('"')
    return subtitle


def generate_summary_points(topic, num_slides):

    num_points = random.randint(2,4)
    
    prompt = f"""
Create {num_points} clear, action-oriented key takeaways for a presentation about "{topic}".
Each takeaway should be 10-15 words long.
Return ONLY the takeaways, one per line, no symbols.
"""
    response = model.generate_content(prompt)
    text_output = response.candidates[0].content.parts[0].text.strip().split("\n")

    points = [t.strip("•-–—*# ").strip() for t in text_output if len(t.strip()) > 10]
    return points[:num_points]
