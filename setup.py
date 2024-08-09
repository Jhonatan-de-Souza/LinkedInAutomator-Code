from cx_Freeze import setup, Executable
import sys

arquivos = ['linkedin_automator.ico']

# Target executable
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
    
configuracao = Executable(
    script='CustomTkinter-version.py',
    icon='linkedin_automator.ico',
    base=base
)


# Dependencies
build_exe_options = {
    "packages": ["customtkinter", "threading", "app"],  # Add your package dependencies here
    "includes": [],
    "include_files": [],  # Add any other files needed by your app here,
    "include_msvcr": True
}


setup(
    name="Linked Automator",
    version="1.0",
    description = 'Este programa automatiza a adição de novos contatos no LinkedIn',
    author = 'Jhonatan de Souza',
    options={"build_exe": build_exe_options},
    executables=[configuracao]  # Replace with your script name
)
