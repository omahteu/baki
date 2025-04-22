import speech_recognition as sr
import subprocess

def execute_command(command):
    """Executa comandos no sistema baseado no texto recebido."""
    try:
        if "abrir navegador" in command:            
            subprocess.run(["xdg-open", "https://www.google.com"])
            print("Abrindo o navegador...")        
        elif "mostrar arquivos" in command:
            subprocess.run(["nautilus", "--browser"])            
            print("Abrindo gerenciador de arquivos...")
        elif "desligar computador" in command:            
            subprocess.run(["shutdown", "now"])
            print("Desligando o computador...")        
        elif "atualizar emails" in command:
            subprocess.run(["xdg-open", "https://mail.google.com"])            
            print("Abrindo cliente de emails...")
        elif "abrir code" in command:            
            subprocess.run(["code"])
            print("Abrindo o Visual Studio Code...")        
        else:
            print("Comando não reconhecido:", command)    
    except Exception as e:
        print("Erro ao executar o comando:", e)
        
def capture_voice_command():    
    """Captura comandos de voz e os transforma em texto."""
    recognizer = sr.Recognizer()    
    with sr.Microphone() as source:
        print("Aguardando comando de voz...")        
        try:
            audio = recognizer.listen(source, timeout=10)            
            print("Reconhecendo...")
            command = recognizer.recognize_google(audio, language="pt-BR")            
            print("Você disse:", command)
            if command.lower().startswith("baki,"):                
                return command.lower().replace("baki,", "").strip()
            else:                
                print("Comando ignorado. Diga 'baki,' antes do comando.")
        except sr.UnknownValueError:            
            print("Não foi possível entender o áudio.")
        except sr.RequestError as e:            
            print("Erro ao conectar com o serviço de reconhecimento de fala:", e)
        except Exception as e:            
            print("Erro inesperado:", e)
        return None
    
if __name__ == "__main__":
    while True:
        command = capture_voice_command()        
        if command:
            execute_command(command)        
            print("\nDiga outro comando ou pressione Ctrl+C para sair.")
