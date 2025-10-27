import customtkinter as ctk

def convert_temperature():
    try:
        temp = float(input_entry.get())
    except ValueError:
        temp = 0.0
    
    unit = selected_unit.get()

    f = c = k = 0

    if unit.startswith("C"):
        c = temp
        f = (temp * 9/5) + 32
        k = temp + 273.15
    elif unit.startswith("F"):
        c = (temp - 32) * 5/9
        k = c + 273.15
        f = temp
    elif unit.startswith("K"):
        c = temp - 273.15
        f = (c * 9/5) + 32
        k = temp
    
    c_value.configure(text=f"{c:.2f} °C")
    f_value.configure(text=f"{f:.2f} °F")
    k_value.configure(text=f"{k:.2f} K")

app = ctk.CTk()
app.title("Temperature Converter")
app.geometry("450x500")
app.minsize(450,500)
app._set_appearance_mode("dark")


app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)


main_frame = ctk.CTkFrame(app, fg_color="transparent")
main_frame.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)



# input Section

entry_label = ctk.CTkLabel(main_frame, text="Enter Temperature Value: ", font=("ComicNeue", 22, "bold"))
entry_label.grid(row=0, column=0, sticky="w", pady=(0, 5), columnspan=2)

input_entry = ctk.CTkEntry(main_frame, font=("Comic", 16))
input_entry.grid(row=1, column=0, sticky="ew", pady=(0, 15), columnspan=2)



# unit Section

unit_label = ctk.CTkLabel(main_frame, text="Select Original Value: ", font=("ComicNeue", 22, "bold"))
unit_label.grid(row=2, column=0, sticky="w", pady=(0, 10), columnspan=2)

# options

selected_unit = ctk.StringVar(value="Celcius")

radio_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
radio_frame.grid(row=3, column=0, sticky="w", columnspan=2, pady=(10, 20))

celcius_option = ctk.CTkRadioButton(radio_frame, text="Celcius", font=("ComicNeue", 18), variable=selected_unit, value="Celcius")
celcius_option.grid(row=0, column=0, padx=10)


fahrenheit_option = ctk.CTkRadioButton(radio_frame, text="Fahrenheit", font=("ComicNeue", 18), variable=selected_unit, value="Fahrenheit")
fahrenheit_option.grid(row=0, column=1, padx=10)


kelvin_option = ctk.CTkRadioButton(radio_frame, text="Kelvin", font=("ComicNeue", 18), variable=selected_unit, value="Kelvin")
kelvin_option.grid(row=0, column=2, padx=10)


# Convert button

convert_button = ctk.CTkButton(main_frame, text="Convert", font=("ComicNeue", 20, "bold"), corner_radius=10, command=convert_temperature)
convert_button.grid(row=4, column=0, pady=(10, 20), columnspan=2)

# Result Screen

result_label = ctk.CTkLabel(main_frame, text="Converted Temperatures: ", font=("ComicNeue", 22, "bold"))
result_label.grid(row=5, column=0, sticky="w", pady=(10, 20))


# Result frame 

result_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
result_frame.grid(row=6, column=0, sticky="ew", columnspan=2)

result_frame.grid_columnconfigure(0, weight=1)
result_frame.grid_columnconfigure(1, weight=1)


c_label = ctk.CTkLabel(result_frame, text="Celcius: ", font=("ComicNeue", 20, "bold"))
c_label.grid(row=0, column=0, sticky="w", pady=5)

c_value = ctk.CTkLabel(result_frame, text="0.0", font=("JetBrains Mono", 16))
c_value.grid(row=0, column=1, sticky="e", pady=5)



f_label = ctk.CTkLabel(result_frame, text="Fahrenheit: ", font=("ComicNeue", 20, "bold"))
f_label.grid(row=1, column=0, sticky="w", pady=5)

f_value = ctk.CTkLabel(result_frame, text="0.0", font=("JetBrains Mono", 16))
f_value.grid(row=1, column=1, sticky="e", pady=5)



k_label = ctk.CTkLabel(result_frame, text="Kelvin: ", font=("ComicNeue", 20, "bold"))
k_label.grid(row=2, column=0, sticky="w", pady=5)

k_value = ctk.CTkLabel(result_frame, text="0.0", font=("JetBrains Mono", 16))
k_value.grid(row=2, column=1, sticky="e", pady=5)


# Run app
app.mainloop()