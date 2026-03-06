import json
import csv
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# === CONFIGURACIÓN ===
html_files = ["1.html", "2.html", "3.html" ,"4.html", "5.html", "6.html", "7.html", "8.html", "9.html", "10.html", "11.html", "12.html", "13.html"]

# 📄 CSV en E:\mi_proyecto
csv_path = r"E:\mi_proyecto\piezas_lego.csv"

# 🖼️ Imágenes en E:\mi_proyecto\piezas
img_dir = r"E:\mi_proyecto\piezas"
os.makedirs(img_dir, exist_ok=True)

# === CONFIGURAR SELENIUM ===
options = Options()
options.add_argument("--headless")          # sin ventana
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

# === EXTRAER DATOS DESDE LOS HTML ===
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
                                "id": sku,
                                "descripcion": nombre,
                                "imagen": imagen
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
for i, producto in enumerate(productos, start=1):
    img_url = producto["imagen"]
    img_name = f"{producto['id']}.jpg"
    img_path = os.path.join(img_dir, img_name)

    try:
        driver.get(img_url)
        time.sleep(1)  # esperar carga
        # obtener bytes de la imagen desde el navegador
        img_data = driver.get_screenshot_as_png()
        # esto captura la vista del navegador (la imagen completa)
        with open(img_path, "wb") as f:
            f.write(img_data)
        print(f"📸 ({i}/{len(productos)}) Imagen descargada: {img_name}")
    except Exception as e:
        print(f"⚠️ Error descargando {img_url}: {e}")

driver.quit()

print(f"\n✅ Total productos: {len(productos)}")
print(f"🗂️ Imágenes guardadas en: {img_dir}")

