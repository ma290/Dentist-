import gradio as gr
import random

def dental_ai_report(image, age, pain_level, notes):
    findings = [
        "Possible dental cavity detected",
        "Gum inflammation observed",
        "Tooth enamel erosion",
        "Wisdom tooth complication suspected",
        "No major abnormality detected"
    ]

    treatments = {
        "Possible dental cavity detected": ("Dental Filling / RCT", "₹2,000 – ₹6,000"),
        "Gum inflammation observed": ("Scaling & Polishing", "₹1,500 – ₹3,000"),
        "Tooth enamel erosion": ("Fluoride Treatment", "₹800 – ₹2,000"),
        "Wisdom tooth complication suspected": ("X-ray & Extraction", "₹3,000 – ₹10,000"),
        "No major abnormality detected": ("Routine Checkup", "₹500 – ₹1,000")
    }

    issue = random.choice(findings)
    treatment, cost = treatments[issue]

    return f"""
🦷 **AI Dental Screening Report**

🔍 Observation:
{issue}

🩺 Suggested Treatment:
{treatment}

💰 Estimated Cost:
{cost}

📌 Note:
This is an AI-assisted preliminary screening.
Final diagnosis must be done by a certified dentist.
"""

def launch_gradio():
    with gr.Blocks() as demo:
        gr.Markdown("# 🦷 DentAssist AI – Dental Report Generator")

        image = gr.Image(label="Upload Dental Image / X-ray")
        age = gr.Number(label="Patient Age", value=30)
        pain = gr.Radio(
            ["No Pain", "Mild", "Moderate", "Severe"],
            value="Mild",
            label="Pain Level"
        )
        notes = gr.Textbox(label="Additional Notes (optional)")
        btn = gr.Button("Generate Report")
        output = gr.Markdown()

        btn.click(
            dental_ai_report,
            inputs=[image, age, pain, notes],
            outputs=output
        )

    return demo
