import csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from statistics import mean

def read_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data

def analyze_data(data):
    scores = [int(row['Score']) for row in data]
    average_score = mean(scores)
    return average_score

def generate_pdf(data, average_score, output_file):
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 50, "Employee Performance Report")

    c.setFont("Helvetica", 12)
    y = height - 100
    c.drawString(50, y, "Name")
    c.drawString(200, y, "Department")
    c.draw…