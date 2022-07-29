from PIL import Image
from pathlib import Path
import base64
from io import BytesIO


def resize_image(length: int, width: int):
    base_path = Path(__file__).resolve().parents[1]
    file_path = (base_path / "charles.png").resolve()
    img = Image.open(file_path)
    new_img = img.resize((length, width))

    buffered = BytesIO()
    new_img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())
    img_url = 'data:image/png;base64,' + img_str.decode('ascii')
    return img_url
