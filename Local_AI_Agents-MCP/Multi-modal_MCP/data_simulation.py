import random
from PIL import Image, ImageDraw
from io import BytesIO
import base64

# Maç listesi (isteğe bağlı, basit)
matches = []

# Heatmap üret
def generate_heatmap_image():
    img = Image.new('RGB', (200, 100), color='white')
    draw = ImageDraw.Draw(img)
    for _ in range(20):
        x, y = random.randint(0, 199), random.randint(0, 99)
        draw.ellipse((x-3, y-3, x+3, y+3), fill='red')
    return img

def image_to_base64(img):
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode('utf-8')