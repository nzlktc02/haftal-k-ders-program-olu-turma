import sqlite3

# Veritabanı dosyasını oluştur veya bağlan
conn = sqlite3.connect('universite.db')
cursor = conn.cursor()

# Yazılım Mühendisliği Dersleri Tablosu (saat sütunu eklendi)
cursor.execute('''
CREATE TABLE IF NOT EXISTS yazilim_muh_dersler (
    ders_kodu TEXT PRIMARY KEY,
    ders_adi TEXT NOT NULL,
    donem INTEGER NOT NULL,
    akts INTEGER NOT NULL,
    ders_tipi TEXT NOT NULL,
    saat TEXT,
    ders_hocasi TEXT,
    ders_sekli TEXT
)
''')

# Bilgisayar Mühendisliği Dersleri Tablosu (saat sütunu eklendi)
cursor.execute('''
CREATE TABLE IF NOT EXISTS bilgisayar_muh_dersler (
    ders_kodu TEXT PRIMARY KEY,
    ders_adi TEXT NOT NULL,
    donem INTEGER NOT NULL,
    akts INTEGER NOT NULL,
    ders_tipi TEXT NOT NULL,
    saat TEXT,
    ders_hocasi TEXT,
    ders_sekli TEXT
)
''')

# Yazılım Mühendisliği Derslerini Ekleme (saat sütunu boş bırakıldı)
yazilim_dersler = [
    ("MAT110", "MATEMATİK I", 1, 5, "Zorunlu", 5, "Dr. Öğr. Üyesi Vildan YAZICI", "Örgün"),
    ("FIZ110", "FİZİK I", 1, 5, "Zorunlu", 5, "Dr. Öğr. Üyesi Saliha ELMAS", "Örgün"),
    ("YZM113", "BİLGİSAYAR PROGRAMLAMA-I", 1, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Ulaş VURAL", "Örgün"),
    ("YZM115", "BİLGİSAYAR LAB-I", 1, 3, "Zorunlu", 2, "Dr. Öğr. Üyesi Ulaş VURAL", "Örgün"),
    ("MAT127", "LİNEER CEBİR", 1, 3, "Zorunlu", 3, "Prof. Dr. Hüseyin Tarık DURU", "Örgün"),
    ("YZM119", "YAZILIM MÜHENDİSLİĞİNE GİRİŞ", 1, 3, "Zorunlu", 2, "Prof. Dr. Nevcihan DURU", "Örgün"),
    ("DİL100", "İNGİLİZCE", 1, 4, "Zorunlu", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("US001", "ÜNİVERSİTE SEÇMELİ DERS I", 1, 3, "Seçmeli", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("YZM122", "BİLGİSAYAR PROGRAMLAMA II", 2, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Ulaş VURAL", "Örgün"),
    ("FIZ120", "FİZİK II", 2, 5, "Zorunlu", 4, "Dr. Öğr. Üyesi Saliha ELMAS", "Örgün"),
    ("MAT120", "MATEMATİK II", 2, 5, "Zorunlu", 5, "Dr. Öğr. Üyesi Vildan YAZICI", "Örgün"),
    ("YZM117", "BİLGİSAYAR LAB-II", 2, 3, "Zorunlu", 2, "Dr. Öğr. Üyesi Ulaş VURAL", "Örgün"),
    ("YZM128", "WEB TEKNOLOJİLERİ", 2, 5, "Zorunlu", 2, "Dr. Öğr. Üyesi Mehmet KARA", "Örgün"),
    ("ATA100", "ATATÜRK İLKELERİ VE İNKILAP TARİHİ", 2, 4, "Zorunlu", 2, "Dr. Öğr. Üyesi İsmet KARADUMAN", "Uzaktan"),
    ("TUR100", "TÜRK DİLİ", 2, 4, "Zorunlu", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("MAT213", "AYRIK MATEMATİK", 3, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Vildan YAZICI", "Örgün"),
    ("YZM219", "YAZILIM GEREKSİNİM ANALİZİ", 3, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi Ercan ÖLÇER", "Örgün"),
    ("YZM224", "VERİTABANI YÖNETİM SİSTEMLERİ", 3, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi Fulya AKDENİZ", "Örgün"),
    ("YZM229", "NESNEYE YÖNELİK PROGRAMLAMA", 3, 5, "Zorunlu", 4, "Dr. Öğr. Üyesi Ulaş VURAL", "Örgün"),
    ("YZM127", "PROGRAMLAMA LAB- I", 3, 5, "Zorunlu", 2, "Dr. Öğr. Üyesi Fulya AKDENİZ", "Örgün"),
    ("US002", "ÜNİVERSİTE SEÇMELİ DERS II", 3, 3, "Seçmeli", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("US003", "ÜNİVERSİTE SEÇMELİ DERS III", 3, 3, "Seçmeli", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("YZM226", "YAZILIM TASARIMI", 4, 4, "Zorunlu", 2, "Dr. Öğr. Üyesi Ercan ÖLÇER", "Örgün"),
    ("YZM228", "PROGRAMLAMA LAB-II", 4, 5, "Zorunlu", 3, "Prof. Dr. Nevcihan DURU", "Örgün"),
    ("YZM317", "BİLGİSAYAR AĞLARI", 4, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi Mehmet KARA", "Örgün"),
    ("MAT224", "OLASILIK VE İSTATİSTİK", 4, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Vildan YAZICI", "Örgün"),
    ("YZM213", "VERİ YAPILARI", 4, 5, "Zorunlu", 4, "Dr. Öğr. Üyesi Fulya AKDENİZ", "Örgün"),
    ("YZMSTJ001", "STAJ I", 4, 4, "Zorunlu", None, "Dr. Öğr. Üyesi İsmet KARADUMAN", "Örgün"),
    ("US004", "ÜNİVERSİTE SEÇMELİ DERS IV", 4, 3, "Seçmeli", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("YZM319", "WEB PROGRAMLAMA", 5, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Fulya AKDENİZ", "Örgün"),
    ("YZM329", "YAZILIM TEST VE KALİTE", 5, 3, "Zorunlu", 3, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Örgün"),
    ("YZM335", "YAPAY ZEKA", 5, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi İsmet KARADUMAN", "Örgün"),
    ("MAT220", "SAYISAL YÖNTEMLER", 5, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Vildan YAZICI", "Örgün"),
    ("YZM326", "BİLGİSAYAR MİMARİSİ VE ORGANİZASYONU", 5, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU","Örgün"),
    ("S018", "ALAN SEÇMELİ DERS I", 5, 4, "Seçmeli", 3, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("YZM331", "YAZILIM LAB-I", 5, 4, "Zorunlu", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Örgün"),
    ("US005", "ÜNİVERSİTE SEÇMELİ DERS V", 5, 3, "Seçmeli", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("STJ002", "STAJ II", 6, 5, "Zorunlu", None, "Dr. Öğr. Üyesi İsmet KARADUMAN", "Örgün"),
    ("YZM411", "YAZILIM PROJE YÖNETİMİ", 6, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi Ercan ÖLÇER", "Örgün"),
    ("YZM312", "İŞLETİM SİSTEMLERİ", 6, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi İsmet KARADUMAN", "Örgün"),
    ("YZM330", "YAZILIM LAB- II", 6, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Örgün"),
    ("YZM332", "ALGORİTMA TASARIMI VE ANALİZİ", 6, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Örgün"),
    ("US006", "SEÇMELİ DERS VI", 6, 3, "Seçmeli", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("S019", "ALAN SEÇMELİ DERS II", 6, 4, "Seçmeli", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("YZM413", "İŞ SAĞLIĞI VE GÜVENLİĞİ-I", 7, 2, "Zorunlu", 3, "Prof. Dr. Hüseyin Tarık DURU", "Örgün"),
    ("YZM419", "BİÇİMSEL DİLLER VE OTOMATLAR", 7, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi Fulya AKDENİZ", "Örgün"),
    ("YZM417", "BİLGİ GÜVENLİĞİ", 7, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Fulya AKDENİZ", "Örgün"),
    ("YZM429", "ARAŞTIRMA PROBLEMLERİ", 7, 5, "Zorunlu", 4, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Örgün"),
    ("S020", "ALAN SEÇMELİ DERS III", 7, 4, "Seçmeli", 3, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("S021", "ALAN SEÇMELİ DERS IV", 7, 4, "Seçmeli", 3, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("US007", "ÜNİVERSİTE SEÇMELİ DERS VII", 7, 3, "Seçmeli", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("US008", "ÜNİVERSİTE SEÇMELİ DERS VIII", 7, 3, "Seçmeli", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("YZM426", "İŞ SAĞLIĞI VE GÜVENLİĞİ-II", 8, 2, "Zorunlu", 2, "Dr. Öğr. Üyesi İsmet KARADUMAN", "Örgün"),
    ("YZM430", "BİTİRME ÇALIŞMASI (BİTİRME TEZİ)", 8, 10, "Zorunlu", None, "Prof. Dr. Nevcihan DURU", "Örgün"),
    ("SMUH311", "BİLİŞİM ETİĞİ VE HUKUKU", 8, 4, "Zorunlu", 3, "Prof. Dr. Hüseyin Tarık DURU", "Uzaktan"),
    ("S022", "ALAN SEÇMELİ DERS V", 8, 4, "Seçmeli", 3, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("US009", "ÜNİVERSİTE SEÇMELİ DERS IX", 8, 3, "Seçmeli", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "Uzaktan"),
    ("US010", "ÜNİVERSİTE SEÇMELİ DERS X", 8, 3, "Seçmeli", 2,"Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU","Uzaktan")
]

cursor.executemany('INSERT OR IGNORE INTO yazilim_muh_dersler (ders_kodu, ders_adi, donem, akts, ders_tipi, saat, ders_hocasi, ders_sekli) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', yazilim_dersler)

# Updated Bilgisayar Mühendisliği Derslerini Ekleme (saat sütunu boş bırakıldı)
bilgisayar_dersler = [
    ("BLM111", "BİLGİSAYAR MÜHENDİSLİĞİNE GİRİŞ", 1, 3, "Zorunlu", 2, "Prof. Dr. Nevcihan DURU", "örgün"),
    ("MAT110", "MATEMATİK I", 1, 5, "Zorunlu", 5, "Dr. Öğr. Üyesi Vildan YAZICI", "örgün"),
    ("FİZ110", "FİZİK I", 1, 5, "Zorunlu", 5, "Dr. Öğr. Üyesi Saliha ELMAS", "örgün"),
    ("BLM112", "BİLGİSAYAR PROGRAMLAMA 1", 1, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Ulaş VURAL", "örgün"),
    ("BLM113", "BİLGİSAYAR LAB-I", 1, 3, "Zorunlu", 2, "Dr. Öğr. Üyesi Ulaş VURAL", "örgün"),
    ("MAT129", "LİNEER CEBİR", 1, 3, "Zorunlu", 4, "Prof. Dr. Hüseyin Tarık DURU", "örgün"),
    ("DİL100", "İNGİLİZCE", 1, 4, "Zorunlu", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "uzaktan"),
    ("US001", "ÜNİVERSİTE SEÇMELİ DERS I", 1, 3, "SEÇMELİ", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "uzaktan"),
    ("MAT120", "MATEMATİK II", 2, 5, "Zorunlu", 5, "Dr. Öğr. Üyesi Vildan YAZICI", "örgün"),
    ("FIZ120", "FİZİK II", 2, 5, "Zorunlu", 4, "Dr. Öğr. Üyesi Saliha ELMAS", "örgün"),
    ("BLM121", "BİLGİSAYAR LAB-II", 2, 3, "Zorunlu", 2, "Dr. Öğr. Üyesi Ulaş VURAL", "örgün"),
    ("BLM122", "BİLGİSAYAR PROGRAMLAMA II", 2, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Ulaş VURAL", "örgün"),
    ("ATA100", "ATATÜRK İLKELERİ VE İNKILAP TARİHİ", 2, 4, "SEÇMELİ", 2, "Dr. Öğr. Üyesi İsmet KARADUMAN", "uzaktan"),
    ("TUR100", "TÜRK DİLİ", 2, 4, "Zorunlu", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "uzaktan"),
    ("BLM125", "ELEKTRİK DEVRE TEMELLERİ", 2, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi Mehmet KARA", "örgün"),
    ("MAT211", "DİFERANSİYEL DENKLEMLER", 3, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Vildan YAZICI", "örgün"),
    ("BLM211", "NESNEYE YÖNELİK PROGRAMLAMA", 3, 5, "Zorunlu", 4, "Dr. Öğr. Üyesi Ulaş VURAL", "örgün"),
    ("BLM217", "PROGRAMLAMA LAB-I", 3, 5, "Zorunlu", 2, "Dr. Öğr. Üyesi Fulya AKDENİZ", "örgün"),
    ("BLM215", "TEMEL ELEKTRONİK VE UYGULAMALARI", 3, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Mehmet KARA", "örgün"),
    ("MAT213", "AYRIK MATEMATİK", 3, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Vildan YAZICI", "uzaktan"),
    ("BLM230", "VERİTABANI YÖNETİM SİSTEMLERİ", 3, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi Fulya AKDENİZ", "örgün"),
    ("US002", "ÜNİVERSİTE SEÇMELİ DERS II", 3, 3, "SEÇMELİ", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "uzaktan"),
    ("BLM226", "SAYISAL TASARIM VE UYGULAMALARI", 4, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Mehmet KARA", "örgün"),
    ("BLM232", "PROGRAMLAMA LAB - II", 4, 5, "Zorunlu", 3, "Prof. Dr. Nevcihan DURU", "örgün"),
    ("BLM317", "BİLGİSAYAR AĞLARI", 4, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi Mehmet KARA", "örgün"),
    ("BLM213", "VERİ YAPILARI", 4, 5, "Zorunlu", 4, "Dr. Öğr. Üyesi Fulya AKDENİZ", "örgün"),
    ("MAT224", "OLASILIK VE İSTATİSTİK", 4, 4, "SEÇMELİ", 3, "Dr. Öğr. Üyesi Vildan YAZICI", "uzaktan"),
    ("BLMSTJ001", "STAJ I", 4, 4, "Zorunlu", None, "Dr. Öğr. Üyesi İsmet KARADUMAN", "örgün"),
    ("US003", "ÜNİVERSİTE SEÇMELİ DERS III", 4, 3, "SEÇMELİ", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "uzaktan"),
    ("BLM313", "YAZILIM MÜHENDİSLİĞİ", 5, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi Ercan ÖLÇER", "örgün"),
    ("BLM315", "YAZILIM LAB-I", 5, 4, "Zorunlu", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "örgün"),
    ("MAT220", "SAYISAL YÖNTEMLER", 5, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Vildan YAZICI", "örgün"),
    ("BLM328", "BİLGİSAYAR MİMARİSİ VE ORGANİZASYONU", 5, 4, "Zorunlu", 3, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "örgün"),
    ("BLM321", "YAPAY ZEKA", 5, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi İsmet KARADUMAN", "örgün"),
    ("S018", "ALAN SEÇMELİ DERS I", 5, 4, "SEÇMELİ", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "örgün"),
    ("US004", "ÜNİVERSİTE SEÇMELİ DERS IV", 5, 3, "SEÇMELİ", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "uzaktan"),
    ("BLM320", "ALGORİTMA TASARIMI VE ANALİZİ", 6, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "örgün"),
    ("BLM311", "İŞLETİM SİSTEMLERİ", 6, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi İsmet KARADUMAN", "örgün"),
    ("BLM334", "YAZILIM LAB-II", 6, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "örgün"),
    ("BLMSTJ002", "STAJ II", 6, 5, "Zorunlu", None, "Dr. Öğr. Üyesi İsmet KARADUMAN", "örgün"),
    ("S019", "ALAN SEÇMELİ DERS II", 6, 4, "SEÇMELİ", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "örgün"),
    ("US006", "ÜNİVERSİTE SEÇMELİ DERS IV", 6, 3, "SEÇMELİ", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "uzaktan"),
    ("US005", "ÜNİVERSİTE SEÇMELİ DERS V", 6, 3, "SEÇMELİ", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "uzaktan"),
    ("BLM415", "ARAŞTIRMA PROBLEMLERİ", 7, 2, "Zorunlu", 3, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "örgün"),
    ("BLM417", "İŞ SAĞLIĞI VE GÜVENLİĞİ-I", 7, 2, "Zorunlu", 2, "Prof. Dr. Hüseyin Tarık DURU", "örgün"),
    ("BLM413", "BİÇİMSEL DİLLER VE OTOMATLAR", 7, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi Fulya AKDENİZ", "örgün"),
    ("S020", "ALAN SEÇMELİ DERS III", 7, 4, "SEÇMELİ", 3, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "örgün"),
    ("S021", "ALAN SEÇMELİ DERS IV", 7, 4, "SEÇMELİ", 3, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "örgün"),
    ("US008", "ÜNİVERSİTE SEÇMELİ DERS VIII", 7, 3, "SEÇMELİ", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "uzaktan"),
    ("BLM411", "PROGRAMLAMA DİLLERİ", 7, 5, "Zorunlu", 3, "Dr. Öğr. Üyesi Fulya AKDENİZ", "örgün"),
    ("US007", "ÜNİVERSİTE SEÇMELİ DERS VII", 7, 3, "SEÇMELİ", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "uzaktan"),
    ("BLM422", "BİTİRME ÇALIŞMASI (BİTİRME TEZİ)", 8, 10, "Zorunlu", None, "Prof. Dr. Nevcihan DURU", "örgün"),
    ("BLM426", "İŞ SAĞLIĞI VE GÜVENLİĞİ-II", 8, 2, "Zorunlu", 2, "Dr. Öğr. Üyesi İsmet KARADUMAN", "örgün"),
    ("BLM420", "BİLİŞİM ETİĞİ VE HUKUKU", 8, 4, "Zorunlu", 3, "Prof. Dr. Hüseyin Tarık DURU", "uzaktan"),
    ("BLMIMEI", "İŞLETMEDE MESLEKİ EĞİTİM", 8, 15, "Zorunlu", None, "Dr. Öğr. Üyesi İsmet KARADUMAN", "örgün"),
    ("S022", "ALAN SEÇMELİ DERS V", 8, 4, "SEÇMELİ", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "örgün"),
    ("S023", "ALAN SEÇMELİ DERS VI", 8, 4, "SEÇMELİ", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "örgün"),
    ("US009", "ÜNİVERSİTE SEÇMELİ DERS IX", 8, 3, "SEÇMELİ", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "uzaktan"),
    ("US010", "ÜNİVERSİTE SEÇMELİ DERS X", 8, 3, "SEÇMELİ", 2, "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU", "uzaktan")
]

# Inserting the data into the database
cursor.executemany('INSERT OR IGNORE INTO bilgisayar_muh_dersler (ders_kodu, ders_adi, donem, akts, ders_tipi, saat, ders_hocasi, ders_sekli) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', bilgisayar_dersler)

# Öğrenciler Tablosu
cursor.execute('''
CREATE TABLE IF NOT EXISTS ogrenciler (
    no INTEGER PRIMARY KEY,
    adi TEXT NOT NULL,
    sinif INTEGER NOT NULL,
    bolum TEXT NOT NULL,
    aldigi_dersler TEXT
)
''')

# Öğrenci Ekleme
students = [
    ('000000000', 'Kostü', 1, 'Bilgisayar', ''),
    ('1001', "Ahmet Yılmaz", 1, "Bilgisayar Mühendisliği", ""),
    ('1002', "Mehmet Demir", 1, "Yazılım Mühendisliği", ""),
    ('1003', "Zeynep Kaya", 1, "Bilgisayar Mühendisliği", ""),
    ('2001', "Elif Çelik", 2, "Yazılım Mühendisliği", ""),
    ('2002', "Mert Özkan", 2, "Bilgisayar Mühendisliği", ""),
    ('2003', "Deniz Aksoy", 2, "Yazılım Mühendisliği", ""),
    ('3001', "Burak Arslan", 3, "Bilgisayar Mühendisliği", ""),
    ('3002', "Hale Yıldırım", 3, "Yazılım Mühendisliği", ""),
    ('3003', "Berkay Şahin", 3, "Bilgisayar Mühendisliği", ""),
    ('4001', "Ece Doğan", 4, "Yazılım Mühendisliği", ""),
    ('4002', "Tuna Güneş", 4, "Bilgisayar Mühendisliği", ""),
    ('4003', "Gizem Sarı", 4, "Yazılım Mühendisliği", "")
]

# SQL sorgusu
sql = '''
    INSERT OR IGNORE INTO ogrenciler (no, adi, sinif, bolum, aldigi_dersler)
    VALUES (?, ?, ?, ?, ?)
'''

# Tüm öğrencileri tek seferde ekle
cursor.executemany(sql, students)


# Hocalar Tablosu (saat sütunu eklenmedi, çünkü hocaların ders saatleri ders tablolarında tutulacak)
cursor.execute('''
CREATE TABLE IF NOT EXISTS hocalar (
    hoca_no TEXT PRIMARY KEY,
    hoca_adi TEXT NOT NULL
)
''')

# Hocaları Ekleme
hocalar = [
    ("001", "Prof. Dr. Nevcihan DURU"),
    ("002", "Dr. Öğr. Üyesi Vildan YAZICI"),
    ("003", "Prof. Dr. Hüseyin Tarık DURU"),
    ("004", "Dr. Öğr. Üyesi Mehmet KARA"),
    ("005", "Dr. Öğr. Üyesi Ulaş VURAL"),
    ("006", "Dr. Öğr. Üyesi İsmet KARADUMAN"),
    ("007", "Dr. Öğr. Üyesi Ercan ÖLÇER"),
    ("008", "Dr. Öğr. Üyesi Elif Pınar HACIBEYOĞLU"),
    ("009", "Dr. Öğr. Üyesi Fulya AKDENİZ"),
    ("010", "Dr. Öğr. Üyesi Saliha ELMAS"),
    ("011", "Arş. Gör. Eray DURSUN"),
    ("012", "Arş. Gör. Candide ÖZTÜRK")
]

cursor.executemany('INSERT OR IGNORE INTO hocalar (hoca_no, hoca_adi) VALUES (?, ?)', hocalar)

# Admin Tablosu
cursor.execute('''
CREATE TABLE IF NOT EXISTS admin (
    kullanici_adi TEXT PRIMARY KEY,
    sifre TEXT NOT NULL
)
''')

# Admin Kayıtlarını Ekleme
admin_kullanicilar = [
    ("kostüadmin1", "Kostü123"),
    ("kostüadmin2", "Kostü1234")
]
cursor.executemany('INSERT OR IGNORE INTO admin (kullanici_adi, sifre) VALUES (?, ?)', admin_kullanicilar)

# Derslikler Tablosu
cursor.execute('''
CREATE TABLE IF NOT EXISTS derslikler (
    derslik_id TEXT PRIMARY KEY,
    kapasite INTEGER NOT NULL,
    statü TEXT NOT NULL
)
''')

# Derslikleri Ekleme
derslikler = [
    ("M101", 66, "NORMAL"),
    ("M201", 141, "NORMAL"),
    ("M301", 141, "NORMAL"),
    ("S101", 138, "NORMAL"),
    ("S201", 60, "NORMAL"),
    ("S202", 60, "NORMAL"),
    ("D101", 87, "NORMAL"),
    ("D102", 87, "NORMAL"),
    ("D103", 88, "NORMAL"),
    ("D104", 56, "NORMAL"),
    ("D201", 87, "NORMAL"),
    ("D202", 56, "NORMAL"),
    ("D301", 88, "NORMAL"),
    ("D302", 56, "NORMAL"),
    ("D401", 88, "NORMAL"),
    ("D402", 56, "NORMAL"),
    ("D403", 56, "NORMAL"),
    ("AMFİ A", 143, "NORMAL"),
    ("AMFİ B", 143, "NORMAL"),
    ("BİL.LAB 1", 40, "LAB"),
    ("BİL.LAB.2", 30, "LAB"),
    ("KÜÇÜK LAB", 20, "LAB")
]

cursor.executemany('INSERT OR IGNORE INTO derslikler (derslik_id, kapasite, statü) VALUES (?, ?, ?)', derslikler)

# Ortak Dersler Tablosu (saat sütunu eklendi)
cursor.execute('''
CREATE TABLE IF NOT EXISTS ortak_dersler (
    ders_kodu TEXT PRIMARY KEY,
    ders_adi TEXT NOT NULL,
    donem INTEGER NOT NULL,
    akts INTEGER NOT NULL,
    saat TEXT
)
''')

# Yazılım ve Bilgisayar Mühendisliği bölümlerindeki ortak dersleri bulup ortak_dersler tablosuna ekleyelim
cursor.execute('''
INSERT OR IGNORE INTO ortak_dersler (ders_kodu, ders_adi, donem, akts, saat)
SELECT yzm.ders_kodu, yzm.ders_adi, yzm.donem, yzm.akts, yzm.saat
FROM yazilim_muh_dersler yzm
LEFT JOIN bilgisayar_muh_dersler blm ON yzm.ders_kodu = blm.ders_kodu
WHERE yzm.ders_kodu NOT LIKE 'US%' AND yzm.ders_kodu NOT LIKE 'S%';

''')

# Üniversite Seçmeli Dersler Tablosu (saat sütunu eklendi)
cursor.execute('''
CREATE TABLE IF NOT EXISTS uni_secmeli_dersler (
    ders_kodu TEXT PRIMARY KEY,
    ders_adi TEXT NOT NULL,
    donem INTEGER NOT NULL,
    akts INTEGER NOT NULL,
    saat TEXT
)
''')

# Yazılım Mühendisliği bölümündeki üniversite seçmeli dersleri ekleyelim
cursor.execute('''
INSERT OR IGNORE INTO uni_secmeli_dersler (ders_kodu, ders_adi, donem, akts, saat)
SELECT DISTINCT ders_kodu, ders_adi, donem, akts, saat
FROM yazilim_muh_dersler
WHERE ders_kodu LIKE 'US%'
''')

# Bilgisayar Mühendisliği bölümündeki üniversite seçmeli dersleri ekleyelim (aynı kodlu olanlar zaten eklendiği için aynı kodu olanlar eklenmeyecek)
cursor.execute('''
INSERT OR IGNORE INTO uni_secmeli_dersler (ders_kodu, ders_adi, donem, akts, saat)
SELECT DISTINCT ders_kodu, ders_adi, donem, akts, saat
FROM bilgisayar_muh_dersler
WHERE ders_kodu LIKE 'US%'
''')

# Alan Seçmeli Dersler Tablosu (saat sütunu eklendi)
cursor.execute('''
CREATE TABLE IF NOT EXISTS alan_secmeli_dersler (
    ders_kodu TEXT PRIMARY KEY,
    ders_adi TEXT NOT NULL,
    donem INTEGER NOT NULL,
    akts INTEGER NOT NULL,
    saat TEXT
)
''')

# Yazılım Mühendisliği bölümündeki alan seçmeli dersleri ekleyelim
cursor.execute('''
INSERT OR IGNORE INTO alan_secmeli_dersler (ders_kodu, ders_adi, donem, akts, saat)
SELECT DISTINCT ders_kodu, ders_adi, donem, akts, saat
FROM yazilim_muh_dersler
WHERE ders_kodu LIKE 'S%'
''')

# Bilgisayar Mühendisliği bölümündeki alan seçmeli dersleri ekleyelim (aynı kodlu olanlar zaten eklendiği için aynı kodu olanlar eklenmeyecek)
cursor.execute('''
INSERT OR IGNORE INTO alan_secmeli_dersler (ders_kodu, ders_adi, donem, akts, saat)
SELECT DISTINCT ders_kodu, ders_adi, donem, akts, saat
FROM bilgisayar_muh_dersler
WHERE ders_kodu LIKE 'S%'
''')

# Veritabanına eklenen verileri kontrol etmek için sorgulama yapıyoruz
print("\nOrtak Dersler Tablosu:")
cursor.execute('SELECT * FROM ortak_dersler')
for ders in cursor.fetchall():
    print(ders)

print("\nÜniversite Seçmeli Dersler Tablosu:")
cursor.execute('SELECT * FROM uni_secmeli_dersler')
for ders in cursor.fetchall():
    print(ders)

print("\nAlan Seçmeli Dersler Tablosu:")
cursor.execute('SELECT * FROM alan_secmeli_dersler')
for ders in cursor.fetchall():
    print(ders)

# Değişiklikleri kaydet ve bağlantıyı kapat
conn.commit()
conn.close()

print("Tüm tablolar başarıyla oluşturuldu ve veriler eklendi.")