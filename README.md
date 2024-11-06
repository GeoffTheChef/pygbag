# Pygame Web Demo

A simple Pygame application demonstrating web deployment using Pygbag.

## Critical Web Deployment Notes

### Window Handling
When deploying Pygame games to web via Pygbag, there are important platform-specific considerations:

✅ **INSTEAD USE:**
```python
screen = pygame.display.set_mode((WIDTH, HEIGHT))
```

**Why?** The `pygame.RESIZABLE` flag causes a complete black screen in web deployment - breaking both rendering and input handling. While this works on desktop, it's incompatible with web/Pygbag deployment.

### Best Practices
1. Keep the base window size fixed
2. Let the web container handle scaling/resizing
3. Test platform-specific features carefully when targeting web deployment
4. Use platform detection for web-specific code:
```python
if sys.platform == "emscripten":
    import platform
    platform.window.canvas.style.imageRendering = "pixelated"
```

## Running the Project

### Local Development
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install pygame pygbag
python main.py
```

### Web Development
```bash
pygbag pygame_input_demo/
```

### Production Deployment
Uses GitHub Actions for automatic deployment to GitHub Pages.

## Project Structure
```
pygame_input_demo/
├── main.py          # Main game file
├── sfx/             # Sound effects (OGG format for web compatibility)
└── ...
```

