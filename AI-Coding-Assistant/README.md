# AI Coding Assistant

Terminalden çalışan, OpenAI API destekli bir kod asistanı. Sohbet edebilir, proje
dosyalarını okuyabilir, onayınızla dosyaları düzenleyebilir ve komut çalıştırabilir.

## Gereksinimler

- Python 3.9+
- Bir OpenAI API key ([platform.openai.com/api-keys](https://platform.openai.com/api-keys))
- `/commit` özelliği için git

## Kurulum

```bash
pip install -r requirements.txt
cp .env.example .env
# .env dosyasına kendi OPENAI_API_KEY değerinizi girin
```

> `.env` dosyanız `.gitignore` ile korunur; API key'inizi asla commit etmeyin veya
> paylaşmayın.

## Kullanım

```bash
python -m ai_assistant.cli
```

veya paket olarak kurduysanız (`pip install -e .`):

```bash
aiassistant
```

Sohbeti bitirmek için `exit` veya `quit` yazın.

## Kısayol komutları

Sık kullanılan görevler için hazır komutlar:

- `/review [dosya/dizin]` — hata ve refactor önerileri sunar
- `/test <dosya>` — o dosya için test yazar ve çalıştırır
- `/docs [dosya/dizin]` — docstring/README dokümantasyonu oluşturur veya günceller
- `/commit` — git değişikliklerini inceler, bir commit mesajı önerir, onay sonrası commit atar
- `/help` — bu komut listesini gösterir

Bunların dışında istediğinizi normal cümlelerle de sorabilirsiniz.

## Nasıl çalışır

Asistan, OpenAI'ın tool-calling özelliğini kullanarak ihtiyaç duyduğunda şu araçları
çağırır:

- `list_files` — proje dizinini listeler
- `read_file` — bir dosyanın içeriğini okur
- `write_file` — bir dosyaya değişiklik önerir; **önce diff gösterir, onayınızı ister**
- `run_command` — bir terminal komutu çalıştırır; **önce onayınızı ister**
- `git_diff` — git değişikliklerini gösterir (salt okunur)
- `git_commit` — önerilen commit mesajını gösterir; **önce onayınızı ister**, onaylanırsa tüm değişiklikleri stage edip commit atar

Dosya yazma, komut çalıştırma ve commit atma işlemleri her zaman kullanıcı onayı gerektirir.

## Proje yapısı

```
ai_assistant/
├── cli.py            # REPL giriş noktası, kısayol komut ayrıştırma
├── commands.py       # /review, /test, /docs, /commit şablonları
├── config.py         # API key / model yapılandırması
├── openai_client.py  # Tool-calling agentic döngü
├── diff_utils.py      # Diff üretimi ve onay istemi
└── tools/
    ├── files.py       # list_files, read_file, write_file
    ├── shell.py       # run_command
    └── git.py         # git_diff, git_commit
```