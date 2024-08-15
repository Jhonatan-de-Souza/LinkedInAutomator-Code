import customtkinter as ctk
from threading import Thread
from app import iniciar_automacao

# Initialize the CustomTkinter window
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("dark-blue")  

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Linked Automator")
        self.geometry("500x500")
        
        # Create UI elements
        self.label = ctk.CTkLabel(self, text="Qual profissão deseja buscar")
        self.label.pack(pady=10)
        
        self.palavra_chave = ctk.CTkEntry(self, width=400)
        self.palavra_chave.pack(pady=10)
        
        self.start_button = ctk.CTkButton(self, text="Iniciar Automação", command=self.start_automation)
        self.start_button.pack(pady=10)
        
        self.output_text = ctk.CTkTextbox(self, width=400, height=300)
        self.output_text.pack(pady=10)
    
    def start_automation(self):
        self.start_button.configure(state="disabled")
        palavra_chave = self.palavra_chave.get()
        self.write_output(f"Iremos buscar por: {palavra_chave}\n")
        self.start_button.configure(state="normal")
        thread = Thread(target=iniciar_automacao, daemon=True, args=(palavra_chave, self))
        thread.start()
    
    def write_output(self, text):
        self.output_text.insert("end", text)
        self.output_text.yview("end")  # Scroll to the end of the output

if __name__ == "__main__":
    app = App()
    app.mainloop()
