from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_core.output_parsers import StrOutputParser

# -------------------------------
# 1. Doküman Puanlayıcı Şeması
# -------------------------------
class GradeDocuments(BaseModel):
    """Dokümanların soruyla alakasını puanla."""
    
    binary_score: str = Field(
        description="Dokümanlar soruyla alakalı mı? 'yes' veya 'no'"
    )


# -------------------------------
# 2. Halüsinasyon Kontrol Şeması
# -------------------------------
class GradeHallucination(BaseModel):
    """Cevabın dokümanlara sadık olup olmadığını puanla."""
    
    binary_score: str = Field(
        description="Cevap dokümanlara dayanıyor mu? 'yes' veya 'no'"
    )


# -------------------------------
# 3. LLM Kurulumu
# -------------------------------
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)

# Structured output tanımları
structured_llm_grader = llm.with_structured_output(GradeDocuments)
hallucination_grader = llm.with_structured_output(GradeHallucination)


# -------------------------------
# 4. Doküman Değerlendirme Promptu
# -------------------------------
doc_grader_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Sen bir kalite kontrol uzmanısın. "
        "Gelen dokümanın kullanıcı sorusuna cevap verip vermediğini "
        "'yes' veya 'no' olarak puanla."
    ),
    (
        "human",
        "Doküman:\n{document}\n\nSoru:\n{question}"
    )
])

# Chain oluşturma
doc_grader_chain = doc_grader_prompt | structured_llm_grader


# -------------------------------
# 5. RAG Prompt
# -------------------------------
rag_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Sen uzman bir araştırmacısın. "
        "Aşağıdaki bağlamı (context) kullanarak soruya cevap ver. "
        "Eğer cevabı bilmiyorsan 'bilmiyorum' de. "
        "En fazla 3 cümle kullan."
    ),
    (
        "human",
        "Bağlam:\n{context}\n\nSoru:\n{question}"
    )
])

# RAG Chain
rag_chain = rag_prompt | llm | StrOutputParser()