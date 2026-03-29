from typing import List, TypedDict

class GraphState(TypedDict):
    """
    Temsilci (Agent) durumunu tutan sözlük yapısı.
    """
    question: str
    documents: List[str]
    generation: str
    search_needed: str
    retry_count: int
