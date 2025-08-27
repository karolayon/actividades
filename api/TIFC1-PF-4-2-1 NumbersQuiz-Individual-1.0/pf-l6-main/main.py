import requests

def trivia_fetch(num):
    """
    Llama a la Numbers API para obtener trivia sobre un número
    y la traduce al español con LibreTranslate (si está disponible).
    """
    # 1. Pedimos trivia en inglés
    url = f"http://numbersapi.com/{num}?json"
    response = requests.get(url)
    data = response.json()

    texto_en = data.get("text", "No trivia found")
    texto_es = texto_en  # valor por defecto (por si la traducción falla)

    # 2. Intentamos traducir con LibreTranslate
    try:
        traduccion_url = "https://libretranslate.de/translate"
        payload = {
            "q": texto_en,
            "source": "en",
            "target": "es",
            "format": "text"
        }
        headers = {"Content-Type": "application/json"}
        trad_resp = requests.post(traduccion_url, json=payload, headers=headers, timeout=10)

        if trad_resp.status_code == 200:
            resp_json = trad_resp.json()
            if "translatedText" in resp_json:
                texto_es = resp_json["translatedText"]
    except Exception as e:
        print("⚠️ Error al traducir, se mostrará en inglés:", e)

    return {
        "number": data.get("number", num),
        "text": texto_es
    }

def main():
    print("¡Hola, alumnos!")  # en español
    
    numero = int(input("Ingresa un número para conocer un dato curioso: "))
    trivia = trivia_fetch(numero)
    print(f"\n🔢 Número: {trivia['number']}")
    print(f"📖 Dato curioso: {trivia['text']}")

if __name__ == "__main__":
    main()
