#!/usr/bin/env python3
"""Generate images using Google's Nano Banana (Gemini Image) API."""

import os
import sys
import base64
import argparse
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("ERROR: google-genai package required. Install with: pip install google-genai")
    sys.exit(1)

# Load API key from environment
API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

MODELS = {
    "pro": "gemini-3-pro-image-preview",      # Nano Banana Pro - high quality
    "flash": "gemini-2.5-flash-image",        # Nano Banana - fast/cheap
}

ASPECT_RATIOS = {
    "landscape": "16:9",
    "wide": "16:9",
    "portrait": "9:16",
    "square": "1:1",
    "cinematic": "21:9",
}

def generate_image(
    prompt: str,
    output_path: str = "generated_image.png",
    model: str = "pro",
    input_images: list[str] = None,
    aspect_ratio: str = "landscape",
) -> str:
    """Generate an image from a text prompt, optionally with reference images."""
    
    if not API_KEY:
        raise ValueError("Set GOOGLE_API_KEY or GEMINI_API_KEY in .env or environment")
    
    client = genai.Client(api_key=API_KEY)
    model_id = MODELS.get(model, model)
    
    # Resolve aspect ratio
    ar = ASPECT_RATIOS.get(aspect_ratio, aspect_ratio)
    
    # Build content list
    contents = []
    
    # Add input images if provided (for editing/reference)
    if input_images:
        for img_path in input_images:
            img_path = Path(img_path)
            if img_path.exists():
                mime = f"image/{img_path.suffix.lstrip('.').replace('jpg', 'jpeg')}"
                with open(img_path, "rb") as f:
                    contents.append(types.Part.from_bytes(data=f.read(), mime_type=mime))
    
    # Add text prompt
    contents.append(prompt)
    
    # Generate with aspect ratio
    response = client.models.generate_content(
        model=model_id,
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
            image_generation_config={"aspect_ratio": ar},
        ),
    )
    
    # Extract and save image
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            img_data = base64.b64decode(part.inline_data.data)
            output = Path(output_path)
            output.write_bytes(img_data)
            return str(output.absolute())
    
    raise RuntimeError("No image generated in response")


def main():
    parser = argparse.ArgumentParser(description="Generate images with Nano Banana API")
    parser.add_argument("prompt", help="Text prompt for image generation")
    parser.add_argument("-o", "--output", default="generated_image.png", help="Output path")
    parser.add_argument("-m", "--model", choices=["pro", "flash"], default="pro",
                        help="Model: 'pro' (high quality, default) or 'flash' (fast)")
    parser.add_argument("-a", "--aspect", default="landscape",
                        choices=["landscape", "portrait", "square", "cinematic", "wide"],
                        help="Aspect ratio (default: landscape)")
    parser.add_argument("-i", "--input", action="append", dest="inputs",
                        help="Input image(s) for editing/reference (can repeat)")
    
    args = parser.parse_args()
    
    try:
        path = generate_image(args.prompt, args.output, args.model, args.inputs, args.aspect)
        print(f"Image saved: {path}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
