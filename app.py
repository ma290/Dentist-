import gradio as gr
from PIL import Image
import random

def dental_ai_report(image, age, pain_level, notes):
    findings = [
        "Possible dental caries (cavity) detected",
        "Signs of gum inflammation (gingivitis)",
        "Tooth enamel wear observed",
        "Possible wisdom tooth complication",
        "No major abnormality detected"
    ]

    treatments = {
        "Possible dental caries (cavity) detected": ("Filling / RCT", "₹2,000 – ₹6,000"),
        "Signs of gum inflammation (gingivitis)": ("Scaling & Polishing", "₹1,500 – ₹3,000"),
        "Tooth enamel wear observed": ("Fluoride Treatment", "₹800 – ₹2,000"),
        "Possible wisdom tooth complication": ("Dental X-ray + Extraction", "₹3,000 – ₹10,000"),
        "No major abnormality detected": ("Routine Checkup", "₹500 – ₹1,000")
    }

    selected = random.choice(findings)
    treatment, cost = treatments[selected]

    report = f"""
🦷 **AI Dental Screening Report**

🔹 **Observation**
{selected}

🔹 **Suggested Treatment**
{treatment}

🔹 **Estimated Cost (India)**
{cost}

🔹 **Patient Explanation (Hindi)**
Is image ke hisaab se daant ya masoodon me samasya ho sakti hai.  
Doctor se clinical examination zaroor karwayein.

⚠️ *Note:*  
Yeh report sirf preliminary AI screening ke liye hai, final diagnosis dentist karega.
"""

    return report


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🦷 AI Dental Report Generator  
    ### Smart Assistant for Dental Clinics
    Upload dental image/X-ray to generate instant patient report.
    """)

    with gr.Row():
        image = gr.Image(type="pil", label="Upload Dental Image / X-ray")

    with gr.Row():
        age = gr.Number(label="Patient Age", value=30)
        pain = gr.Radio(
            ["No Pain", "Mild", "Moderate", "Severe"],
            label="Pain Level",
            value="Mild"
        )

    notes = gr.Textbox(label="Additional Notes (Optional)")

    generate = gr.Button("🧠 Generate AI Dental Report")

    output = gr.Markdown()

    generate.click(
        dental_ai_report,
        inputs=[image, age, pain, notes],
        outputs=output
    )

    gr.Markdown("""
    ---
    🔐 **Clinic Version Features (Paid):**
    - Unlimited reports
    - Clinic logo & name
    - PDF download
    - Patient history storage
    - WhatsApp sharing

    📩 Contact for full version
    """)

demo.launch()
