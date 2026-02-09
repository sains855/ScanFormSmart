from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_angle_cls=True,
    lang='id'
)

def run_ocr(image_path):
    result = ocr.ocr(image_path, cls=True)

    texts = []
    for line in result[0]:
        texts.append(line[1][0])

    return "\n".join(texts)
