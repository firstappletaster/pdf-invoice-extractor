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
