import os
import json
import urllib.request

# 
# simple pero efectivo para distribuciones pequeñas. Si necesitas algo más avanzado, 
# podrías usar herramientas como PyUpdater o implementar un mecanismo basado en Git.
# 
# PyUpdater - Git
#


SERVER_URL = "https://tu-servidor.com/actualizaciones/"
LOCAL_VERSION_FILE = "version.json"

def check_for_updates():
    try:
        # Descargar archivo de versión remota
        remote_version_url = SERVER_URL + "version.json"
        local_version = {}
        
        if os.path.exists(LOCAL_VERSION_FILE):
            with open(LOCAL_VERSION_FILE, "r") as f:
                local_version = json.load(f)

        remote_version = json.loads(urllib.request.urlopen(remote_version_url).read().decode())

        if remote_version["version"] > local_version.get("version", 0):
            print("Nueva versión encontrada. Descargando actualización...")
            for file in remote_version["files"]:
                urllib.request.urlretrieve(SERVER_URL + file, file)
            with open(LOCAL_VERSION_FILE, "w") as f:
                json.dump(remote_version, f)
            print("Actualización completada. Reinicia la aplicación.")

    except Exception as e:
        print(f"Error verificando actualizaciones: {e}")

if __name__ == "__main__":
    check_for_updates()
    # Aquí inicias la aplicación normalmente
    # Empecemos pues:
