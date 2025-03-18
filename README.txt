# BIDONEX & ShakerX Automatic Response System

This system helps generate professional, polite, persuasive, and contextually appropriate responses to customer inquiries about BIDONEX and ShakerX products. All responses are based solely on the knowledge contained in the provided documents.

## Files Included

1. `company_info.txt` - Information about the company, including contact details, company description, sustainability commitment, and unique selling points.
2. `product_info.txt` - Information about BIDONEX and ShakerX products, including models, sizes, features, minimum order quantities, packaging, and shipping.
3. `pricing_info.txt` - Pricing information for all products, including pricing tiers, additional print costs, matrix fees, delivery costs, and sample costs.
4. `email_templates.txt` - Email templates for different scenarios, such as initial inquiry response, quotation response, sample request response, etc.
5. `response_guidelines.txt` - Guidelines for responding to customers, including general guidelines, key points to address, and client data collection.
6. `response_generator.py` - Python script that generates automatic responses based on the information in the text files.
7. `main.py` - Main script that serves as the entry point for the automatic response system.

## How to Use

1. Make sure all the files are in the same directory.
2. Run the `main.py` script:
   ```
   python main.py
   ```
3. The application will open with a user interface.
4. Paste the customer's inquiry in the "Customer Input" text area.
5. Select the appropriate response type from the dropdown menu.
6. Click the "Generate Response" button.
7. The generated response will appear in the "Generated Response" text area.
8. Client data for record-keeping will be displayed in the "Client Data for Record-Keeping" text area.
9. Click the "Copy to Clipboard" button to copy the generated response to the clipboard.
10. Paste the response in your email client to send it to the customer.

## Response Types

The system can generate responses for the following scenarios:

1. Initial Inquiry Response - For responding to initial inquiries about products.
2. Quotation Response - For providing quotations based on customer requirements.
3. Sample Request Response - For responding to sample requests.
4. Order Confirmation & Payment Details - For confirming orders and providing payment details.
5. Shipping Confirmation - For confirming that an order has been shipped.
6. Follow-up Email - For following up on previous communications.
7. Addressing Minimum Order Quantities - For explaining minimum order quantities.
8. Addressing Printing Options - For explaining printing options and costs.
9. Addressing Color Variations - For explaining color variations and solutions.

## Customizing Responses

The system automatically fills in some placeholders based on the customer's inquiry, such as the client's name, product model, quantity, and number of colors. However, you may need to manually edit the generated response to fill in other details or to make it more personalized.

## Client Data Collection

After each response, the system extracts and displays client data for record-keeping. This data includes:

- Email address
- Company name
- Contact person
- Country
- Product
- Quantity
- Number of colors
- Status
- Value
- Address
- VAT number
- Phone number
- Notes

You can copy this data and paste it into your client database or spreadsheet.

## Updating Information

If you need to update any information, such as pricing, product details, or email templates, you can edit the corresponding text files. The changes will be reflected in the generated responses the next time you run the application.