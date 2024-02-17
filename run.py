import subprocess
import sys

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar las dependencias: {e}")
        sys.exit(1)

def run_main_script():
    try:
        subprocess.check_call([sys.executable, 'server.py'])
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script principal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_dependencies()
    run_main_script()
