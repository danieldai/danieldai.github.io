# Favicon Generator Script

This script automates the process of generating comprehensive favicon support for your Jekyll blog.

## Features

- 🎨 Generates all necessary favicon formats (16x16, 32x32, 96x96, 180x180, 192x192, 512x512)
- 📱 Creates Apple Touch icons for iOS devices
- 🤖 Creates Android Chrome icons for Android devices
- 🌐 Generates multi-resolution favicon.ico file
- 📄 Updates web app manifest for PWA support
- 🔗 Automatically updates Jekyll layout with favicon links
- 🚀 Adds cache-busting parameters to prevent browser caching
- 🛡️ Creates backups before modifying files

## Prerequisites

- ImageMagick (will be installed automatically via Homebrew if not present)
- Jekyll blog structure

## Usage

### Basic Usage
```bash
./update-favicon.sh
```
Uses default source image (`assets/icons/dai.png`) and output directory (`assets/icons`).

### Custom Source Image
```bash
./update-favicon.sh my-logo.png
```
Uses `my-logo.png` as source image with default output directory.

### Custom Source and Output Directory
```bash
./update-favicon.sh my-logo.png assets/favicons
```
Uses `my-logo.png` as source and outputs to `assets/favicons` directory.

### Help
```bash
./update-favicon.sh --help
```
Shows usage information and examples.

## What the Script Does

1. **Checks Dependencies**: Verifies ImageMagick is installed (installs via Homebrew if needed)
2. **Validates Input**: Checks if source image exists
3. **Creates Directory**: Creates output directory if it doesn't exist
4. **Generates Favicons**: Creates all necessary favicon formats:
   - `favicon-16x16.png`
   - `favicon-32x32.png`
   - `favicon-96x96.png`
   - `apple-touch-icon.png` (180x180)
   - `android-chrome-192x192.png`
   - `android-chrome-512x512.png`
   - `favicon.ico` (multi-resolution)
5. **Updates Manifest**: Creates/updates `site.webmanifest` for PWA support
6. **Updates Layout**: Adds favicon links to `_layouts/default.html` with cache-busting
7. **Shows Results**: Lists all generated files

## Generated Files

The script creates these files in the output directory:

```
assets/icons/
├── favicon-16x16.png
├── favicon-32x32.png
├── favicon-96x96.png
├── favicon.ico
├── apple-touch-icon.png
├── android-chrome-192x192.png
├── android-chrome-512x512.png
└── site.webmanifest
```

## Layout Integration

The script automatically adds these favicon links to your `_layouts/default.html`:

```html
<!-- Favicons -->
<link rel="shortcut icon" href="{{ '/assets/icons/favicon.ico' | relative_url }}?v={{ site.time | date: '%Y%m%d%H%M%S' }}">
<link rel="icon" type="image/x-icon" href="{{ '/assets/icons/favicon.ico' | relative_url }}?v={{ site.time | date: '%Y%m%d%H%M%S' }}">
<link rel="icon" type="image/png" sizes="16x16" href="{{ '/assets/icons/favicon-16x16.png' | relative_url }}?v={{ site.time | date: '%Y%m%d%H%M%S' }}">
<link rel="icon" type="image/png" sizes="32x32" href="{{ '/assets/icons/favicon-32x32.png' | relative_url }}?v={{ site.time | date: '%Y%m%d%H%M%S' }}">
<link rel="icon" type="image/png" sizes="96x96" href="{{ '/assets/icons/favicon-96x96.png' | relative_url }}?v={{ site.time | date: '%Y%m%d%H%M%S' }}">
<link rel="apple-touch-icon" sizes="180x180" href="{{ '/assets/icons/apple-touch-icon.png' | relative_url }}?v={{ site.time | date: '%Y%m%d%H%M%S' }}">
<link rel="manifest" href="{{ '/assets/icons/site.webmanifest' | relative_url }}?v={{ site.time | date: '%Y%m%d%H%M%S' }}">
```

## After Running the Script

1. **Test Locally**: `bundle exec jekyll serve`
2. **Commit Changes**: `git add . && git commit -m "Update favicon"`
3. **Deploy**: `git push origin master`

## Troubleshooting

- **ImageMagick not found**: The script will automatically install it via Homebrew
- **Layout file not found**: Make sure you're running the script from your Jekyll root directory
- **Permission denied**: Run `chmod +x update-favicon.sh` to make the script executable
- **Existing favicon section**: The script will warn you if favicon links already exist in your layout

## Tips

- Use high-resolution source images (at least 512x512) for best results
- The script creates backups of modified files (`.backup` extension)
- Cache-busting parameters ensure browsers load updated favicons
- Test in different browsers and devices to verify favicon display
