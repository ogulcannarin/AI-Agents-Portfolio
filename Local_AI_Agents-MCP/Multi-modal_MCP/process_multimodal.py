def process_multimodal_match(match_resource):
    print(f"Maç URI: {match_resource['uri']}")
    print(f"Skor: {match_resource['score']}")
    
    if match_resource['heatmap']:
        print(f"Heatmap görseli base64 formatında gönderildi ({len(match_resource['heatmap'])} karakter)")
    else:
        print("Heatmap yok")