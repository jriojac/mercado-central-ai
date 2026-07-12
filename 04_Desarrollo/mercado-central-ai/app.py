"""
Punto de entrada de la aplicación.

Será implementado durante el Hito correspondiente a la interfaz Streamlit.
"""

from src.ui.streamlit_app import StreamlitApp

def main():
    app = StreamlitApp()
    app.run()

if __name__ == "__main__":
    main()