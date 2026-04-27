import os
import sys
import re

def get_md_files(root_dir):
    md_files = []
    # Dışarıda bırakılacak klasörler
    ignores = {'.git', '.venv', 'venv', 'node_modules', '__pycache__', 'assets'}
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Ignore listesindeki klasörleri atla
        dirnames[:] = [d for d in dirnames if d not in ignores]
        
        for file in filenames:
            if file.endswith('.md'):
                md_files.append(os.path.join(dirpath, file))
    return md_files

def remove_emojis_from_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Genişletilmiş Emoji Pattern (🎯, 🧱, 🔬, 🛠️ dahil tüm yeni nesil emojiler)
        emoji_pattern = re.compile(
            "["
            "\U0001F000-\U0001FAFF"  # Tüm modern emojiler ve semboller
            "\u2600-\u2B55"          # Çeşitli semboller ve dingbatlar
            "\ufe0f"                 # Emoji varyasyon seçiciler
            "\u200d"                 # Zero-width joiner (birleşik emojiler için)
            "]+",
            flags=re.UNICODE
        )

        # Sadece emojileri sil, boşluklara DOKUNMA
        content_final = emoji_pattern.sub('', content)

        # Sadece değişiklik varsa dosyaya yaz
        if content != content_final:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content_final)
            print(f"[TEMİZLENDİ] {filepath}")
            
    except Exception as e:
        print(f"[HATA] {filepath}: {e}")

if __name__ == "__main__":
    files_to_process = []
    
    if len(sys.argv) > 1:
        # Spesifik dosyalar verilmişse
        files_to_process = sys.argv[1:]
    else:
        # Parametre yoksa tüm repoyu tara
        print("Parametre verilmedi. Tüm repository (.md dosyaları) taranıyor...")
        files_to_process = get_md_files('.')
        print(f"Toplam {len(files_to_process)} adet .md dosyası bulundu. Temizlik başlıyor...\n")
        
    for filepath in files_to_process:
        remove_emojis_from_file(filepath)
    
    print("\nİşlem tamamlandı.")
