FROM python:3.10-slim

WORKDIR /app

# Kütüphaneleri kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Dosyaları kopyala
COPY . .

# Streamlit Portunu Aç
EXPOSE 8501

# --- BURASI ÇOK ÖNEMLİ ---
# Eski "python main.py" komutunu SİL. Yerine bunu yaz:
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]