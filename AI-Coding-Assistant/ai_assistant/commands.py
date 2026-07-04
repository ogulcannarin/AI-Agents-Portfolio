"""CLI kısayol komutları (/review, /test, /docs, /commit) için hazır görev şablonları."""


def _review(arg: str) -> str:
    target = arg.strip() or "proje genelinde önemli dosyaları"
    return (
        f"{target} için kod incelemesi yap. Olası hataları, edge-case sorunlarını "
        "ve kod kalitesini etkileyen noktaları belirle. Bulduğun her sorun için "
        "kısa bir açıklama ver; net ve güvenli düzeltmeler için write_file ile "
        "değişiklik öner (kullanıcı onayı istenecek). Emin olmadığın konularda "
        "değişiklik yapmak yerine sadece öneri olarak belirt."
    )


def _test(arg: str) -> str:
    if not arg.strip():
        return (
            "Bir dosya adı belirtilmedi. Projeyi incele, test kapsamı eksik olan "
            "önemli bir modül bul ve o modül için testler yaz."
        )
    return (
        f"{arg.strip()} dosyası için kapsamlı testler yaz (uygun bir test "
        "framework'ü kullan, muhtemelen pytest). Testleri uygun bir test dosyasına "
        "(örn. test_<isim>.py) yaz, ardından run_command ile testleri çalıştır ve "
        "sonucu (geçti/kaldı) bana özetle."
    )


def _docs(arg: str) -> str:
    target = arg.strip() or "proje genelini"
    return (
        f"{target} için dokümantasyon oluştur/güncelle: eksik docstring'leri ekle "
        "ve gerekiyorsa README'yi güncelle. Değişiklikleri write_file ile öner "
        "(onay istenecek)."
    )


def _commit(arg: str) -> str:
    return (
        "Önce git_diff aracıyla mevcut değişiklikleri incele. Değişiklik yoksa "
        "bana bunu söyle ve başka bir şey yapma. Değişiklik varsa, Conventional "
        "Commits formatında (fix:/feat:/refactor:/docs:/test:) kısa ve açıklayıcı "
        "bir commit mesajı öner ve git_commit aracını bu mesajla çağır (kullanıcı "
        "onayı istenecek)."
    )


SLASH_COMMANDS = {
    "review": _review,
    "test": _test,
    "docs": _docs,
    "commit": _commit,
}

HELP_TEXT = """Kullanılabilir kısayol komutları:
  /review [dosya/dizin]  - hata ve refactor önerileri
  /test <dosya>          - test üretir ve çalıştırır
  /docs [dosya/dizin]    - dokümantasyon/docstring oluşturur
  /commit                - git diff'e bakıp commit mesajı önerir, onay sonrası commit atar
  /help                  - bu listeyi gösterir

Bunların dışında istediğin her şeyi normal cümlelerle de sorabilirsin."""
