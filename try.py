# # import fitz  # PyMuPDF
# from docx import Document

# # Use raw string or escape backslashes for Windows paths
# file_path_docx = r"C:\Users\ANDREW\Research Hub\media\articles\content\Assessment_in_Robotics_Education__A_Teaching_Guide.docx"

# def extract_text_from_pdf(file_path):
#     text = ""
#     with fitz.open(file_path) as doc:
#         for page in doc:
#             text += page.get_text()
#     return text.strip()

# def extract_text_from_docx(file_path):
#     doc = Document(file_path)
#     return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])

# print("DOCX TEST")
# print(extract_text_from_docx(file_path_docx))

