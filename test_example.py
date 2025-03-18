import tkinter as tk
from response_generator import ResponseGenerator

def main():
    """Main function to demonstrate the response generator with a sample inquiry"""
    # Create the root window
    root = tk.Tk()
    app = ResponseGenerator(root)
    
    # Sample customer inquiry
    sample_inquiry = """
Dear Bartosz,

I hope this email finds you well. My name is John Smith and I represent ABC Sports, a distributor of sports equipment in Germany.

We are looking for custom water bottles for our upcoming sports event. We would need approximately 200 bottles with our logo printed on them. We are particularly interested in your BID009 model.

Could you please provide us with a quotation for 200 bottles with 2-color printing? Also, what is the minimum order quantity and delivery time?

Thank you for your assistance.

Best regards,
John Smith
Marketing Manager
ABC Sports
john.smith@abcsports.de
+49 123 456789
"""
    
    # Set the sample inquiry in the customer input text area
    app.customer_input.delete("1.0", tk.END)
    app.customer_input.insert(tk.END, sample_inquiry)
    
    # Set the response type to "Quotation Response"
    app.response_type.set("Quotation Response")
    
    # Generate the response
    app.generate_response()
    
    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()