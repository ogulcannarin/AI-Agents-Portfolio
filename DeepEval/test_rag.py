import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import FaithfulnessMetric, AnswerRelevancyMetric

def test_customer_support_rag():
    # 1. Senaryo Verileri (Normalde bu veriler uygulamanızdan gelir)
    input_query = "İade politikası nedir?"
    actual_output = "Ürünlerimizi 30 gün içerisinde fişinizle birlikte iade edebilirsiniz."
    retrieval_context = [
        "Şirketimiz, satın alma tarihinden itibaren 30 günlük bir iade süresi sunmaktadır.",
        "İade işlemleri için orijinal fiş veya fatura ibrazı zorunludur."
    ]

    # 2. Metriklerin Tanımlanması
    # Faithfulness: Yanıt, verilen kaynaklara (context) ne kadar sadık?
    faithfulness_metric = FaithfulnessMetric(threshold=0.7)
    
    # Relevancy: Yanıt, kullanıcının sorusuna ne kadar uygun?
    relevancy_metric = AnswerRelevancyMetric(threshold=0.7)

    # 3. Test Case Oluşturma
    test_case = LLMTestCase(
        input=input_query,
        actual_output=actual_output,
        retrieval_context=retrieval_context
    )

    # 4. Testi Çalıştırma ve Doğrulama
    assert_test(test_case, [faithfulness_metric, relevancy_metric])