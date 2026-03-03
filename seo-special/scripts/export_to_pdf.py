import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

def markdown_to_pdf(domain):
    desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    report_dir = os.path.join(desktop, 'SEO_WORKSPACE', 'report', domain)
    
    if not os.path.exists(report_dir):
        print(f"Errore: Directory {report_dir} non trovata.")
        return

    pdf_path = os.path.join(report_dir, f"FULL_AUDIT_{domain}.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    body_style = ParagraphStyle('CustomBody', parent=styles['Normal'], fontSize=10, leading=12, alignment=TA_LEFT, spaceAfter=6)

    story = []
    story.append(Paragraph(f"SEO DEEP AUDIT - {domain.upper()}", styles['Title']))
    story.append(Spacer(1, 24))

    files = [f for f in os.listdir(report_dir) if f.endswith('.md')]
    files.sort()

    for filename in files:
        file_path = os.path.join(report_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        story.append(Paragraph(f"ANALISI: {filename.upper()}", styles['Heading1']))
        story.append(Spacer(1, 12))
        
        for line in content.split('\n'):
            if line.strip():
                story.append(Paragraph(line.replace('#', '').strip(), body_style))
        story.append(PageBreak())

    doc.build(story)
    print(f"PDF GENERATO: {pdf_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        markdown_to_pdf(sys.argv[1])
