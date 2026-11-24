import re
import fitz  # PyMuPDF


def pdf_metni_al(dosya_yolu: str) -> str:
    with fitz.open(dosya_yolu) as belge:
        return "\n".join(sayfa.get_text("text") for sayfa in belge)
def alanlari_ayikla(metin: str) -> dict:
    tarih = re.search(r"\b(\d{2}[./]\d{2}[./]\d{4})\b", metin)
    belge_no = re.search(
        r"(?:fatura\s*no|belge\s*no|invoice\s*(?:no|number)?)\s*[:#-]?\s*([A-Z0-9-]+)",
        metin,
        flags=re.IGNORECASE,
    )
    tutar = re.search(
        r"(?:genel\s*toplam|ödenecek\s*tutar|toplam)\s*[:=]?\s*(?:TL|₺|TRY|\$|€)?\s*(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2}))",
        metin,
        flags=re.IGNORECASE,
    )
return {
        "tarih": tarih.group(1) if tarih else None,
        "belge_no": belge_no.group(1) if belge_no else None,
        "tutar": tutar.group(1) if tutar else None,
    }
import os
import re
import fitz  # PyMuPDF
import pandas as pd


def pdf_metni_al(dosya_yolu: str) -> str:
    with fitz.open(dosya_yolu) as belge:
        return "\n".join(sayfa.get_text("text") for sayfa in belge)


def alanlari_ayikla(metin: str) -> dict:
    tarih = re.search(r"\b(\d{2}[./]\d{2}[./]\d{4})\b", metin)
    belge_no = re.search(
        r"(?:fatura\s*no|belge\s*no|invoice\s*(?:no|number)?)\s*[:#-]?\s*([A-Z0-9-]+)",
       metin,
        flags=re.IGNORECASE,
    )
    tutar = re.search(
        r"(?:genel\s*toplam|ödenecek\s*tutar|toplam)\s*[:=]?\s*(?:TL|₺|TRY|\$|€)?\s*(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2}))",
        metin,
        flags=re.IGNORECASE,
    )
    return {
        "tarih": tarih.group(1) if tarih else None,
        "belge_no": belge_no.group(1) if belge_no else None,
        "tutar": tutar.group(1) if tutar else None,
    }
    def klasoru_excele_aktar(klasor_yolu: str, cikti_dosyasi: str = "faturalar.xlsx") -> None:
    if not os.path.isdir(klasor_yolu):
        print(f"Klasör bulunamadı: {klasor_yolu}")
        return

    satirlar = []
    for dosya_adi in sorted(os.listdir(klasor_yolu)):
        if not dosya_adi.lower().endswith(".pdf"):
            continue

        tam_yol = os.path.join(klasor_yolu, dosya_adi)
        metin = pdf_metni_al(tam_yol)
        veri = alanlari_ayikla(metin)
        veri["dosya_adi"] = dosya_adi
        satirlar.append(veri)
        sutun_sirasi = ["dosya_adi", "tarih", "belge_no", "tutar"]
    df = pd.DataFrame(satirlar, columns=sutun_sirasi)
    df.to_excel(cikti_dosyasi, index=False)
    print(f"{len(satirlar)} fatura işlendi -> {cikti_dosyasi}")


if _name_ == "_main_":
    klasoru_excele_aktar("./ornek_faturalar", "faturalar.xlsx")
