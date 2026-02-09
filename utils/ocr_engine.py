import easyocr

reader = easyocr.Reader(['id','en'], gpu=False)

def run_ocr(image_path):
    results = reader.readtext(image_path, paragraph=True)
    text = "\n".join([res[1] for res in results])
    return text
