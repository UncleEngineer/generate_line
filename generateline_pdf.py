from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_number_table():
    numbers = list(range(1, 32))  # Generate numbers from 1 to 31
    
    # Prepare data for PDF export
    table_data = []
    for i in range(15):
        col1 = f"{numbers[i]}_" + "_" * 35
        col2 = f"{numbers[i+15]}_" + "_" * 35 if i+15 < len(numbers)-1 else ""
        table_data.append((col1, col2))
    
    # Add 31 on the left column alone
    table_data.append((f"{numbers[30]}_" + "_" * 35, ""))
    
    # Export to PDF
    export_to_pdf(table_data)

def export_to_pdf(data):
    pdf_filename = "number_table.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    width, height = A4
    margin = 28  # 1 cm margin (28 points in ReportLab)
    col_spacing = (width - 2 * margin) / 2  # Average spacing between columns
    row_spacing = (height - 2 * margin - 50) / 17  # Average row spacing for 17 rows
    
    # Title left-aligned
    title = "Monthly EP"
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, height - margin - 20, title)
    
    # Table content
    c.setFont("Helvetica", 12)
    y_position = height - margin - 50  # Start position after title
    
    for row in data:
        c.drawString(margin, y_position, row[0])
        c.drawString(margin + col_spacing, y_position, row[1])
        y_position -= row_spacing  # Move down for next row
        
        if y_position < margin:
            c.showPage()
            c.setFont("Helvetica", 12)
            y_position = height - margin - 50
    
    c.save()
    print(f"PDF saved as {pdf_filename}")

if __name__ == "__main__":
    generate_number_table()