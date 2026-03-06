<<<<<<< HEAD
import json
import csv
import os
import time
import random
import requests
from bs4 import BeautifulSoup

# === CONFIGURACIÓN ===
html_files = [f"{i}.html" for i in range(1, 20)]
csv_path = r"E:\mi_proyecto\piezas_lego.csv"
img_dir = r"E:\mi_proyecto\piezas"
os.makedirs(img_dir, exist_ok=True)

# === HEADERS (más realistas) ===
BASE_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) "
        "Gecko/20100101 Firefox/120.0"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Referer": "https://www.lego.com/es-es/service/bricks",
}

# === FUNCIÓN para descargar imagen con reintentos ===
def descargar_imagen(url, destino, intentos=3):
    tamanos = ["192x192", "400x400", "800x800"]  # prueba distintos tamaños
    for intento in range(intentos):
        try:
            # Variar el tamaño si hay patrón conocido
            for t in tamanos:
                if "192x192" in url:
                    test_url = url.replace("192x192", t)
                else:
                    test_url = url

                headers = BASE_HEADERS.copy()
                headers["Referer"] = f"https://www.lego.com/es-es/pdp/{random.randint(100000, 999999)}"

                response = requests.get(test_url, headers=headers, timeout=15, stream=True)
                if response.status_code == 200 and response.content:
                    with open(destino, "wb") as f:
                        for chunk in response.iter_content(1024):
                            f.write(chunk)
                    return True
                elif response.status_code == 404:
                    break  # no existe este tamaño, no insistas
            # Esperar antes de reintentar
            time.sleep(random.uniform(1.0, 3.0))
        except Exception as e:
            time.sleep(random.uniform(2.0, 4.0))
    return False

# === EXTRACCIÓN DE DATOS ===
productos = []
for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                data = json.loads(script.string)
                if isinstance(data, dict) and data.get("@type") == "ItemList":
                    for item in data["itemListElement"]:
                        sku = item.get("sku")
                        nombre = item.get("name")
                        imagen = item.get("image")
                        if sku and nombre and imagen:
                            productos.append({
                                "id": sku.strip(),
                                "descripcion": nombre.strip(),
                                "imagen": imagen.strip(),
                            })
            except Exception:
                continue

# === GUARDAR CSV ===
with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["id", "descripcion", "imagen"])
    writer.writeheader()
    writer.writerows(productos)

print(f"✅ CSV guardado en: {csv_path}")

# === DESCARGAR IMÁGENES ===
total = len(productos)
descargadas = 0
for i, producto in enumerate(productos, start=1):
    img_url = producto["imagen"]
    img_name = f"{producto['id']}.jpg"
    img_path = os.path.join(img_dir, img_name)

    if os.path.exists(img_path):
        print(f"🟢 ({i}/{total}) Ya existe: {img_name}")
        continue

    ok = descargar_imagen(img_url, img_path)
    if ok:
        descargadas += 1
        print(f"📸 ({i}/{total}) Imagen guardada: {img_name}")
    else:
        print(f"⚠️ ({i}/{total}) No se pudo descargar: {img_url}")

    # Esperar entre descargas para evitar bloqueo
    time.sleep(random.uniform(0.5, 1.5))

print(f"\n✅ Total productos: {len(productos)}")
print(f"📦 Imágenes descargadas: {descargadas}")
print(f"🗂️ Guardadas en: {img_dir}")
=======
import json
import csv
import os
import time
import random
import requests
from bs4 import BeautifulSoup

# === CONFIGURACIÓN ===
html_files = [f"{i}.html" for i in range(1, 20)]
csv_path = r"E:\mi_proyecto\piezas_lego.csv"
img_dir = r"E:\mi_proyecto\piezas"
os.makedirs(img_dir, exist_ok=True)

# === HEADERS (más realistas) ===
BASE_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) "
        "Gecko/20100101 Firefox/120.0"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Referer": "https://www.lego.com/es-es/service/bricks",
}

# === FUNCIÓN para descargar imagen con reintentos ===
def descargar_imagen(url, destino, intentos=3):
    tamanos = ["192x192", "400x400", "800x800"]  # prueba distintos tamaños
    for intento in range(intentos):
        try:
            # Variar el tamaño si hay patrón conocido
            for t in tamanos:
                if "192x192" in url:
                    test_url = url.replace("192x192", t)
                else:
                    test_url = url

                headers = BASE_HEADERS.copy()
                headers["Referer"] = f"https://www.lego.com/es-es/pdp/{random.randint(100000, 999999)}"

                response = requests.get(test_url, headers=headers, timeout=15, stream=True)
                if response.status_code == 200 and response.content:
                    with open(destino, "wb") as f:
                        for chunk in response.iter_content(1024):
                            f.write(chunk)
                    return True
                elif response.status_code == 404:
                    break  # no existe este tamaño, no insistas
            # Esperar antes de reintentar
            time.sleep(random.uniform(1.0, 3.0))
        except Exception as e:
            time.sleep(random.uniform(2.0, 4.0))
    return False

# === EXTRACCIÓN DE DATOS ===
productos = []
for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                data = json.loads(script.string)
                if isinstance(data, dict) and data.get("@type") == "ItemList":
                    for item in data["itemListElement"]:
                        sku = item.get("sku")
                        nombre = item.get("name")
                        imagen = item.get("image")
                        if sku and nombre and imagen:
                            productos.append({
                                "id": sku.strip(),
                                "descripcion": nombre.strip(),
                                "imagen": imagen.strip(),
                            })
            except Exception:
                continue

# === GUARDAR CSV ===
with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["id", "descripcion", "imagen"])
    writer.writeheader()
    writer.writerows(productos)

print(f"✅ CSV guardado en: {csv_path}")

# === DESCARGAR IMÁGENES ===
total = len(productos)
descargadas = 0
for i, producto in enumerate(productos, start=1):
    img_url = producto["imagen"]
    img_name = f"{producto['id']}.jpg"
    img_path = os.path.join(img_dir, img_name)

    if os.path.exists(img_path):
        print(f"🟢 ({i}/{total}) Ya existe: {img_name}")
        continue

    ok = descargar_imagen(img_url, img_path)
    if ok:
        descargadas += 1
        print(f"📸 ({i}/{total}) Imagen guardada: {img_name}")
    else:
        print(f"⚠️ ({i}/{total}) No se pudo descargar: {img_url}")

    # Esperar entre descargas para evitar bloqueo
    time.sleep(random.uniform(0.5, 1.5))

print(f"\n✅ Total productos: {len(productos)}")
print(f"📦 Imágenes descargadas: {descargadas}")
print(f"🗂️ Guardadas en: {img_dir}")
>>>>>>> 2052878031b42032dedad2deecdbf8d74fafb595
