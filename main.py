import os
import sys
import tkinter as tk
from response_generator import ResponseGenerator

def check_files():
    """Check if all required files exist"""
    required_files = [
        "company_info.txt",
        "product_info.txt",
        "pricing_info.txt",
        "email_templates.txt",
        "response_guidelines.txt"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    return missing_files

def main():
    """Main function to start the application"""
    # Check if all required files exist
    missing_files = check_files()
    if missing_files:
        print("Error: The following required files are missing:")
        for file in missing_files:
            print(f"- {file}")
        print("\nPlease make sure all required files are in the same directory as this script.")
        return
    
    # Start the application
    root = tk.Tk()
    app = ResponseGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()