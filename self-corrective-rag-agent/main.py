from dotenv import load_dotenv
load_dotenv()

from graph import app
def run_agent(question: str):
    # Başlangıç durumu (Initial State)
    inputs = {"question": question, "documents": [], "retry_count": 0}
    
    # Grafı çalıştır ve her adımı (node) izle
    for output in app.stream(inputs):
        for key, value in output.items():
            print(f"\n---ADIM: {key}---")
            # Adım çıktılarını görmek için (isteğe bağlı):
            # print(value) 

    # Final cevabı yazdır
    print("\n" + "="*30)
    print(f"SORU: {question}")
    print(f"CEVAP: {value.get('generation', 'Cevap üretilemedi.')}")
    print("="*30)

# TEST SENARYOLARI
if __name__ == "__main__":
    # Senaryo A: Vektör DB'de olmayan güncel bir bilgi sor (Web Search tetiklensin)
    run_agent("2026 dünya kupası nerede oynanacak?")
    
    # Senaryo B: Çok spesifik ve bilinen bir şey sor (Direct RAG çalışsın)
    # run_agent("Python'da LangGraph nedir?")