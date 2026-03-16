from data_simulation import generate_heatmap_image, image_to_base64
from mcp_resource import mcp_resource
from process_multimodal import process_multimodal_match

# Örnek maç
week = 3
match_id = 105
score = "5-2"

# Heatmap simülasyonu
heatmap_img = generate_heatmap_image()
heatmap_b64 = image_to_base64(heatmap_img)

# MCP resource template kullanımı
uri_template = "football://match/{week}/{match_id}"
resource = mcp_resource(uri_template, week, match_id, extras={"score": score, "heatmap": heatmap_b64})

# Multi-modal veri işleme
process_multimodal_match(resource)