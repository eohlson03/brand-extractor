# Website Brand Extractor

A Python tool that extracts branding elements (fonts, colors, and themes) from websites using Pyppeteer (Python port of Puppeteer).

## Features

- Extracts font families used in the website
- Identifies color schemes (hex, RGB, RGBA, and named colors)
- Analyzes visual themes and primary colors
- Generates a structured JSON output of branding elements
- Handles dynamically loaded content and styles using Pyppeteer
- Captures both external stylesheets and inline styles

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

Note: Pyppeteer will automatically download a compatible version of Chromium on first run.

## Usage

Run the script and enter a website URL when prompted:

```bash
python brand_extractor.py
```

The script will output a JSON object containing:
- Font families used in the website
- Color codes found in the CSS
- Primary colors based on usage frequency
- Overall color scheme
- List of stylesheets found (both external and inline)

## Example Output

```json
{
  "url": "https://example.com",
  "fonts": ["Arial", "Helvetica", "sans-serif"],
  "colors": ["#ffffff", "#000000", "rgb(255, 0, 0)"],
  "themes": {
    "primary_colors": ["#ffffff", "#000000"],
    "fonts": ["Arial", "Helvetica", "sans-serif"],
    "color_scheme": ["#ffffff", "#000000", "rgb(255, 0, 0)"]
  },
  "stylesheets": [
    "https://example.com/styles.css",
    "inline_style"
  ]
}
```

## Notes

- The script uses Pyppeteer to handle dynamic content and JavaScript-rendered styles
- It respects robots.txt and includes a proper User-Agent header
- Some websites may block automated access
- The analysis captures both static and dynamically loaded styles
- First run may take longer as it downloads Chromium 