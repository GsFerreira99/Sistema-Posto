import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os","sys","ctypes"], "excludes": ["tkinter"], 'include_msvcr': True}

# base="Win32GUI" should be used only for Windows GUI app

setup(
    name = "Gerenciamento",
    version = "0.1",
    description = "Aplicação Teste!",
    options = {"build_exe": build_exe_options},
    data_files = [('Database', ['Database\caminho_db.txt']), ('', ['logo.ico'])],
    executables = [Executable(
    script="main.py",
    icon="logo.ico",
    base = "Win32GUI"
    )]
)