import os
import re
import datetime
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

class ResponseGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("BIDONEX & ShakerX Response Generator")
        self.root.geometry("1000x800")
        
        # Load data from files
        self.company_info = self.load_file("company_info.txt")
        self.product_info = self.load_file("product_info.txt")
        self.pricing_info = self.load_file("pricing_info.txt")
        self.email_templates = self.load_file("email_templates.txt")
        self.response_guidelines = self.load_file("response_guidelines.txt")
        
        # Create UI
        self.create_ui()
    
    def load_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return f"Error: {filename} not found."
    
    def create_ui(self):
        # Create main frame
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create input and output frames
        input_frame = ttk.LabelFrame(main_frame, text="Customer Input", padding=10)
        input_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        output_frame = ttk.LabelFrame(main_frame, text="Generated Response", padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True)
        
        # Customer input text area
        self.customer_input = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, height=10)
        self.customer_input.pack(fill=tk.BOTH, expand=True)
        
        # Response type selection
        response_type_frame = ttk.Frame(main_frame)
        response_type_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(response_type_frame, text="Response Type:").pack(side=tk.LEFT, padx=(0, 10))
        
        self.response_type = tk.StringVar()
        response_types = [
            "Initial Inquiry Response",
            "Quotation Response",
            "Sample Request Response",
            "Order Confirmation & Payment Details",
            "Shipping Confirmation",
            "Follow-up Email",
            "Addressing Minimum Order Quantities",
            "Addressing Printing Options",
            "Addressing Color Variations"
        ]
        
        response_type_combo = ttk.Combobox(response_type_frame, textvariable=self.response_type, values=response_types, width=30)
        response_type_combo.pack(side=tk.LEFT)
        response_type_combo.current(0)
        
        # Generate button
        generate_button = ttk.Button(main_frame, text="Generate Response", command=self.generate_response)
        generate_button.pack(pady=10)
        
        # Generated response text area
        self.generated_response = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, height=15)
        self.generated_response.pack(fill=tk.BOTH, expand=True)
        
        # Copy button
        copy_button = ttk.Button(main_frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.pack(pady=10)
        
        # Client data frame
        client_data_frame = ttk.LabelFrame(main_frame, text="Client Data for Record-Keeping", padding=10)
        client_data_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.client_data = scrolledtext.ScrolledText(client_data_frame, wrap=tk.WORD, height=10)
        self.client_data.pack(fill=tk.BOTH, expand=True)
    
    def extract_client_info(self, text):
        """Extract client information from the input text"""
        client_data = {
            "E-mail": "",
            "Company": "",
            "Contact": "",
            "Country": "",
            "Product": "",
            "Quantity": "",
            "Colors": "",
            "Status": "",
            "Value": "",
            "Address": "",
            "VAT": "",
            "Phone": "",
            "Notes": ""
        }
        
        # Extract email
        email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
        if email_match:
            client_data["E-mail"] = email_match.group(0)
        
        # Extract product
        product_match = re.search(r'(BID\d{3}|ShakerX \d{3} ?ml( 2 in 1)?)', text, re.IGNORECASE)
        if product_match:
            client_data["Product"] = product_match.group(0)
        
        # Extract quantity
        quantity_match = re.search(r'(\d+)( units| pieces| pcs)', text, re.IGNORECASE)
        if quantity_match:
            client_data["Quantity"] = quantity_match.group(1)
        
        # Extract colors
        colors_match = re.search(r'(\d+) colou?rs?', text, re.IGNORECASE)
        if colors_match:
            client_data["Colors"] = colors_match.group(1)
        
        # Extract value
        value_match = re.search(r'Total cost = (\d+\.\d{2}) EUR', text)
        if value_match:
            client_data["Value"] = value_match.group(1) + " EUR"
        
        # Set status based on response type
        response_type = self.response_type.get()
        if "Quotation" in response_type:
            client_data["Status"] = "Quote Sent"
        elif "Sample" in response_type:
            client_data["Status"] = "Sample Requested"
        elif "Order Confirmation" in response_type:
            client_data["Status"] = "Order Placed"
        elif "Shipping" in response_type:
            client_data["Status"] = "Order Shipped"
        else:
            client_data["Status"] = "Initial Contact"
        
        return client_data
    
    def format_client_data(self, client_data):
        """Format client data for display"""
        formatted_data = ""
        for key, value in client_data.items():
            formatted_data += f"{key}: {value}\n"
        return formatted_data
    
    def get_template(self, template_name):
        """Extract the specified template from email_templates.txt"""
        pattern = rf"## {re.escape(template_name)}\n\n(.*?)(?=\n\n##|\Z)"
        match = re.search(pattern, self.email_templates, re.DOTALL)
        if match:
            return match.group(1).strip()
        return "Template not found."
    
    def generate_response(self):
        """Generate a response based on the selected template and customer input"""
        customer_text = self.customer_input.get("1.0", tk.END).strip()
        if not customer_text:
            messagebox.showwarning("Input Required", "Please enter customer text.")
            return
        
        template_name = self.response_type.get()
        template = self.get_template(template_name)
        
        # Extract client name if possible
        client_name_match = re.search(r'Dear ([^,\n]+)', customer_text)
        client_name = client_name_match.group(1) if client_name_match else "[Client Name]"
        
        # Replace placeholders
        response = template.replace("[Client Name]", client_name)
        response = response.replace("[Your Name]", "Bartosz Kula")
        response = response.replace("[Your Position]", "International Sales Manager")
        response = response.replace("[Your Email]", "bartoszkula@bidonex.com")
        
        # For quotation responses, try to fill in more details
        if template_name == "Quotation Response":
            # Extract product model if mentioned
            model_match = re.search(r'(BID\d{3}|ShakerX \d{3} ?ml( 2 in 1)?)', customer_text, re.IGNORECASE)
            model = model_match.group(0) if model_match else "[Model Name]"
            response = response.replace("[Model Name]", model)
            
            # Extract quantity if mentioned
            quantity_match = re.search(r'(\d+)( units| pieces| pcs)', customer_text, re.IGNORECASE)
            quantity = quantity_match.group(1) if quantity_match else "[Quantity]"
            response = response.replace("[Quantity]", quantity)
            
            # Extract colors if mentioned
            colors_match = re.search(r'(\d+) colou?rs?', customer_text, re.IGNORECASE)
            colors = colors_match.group(1) if colors_match else "1"
            response = response.replace("[Number of Colors]", colors)
        
        # Display the response
        self.generated_response.delete("1.0", tk.END)
        self.generated_response.insert(tk.END, response)
        
        # Generate client data for record-keeping
        client_data = self.extract_client_info(customer_text + "\n" + response)
        formatted_client_data = self.format_client_data(client_data)
        
        self.client_data.delete("1.0", tk.END)
        self.client_data.insert(tk.END, formatted_client_data)
    
    def copy_to_clipboard(self):
        """Copy the generated response to clipboard"""
        response_text = self.generated_response.get("1.0", tk.END).strip()
        if response_text:
            self.root.clipboard_clear()
            self.root.clipboard_append(response_text)
            messagebox.showinfo("Copied", "Response copied to clipboard.")
        else:
            messagebox.showwarning("No Response", "No response to copy.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ResponseGenerator(root)
    root.mainloop()