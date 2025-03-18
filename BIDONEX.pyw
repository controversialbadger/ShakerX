import math
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class BidonexCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Bidonex Calculator")
        self.root.geometry("800x1000")  # Increased height
        self.root.resizable(False, False)  # Fixed window size
        self.root.configure(bg='white')
        
        # Update colors for better contrast
        self.colors = {
            'bg': '#ffffff',
            'primary': '#1a237e',
            'secondary': '#303f9f',
            'accent': '#3949ab',
            'light': '#ffffff',
            'frame_bg': '#ffffff',
            'shadow': '#e1e5eb',
            'text': '#2c3e50',
            'border': '#dee2e6',
            'success': '#2ecc71',
            'error': '#e74c3c',
            'hover': '#e8f0fe'
        }

        
        self.root.configure(bg=self.colors['bg'])
        
        # Configure styles
        style = ttk.Style()
        style.configure('Card.TFrame',
                       background=self.colors['frame_bg'],
                       relief='solid',
                       borderwidth=1)
        
        style.configure('Container.TFrame',
                       background=self.colors['bg'])
        
        style.configure('Title.TLabel', 
                       background=self.colors['bg'],
                       foreground=self.colors['primary'],
                       font=('Segoe UI', 24, 'bold'),
                       padding=(0, 20))
        
        style.configure('Subtitle.TLabel',
                       background=self.colors['frame_bg'],
                       foreground=self.colors['text'],
                       font=('Segoe UI', 14),
                       padding=8)
        
        style.configure('Field.TLabel',
                       background=self.colors['frame_bg'],
                       foreground=self.colors['text'],
                       font=('Segoe UI', 12),
                       padding=(0, 8))
        
        style.configure('Custom.TEntry',
                       fieldbackground='white',
                       foreground=self.colors['text'],
                       font=('Segoe UI', 11),
                       relief='solid',
                       borderwidth=1)
        
        style.configure('Custom.TCombobox',
                       background='white',
                       fieldbackground='white',
                       foreground=self.colors['text'],
                       arrowcolor=self.colors['primary'],
                       font=('Segoe UI', 11),
                       relief='solid',
                       borderwidth=1)
        
        style.configure('Custom.TCheckbutton',
                       background=self.colors['frame_bg'],
                       foreground=self.colors['text'],
                       font=('Segoe UI', 12))
                       
        style.configure('RoundedButton.TButton',
                       padding=10,
                       relief='flat',
                       background=self.colors['accent'],
                       foreground='white',
                       font=('Segoe UI', 12, 'bold'))
        
        # Update main container frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=True, padx=30, pady=30)
        
        # Add hover effect method
        def add_hover_effect(entry_frame):
            def on_enter(e):
                if isinstance(entry_frame, tk.Frame):  # Only apply to tk.Frame widgets
                    entry_frame.configure(background=self.colors['hover'])
            def on_leave(e):
                if isinstance(entry_frame, tk.Frame):  # Only apply to tk.Frame widgets
                    entry_frame.configure(background=self.colors['border'])
            entry_frame.bind("<Enter>", on_enter)
            entry_frame.bind("<Leave>", on_leave)
            
        self.add_hover_effect = add_hover_effect
        self.create_widgets()
        



    def show_error(self, message):
        messagebox.showerror("Error", message, 
                            icon='error',
                            parent=self.root)

    def add_entry_effects(self, entry_frame):
        entry = entry_frame.winfo_children()[-1]  # Get the Entry widget
        def on_focus_in(e):
            if isinstance(entry_frame, tk.Frame):  # Only apply to tk.Frame widgets
                entry_frame.configure(background=self.colors['primary'])
        def on_focus_out(e):
            if isinstance(entry_frame, tk.Frame):  # Only apply to tk.Frame widgets
                entry_frame.configure(background=self.colors['border'])
        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

    def create_widgets(self):
        # Update main frame configuration
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=True, padx=5, pady=5)  # Reduced padding
        
        # Header with solid background
        header_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))
        
        gradient_canvas = tk.Canvas(header_frame, height=3, bg=self.colors['bg'], highlightthickness=0)
        gradient_canvas.pack(fill='x', pady=(0, 25))
        gradient_canvas.create_line(0, 1, gradient_canvas.winfo_reqwidth(), 1,
                              fill=self.colors['accent'], width=3, smooth=True)
        
        ttk.Label(header_frame, text="Bidonex Calculator", style='Title.TLabel').pack()
        ttk.Label(header_frame, text="Professional Pricing Solution", 
              style='Subtitle.TLabel', foreground=self.colors['secondary']).pack()

        # Main content card with shadow
        main_card = tk.Frame(self.main_frame, bg=self.colors['shadow'], bd=0)
        main_card.pack(fill='both', expand=True, padx=2, pady=2)
        main_card.update_idletasks()  # Force update
        
        content_frame = ttk.Frame(main_card, style='Card.TFrame', relief='raised', borderwidth=1)
        content_frame.pack(fill='both', expand=True, padx=5, pady=5)  # Reduced padding

        # Make the content frame scrollable
        canvas = tk.Canvas(content_frame, bg=self.colors['frame_bg'], highlightthickness=0, width=750)  # Set fixed width
        scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='Card.TFrame')

        def _on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        scrollable_frame.bind("<Configure>", _on_frame_configure)
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        # Create window in canvas
        canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=750)  # Set fixed width
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack scrollbar and canvas
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)






        # Update all widget parents from content_frame to scrollable_frame
        # Model selection with custom styling
        model_frame = tk.Frame(scrollable_frame, relief='solid', bd=1, bg='white')
        model_frame.pack(fill='x', padx=20, pady=20)
        
        ttk.Label(model_frame, text="Select Model", style='Field.TLabel', background='white').pack(anchor='w', padx=15, pady=10)
        
        model_entry_frame = tk.Frame(model_frame, background=self.colors['border'], relief='solid', bd=1)
        model_entry_frame.pack(fill='x', padx=15, pady=(0, 15))
        
        self.model_var = tk.StringVar()
        models = ["BID009", "BID011", "BID012", "BID013", "ShakerX 400 ml", "ShakerX 700 ml", 
              "ShakerX 400 ml 2 in 1", "ShakerX 700 ml 2 in 1"]
        model_combo = ttk.Combobox(model_entry_frame, textvariable=self.model_var, values=models, 
                              state='readonly', style='Custom.TCombobox', width=40)
        model_combo.pack(fill='x', padx=1, pady=1)
        model_combo.set(models[0])

        # Input fields in a grid layout
        input_grid = ttk.Frame(scrollable_frame, style='Card.TFrame')
        input_grid.pack(fill='x', padx=20, pady=20)
        input_grid.columnconfigure(0, weight=1, uniform='col')
        input_grid.columnconfigure(1, weight=1, uniform='col')
        input_grid.update_idletasks()  # Force update
        
        # Initialize StringVar instances with default values
        self.box_price_var = tk.StringVar(value="0.0")
        self.unit_count_var = tk.StringVar(value="0")
        self.additional_colour_count_var = tk.StringVar(value="0")
        self.additional_colour_price_var = tk.StringVar(value="0.0")
        
        fields = [
            ("Box Price (EUR)", self.box_price_var),
            ("Number of Units", self.unit_count_var),
            ("Additional Colors", self.additional_colour_count_var),
            ("Color Price (EUR/unit)", self.additional_colour_price_var)
        ]
        
        for i, (label, var) in enumerate(fields):
            field_frame = ttk.Frame(input_grid, style='Card.TFrame')
            field_frame.grid(row=i//2, column=i%2, padx=15, pady=15, sticky='nsew')
            
            ttk.Label(field_frame, text=label, style='Field.TLabel').pack(anchor='w', padx=15, pady=(10, 5))
            
            entry_frame = tk.Frame(field_frame, relief='solid', borderwidth=1, bg=self.colors['border'])  # Changed to tk.Frame
            entry_frame.pack(fill='x', padx=15, pady=(0, 15))
            
            entry = ttk.Entry(entry_frame, textvariable=var, style='Custom.TEntry')
            entry.pack(fill='x', padx=5, pady=5)
            self.add_hover_effect(entry_frame)
            self.add_entry_effects(entry_frame)
        
        input_grid.grid_columnconfigure(0, weight=1)
        input_grid.grid_columnconfigure(1, weight=1)
        
        # Add hover effects to model entry frame
        self.add_hover_effect(model_entry_frame)

        # Custom price section with improved styling
        custom_frame = tk.Frame(scrollable_frame, relief='solid', bd=1, bg='white')
        custom_frame.pack(fill='x', padx=20, pady=20)
        
        self.custom_price_check_var = tk.BooleanVar()
        custom_check = ttk.Checkbutton(custom_frame, text="Use Custom Price", 
                                  variable=self.custom_price_check_var,
                                  command=self.toggle_custom_price,
                                  style='Custom.TCheckbutton')
        custom_check.pack(side='left')
        
        custom_entry_frame = tk.Frame(custom_frame, background=self.colors['border'], relief='solid', bd=1)
        custom_entry_frame.pack(side='left', padx=(15, 0), fill='x', expand=True)
        self.add_hover_effect(custom_entry_frame)
        
        self.custom_price_var = tk.StringVar()
        self.custom_price_entry = ttk.Entry(custom_entry_frame, textvariable=self.custom_price_var,
                                      state='disabled', style='Custom.TEntry')
        self.custom_price_entry.pack(fill='x', padx=1, pady=1)
        self.add_entry_effects(custom_entry_frame)

        # Update button and result text configuration
        button_frame = ttk.Frame(scrollable_frame, style='Card.TFrame')
        button_frame.pack(fill='x', padx=20, pady=10)
        
        calc_button = tk.Button(button_frame, text="Calculate", command=self.calculate,
                      font=('Segoe UI', 13, 'bold'),
                      bg=self.colors['accent'],
                      fg='white',
                      activebackground=self.colors['secondary'],
                      activeforeground='white',
                      relief='raised',
                      borderwidth=1,
                      padx=50,
                      pady=12,
                      cursor='hand2')
        calc_button.pack(pady=10)

        def on_enter(e):
            calc_button['background'] = self.colors['secondary']

        def on_leave(e):
            calc_button['background'] = self.colors['accent']

        calc_button.bind("<Enter>", on_enter)
        calc_button.bind("<Leave>", on_leave)

        # Results section
        result_card = ttk.Frame(scrollable_frame, style='Card.TFrame')
        result_card.pack(fill='both', expand=True, padx=20, pady=10)
        
        ttk.Label(result_card, text="Calculation Results", 
              style='Subtitle.TLabel').pack(anchor='w', padx=20, pady=10)
        
        result_border = ttk.Frame(result_card, bg=self.colors['border'])
        result_border.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.result_text = tk.Text(result_border, height=10, width=50,
                          font=('Segoe UI', 12),
                          bg=self.colors['light'],
                          fg=self.colors['text'],
                          relief='flat',
                          padx=20, pady=15,
                          selectbackground=self.colors['accent'],
                          selectforeground='white',
                          insertbackground=self.colors['accent'],
                          wrap=tk.WORD)
        self.result_text.pack(fill='both', expand=True, padx=1, pady=1)



    def toggle_custom_price(self):
        if self.custom_price_check_var.get():
            self.custom_price_entry.config(state='normal')
        else:
            self.custom_price_entry.config(state='disabled')
            self.custom_price_var.set('')  # Clear the custom price when disabled

    def get_unit_price(self, model, unit_count):
        price_tiers = {
            "BID009": [(1500, float('inf'), 1.25),
                       (1200, 1500, 1.40), (800, 1199, 1.55), (400, 799, 1.70), 
                       (200, 399, 1.85), (100, 199, 2.00), (50, 99, 2.50)],
            "BID011": [(1500, float('inf'), 1.15),
                       (1200, 1500, 1.30), (800, 1199, 1.45), (400, 799, 1.60), 
                       (200, 399, 1.75), (100, 199, 1.90), (50, 99, 2.50)],
            "BID012": [(1500, float('inf'), 1.35),
                       (1200, 1500, 1.50), (800, 1199, 1.65), (400, 799, 1.80), 
                       (200, 399, 1.95), (100, 199, 2.10), (50, 99, 2.50)],
            "BID013": [(1500, float('inf'), 1.35),
                       (1200, 1500, 1.50), (800, 1199, 1.65), (400, 799, 1.80), 
                       (200, 399, 1.95), (100, 199, 2.10), (50, 99, 2.50)],
            "ShakerX 400 ml": [
                (60, 60, lambda c: 3.70 if c == 1 else (4.20 if c == 2 else 4.70)),
                (120, 120, lambda c: 3.50 if c == 1 else (4.00 if c == 2 else 4.50)),
                (180, 180, lambda c: 3.30 if c == 1 else (3.80 if c == 2 else 4.30)),
                (360, 360, lambda c: 3.20 if c == 1 else (3.70 if c == 2 else 4.20)),
                (660, 660, lambda c: 3.00 if c == 1 else (3.50 if c == 2 else 4.00)),
                (1260, 1260, lambda c: 2.70 if c == 1 else (3.20 if c == 2 else 3.70)),
                (1980, 1980, lambda c: 2.50 if c == 1 else (3.00 if c == 2 else 3.50)),
                (2880, 2880, lambda c: 2.20 if c == 1 else (2.70 if c == 2 else 3.20))
            ],
            "ShakerX 700 ml": [
                (56, 56, lambda c: 4.20 if c == 1 else (4.70 if c == 2 else 5.20)),
                (112, 112, lambda c: 4.00 if c == 1 else (4.50 if c == 2 else 5.00)),
                (168, 168, lambda c: 3.80 if c == 1 else (4.30 if c == 2 else 4.80)),
                (336, 336, lambda c: 3.70 if c == 1 else (4.20 if c == 2 else 4.70)),
                (616, 616, lambda c: 3.50 if c == 1 else (4.00 if c == 2 else 4.50)),
                (1176, 1176, lambda c: 3.20 if c == 1 else (3.70 if c == 2 else 4.20)),
                (1848, 1848, lambda c: 3.00 if c == 1 else (3.50 if c == 2 else 4.00)),
                (2688, 2688, lambda c: 2.70 if c == 1 else (3.20 if c == 2 else 3.70))
            ],
            "ShakerX 400 ml 2 in 1": [
                (48, 48, lambda c: 4.40 if c == 1 else (4.90 if c == 2 else 5.40)),
                (96, 96, lambda c: 4.20 if c == 1 else (4.70 if c == 2 else 5.20)),
                (144, 144, lambda c: 4.00 if c == 1 else (4.50 if c == 2 else 5.00)),
                (288, 288, lambda c: 3.90 if c == 1 else (4.40 if c == 2 else 4.90)),
                (528, 528, lambda c: 3.70 if c == 1 else (4.20 if c == 2 else 4.70)),
                (1008, 1008, lambda c: 3.40 if c == 1 else (3.90 if c == 2 else 4.40)),
                (1584, 1584, lambda c: 3.20 if c == 1 else (3.70 if c == 2 else 4.20)),
                (2304, 2304, lambda c: 2.90 if c == 1 else (3.40 if c == 2 else 3.90))
            ],
            "ShakerX 700 ml 2 in 1": [
                (48, 48, lambda c: 4.90 if c == 1 else (5.40 if c == 2 else 5.90)),
                (96, 96, lambda c: 4.70 if c == 1 else (5.20 if c == 2 else 5.70)),
                (144, 144, lambda c: 4.50 if c == 1 else (5.00 if c == 2 else 5.50)),
                (288, 288, lambda c: 4.40 if c == 1 else (4.90 if c == 2 else 5.40)),
                (528, 528, lambda c: 4.20 if c == 1 else (4.70 if c == 2 else 5.20)),
                (1008, 1008, lambda c: 3.90 if c == 1 else (4.40 if c == 2 else 4.90)),
                (1584, 1584, lambda c: 3.70 if c == 1 else (4.20 if c == 2 else 4.70)),
                (2304, 2304, lambda c: 3.40 if c == 1 else (3.90 if c == 2 else 4.40))
            ]        }
        
        # Dla produktów ShakerX
        if model.startswith("ShakerX"):
            # Znajdź wszystkie dostępne ilości dla danego modelu
            quantities = sorted([tier[0] for tier in price_tiers[model]])
            
            # Znajdź najbliższą większą lub równą ilość
            for qty in quantities:
                if unit_count <= qty:
                    # Znajdź odpowiednią cenę
                    for lower, upper, price in price_tiers[model]:
                        if lower == qty:
                            return price(1)  # Zakładamy 1 kolor jako domyślny
                    break
            
            # Jeśli ilość jest większa niż największa dostępna
            if unit_count > quantities[-1]:
                # Użyj ceny dla największej dostępnej ilości
                for lower, upper, price in price_tiers[model]:
                    if lower == quantities[-1]:
                        return price(1)
        
        # Dla pozostałych produktów (BID)
        else:
            for lower, upper, price in price_tiers[model]:
                if lower <= unit_count <= upper:
                    return price() if callable(price) else price
        
        return None

    def calculate(self):
        try:
            matrix_price = 18
            box_quantities = {
                "BID009": 110, "BID011": 140, "BID012": 120, "BID013": 100,
                "ShakerX 400 ml": {60: 1, 120: 2, 180: 3, 360: 6, 660: 11, 1260: 21, 1980: 33, 2880: 48},
                "ShakerX 700 ml": {56: 1, 112: 2, 168: 3, 336: 6, 616: 11, 1176: 21, 1848: 33, 2688: 48},
                "ShakerX 400 ml 2 in 1": {48: 1, 96: 2, 144: 3, 288: 6, 528: 11, 1008: 21, 1584: 33, 2304: 48},
                "ShakerX 700 ml 2 in 1": {48: 1, 96: 2, 144: 3, 288: 6, 528: 11, 1008: 21, 1584: 33, 2304: 48}            }
            max_quantities = {
                "ShakerX 400 ml": 2880,
                "ShakerX 700 ml": 2688,
                "ShakerX 400 ml 2 in 1": 2304,
                "ShakerX 700 ml 2 in 1": 2304            }

            model = self.model_var.get()
            box_price = float(self.box_price_var.get())
            unit_count = int(self.unit_count_var.get())
            additional_colour_count = int(self.additional_colour_count_var.get())

            standard_unit_price = self.get_unit_price(model, unit_count)
            if standard_unit_price is None:
                messagebox.showerror("Error", "Invalid unit price. Please check your inputs.")
                return

            if self.custom_price_check_var.get():
                if not self.custom_price_var.get():
                    self.show_error("Please enter a custom price.")
                    return
                try:
                    unit_price = float(self.custom_price_var.get())
                    savings = (standard_unit_price - unit_price) * unit_count
                    savings_text = f"\nSavings compared to standard price: {savings:.2f} EUR Net"
                except ValueError:
                    self.show_error("Invalid custom price value.")
                    return
            else:
                unit_price = standard_unit_price
                savings_text = ""

            # Adjust unit_count for ShakerX products before any calculations
            unit_count = unit_count  # Keep original input for reference
            if model in box_quantities and isinstance(box_quantities[model], dict):
                available_quantities = sorted(box_quantities[model].keys())
                # Find the smallest quantity that is greater than or equal to unit_count
                for qty in available_quantities:
                    if qty >= unit_count:
                        closest_quantity = qty
                        break
                else:
                    # If unit_count > max available quantity, round up to nearest multiple of max quantity
                    max_qty = available_quantities[-1]
                    multiplier = ((unit_count - 1) // max_qty) + 1
                    closest_quantity = max_qty * multiplier

                unit_count = closest_quantity  # Adjusted unit count
                box_count = box_quantities[model].get(closest_quantity)
                if not box_count:
                    # Calculate box count for quantities above the predefined ones
                    boxes_in_max_qty = box_quantities[model][available_quantities[-1]]
                    box_count = boxes_in_max_qty * multiplier
                matrix_count = 0  # No matrix cost for ShakerX products
            else:
                box_count = math.ceil(unit_count / box_quantities[model])
                matrix_count = additional_colour_count + 1

            # Calculate additional color charge with adjusted unit count
            additional_colour_charge = 0
            if additional_colour_count > 0:
                additional_colour_price = float(self.additional_colour_price_var.get())
                additional_colour_charge = additional_colour_count * unit_count * additional_colour_price

            delivery_cost = box_price * box_count
            total_cost = unit_count * unit_price + additional_colour_charge + matrix_price * matrix_count + delivery_cost

            # Clear previous results
            self.result_text.delete(1.0, tk.END)

            # Correctly calculate the total number of colors
            total_colours = additional_colour_count + 1

            # Format and display results
            result = f"""Model {model} ({unit_count} units) ({total_colours} color print)
{model} {unit_count} units x {unit_price:.2f} EUR = {unit_count * unit_price:.2f} EUR Net
"""
            if additional_colour_count > 0:
                result += f"Additional colors charge = {additional_colour_charge:.2f} EUR Net\n"

            if matrix_count > 0:
                result += f"Matrix for {matrix_count} colors = {matrix_price * matrix_count:.2f} EUR Net\n"

            result += f"""Delivery cost = {delivery_cost:.2f} EUR Net
Total cost = {total_cost:.2f} EUR Net{savings_text}"""

            self.result_text.insert(tk.END, result)

        except ValueError as e:
            self.show_error("Please enter valid numeric values.")
        except Exception as e:
            self.show_error(f"An error occurred: {str(e)}")

# Change the following line to prevent console window from opening
if __name__ == "__main__":
    root = tk.Tk()
    app = BidonexCalculator(root)
    root.mainloop()
