import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import os
from reportlab.pdfgen import canvas

def on_drop(event):
    files = root.tk.splitlist(event.data)
    for file in files:
        if file.lower().endswith('.pdf'):
            pdf_listbox.insert(tk.END, file)
        else:
            messagebox.showwarning("Warning", f"'{os.path.basename(file)}' is not a PDF file.")

def select_files():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")], title="Select PDF Files")
    for file in files:
        pdf_listbox.insert(tk.END, file)

def add_page_numbers(pdf_path):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    temp_files = []

    for i, page in enumerate(reader.pages, start=1):
        temp_file = f"temp_page_{i}.pdf"
        temp_files.append(temp_file)
        
        # Create a PDF with only the page number
        c = canvas.Canvas(temp_file, pagesize=(page.mediabox.width, page.mediabox.height))
        c.drawString(page.mediabox.width / 2 - 10, 20, f"- {i} -")  # Centered at the bottom
        c.save()
        
        # Merge the page number PDF onto the original page
        temp_reader = PdfReader(temp_file)
        page.merge_page(temp_reader.pages[0])
        writer.add_page(page)

    with open(pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

    # Clean up temp files
    for temp_file in temp_files:
        os.remove(temp_file)

def concat_pdfs():
    if pdf_listbox.size() == 0:
        messagebox.showwarning("Warning", "No PDFs selected for merging.")
        return

    files = sorted(pdf_listbox.get(0, tk.END))
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Save Merged PDF")
    if not save_path:
        return

    merger = PdfMerger()
    progress_bar['maximum'] = len(files)
    try:
        for index, file in enumerate(files, start=1):
            merger.append(file)
            progress_bar['value'] = index  # Update progress bar
            root.update_idletasks()

        merger.write(save_path)
        merger.close()
        
        # Add page numbers to the merged PDF
        add_page_numbers(save_path)
        
        messagebox.showinfo("Success", f"PDFs successfully merged into '{save_path}'.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to merge PDFs. Error: {str(e)}")
    finally:
        merger.close()
        progress_bar['value'] = 0  # Reset progress bar

def clear_list():
    pdf_listbox.delete(0, tk.END)

# GUI setup
root = TkinterDnD.Tk()
root.title("PDF Merger")
root.geometry("600x450")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# PDF listbox
listbox_frame = tk.LabelFrame(frame, text="Selected PDFs", padx=5, pady=5)
listbox_frame.pack(fill=tk.BOTH, expand=True)

pdf_listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE)
pdf_listbox.pack(fill=tk.BOTH, expand=True)

# Enable drag & drop
pdf_listbox.drop_target_register(DND_FILES)
pdf_listbox.dnd_bind("<<Drop>>", on_drop)

# Buttons
button_frame = tk.Frame(frame)
button_frame.pack(fill=tk.X, pady=10)

select_button = tk.Button(button_frame, text="Select PDFs", command=select_files)
select_button.pack(side=tk.LEFT, padx=5, pady=5)

concat_button = tk.Button(button_frame, text="Concat", command=concat_pdfs)
concat_button.pack(side=tk.LEFT, padx=5, pady=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_list)
clear_button.pack(side=tk.LEFT, padx=5, pady=5)

quit_button = tk.Button(button_frame, text="Quit", command=root.quit)
quit_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Progress bar
progress_bar = ttk.Progressbar(frame, orient="horizontal", length=580, mode='determinate')
progress_bar.pack(pady=5)

root.mainloop()
