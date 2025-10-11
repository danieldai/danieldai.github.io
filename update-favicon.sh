#!/bin/bash

# Favicon Generator Script for Jekyll Blog
# This script generates all necessary favicon formats from a source image
# Usage: ./update-favicon.sh [source-image] [output-directory]

set -e  # Exit on any error

# Default values
SOURCE_IMAGE="${1:-assets/icons/dai.png}"
OUTPUT_DIR="${2:-assets/icons}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if ImageMagick is installed
check_imagemagick() {
    if ! command -v magick &> /dev/null; then
        print_error "ImageMagick is not installed!"
        print_status "Installing ImageMagick via Homebrew..."
        
        if command -v brew &> /dev/null; then
            brew install imagemagick
            print_success "ImageMagick installed successfully!"
        else
            print_error "Homebrew is not installed. Please install ImageMagick manually."
            print_status "Visit: https://imagemagick.org/script/download.php"
            exit 1
        fi
    else
        print_success "ImageMagick is available"
    fi
}

# Check if source image exists
check_source_image() {
    if [[ ! -f "$SOURCE_IMAGE" ]]; then
        print_error "Source image '$SOURCE_IMAGE' not found!"
        print_status "Please provide a valid image file path."
        print_status "Usage: $0 [source-image] [output-directory]"
        exit 1
    fi
    print_success "Source image found: $SOURCE_IMAGE"
}

# Create output directory if it doesn't exist
create_output_dir() {
    if [[ ! -d "$OUTPUT_DIR" ]]; then
        print_status "Creating output directory: $OUTPUT_DIR"
        mkdir -p "$OUTPUT_DIR"
    fi
    print_success "Output directory ready: $OUTPUT_DIR"
}

# Generate favicon files
generate_favicons() {
    print_status "Generating favicon files from $SOURCE_IMAGE..."
    
    # Standard favicon sizes
    print_status "Creating standard favicons..."
    magick "$SOURCE_IMAGE" -resize 16x16 "$OUTPUT_DIR/favicon-16x16.png"
    magick "$SOURCE_IMAGE" -resize 32x32 "$OUTPUT_DIR/favicon-32x32.png"
    magick "$SOURCE_IMAGE" -resize 96x96 "$OUTPUT_DIR/favicon-96x96.png"
    
    # Apple Touch icon
    print_status "Creating Apple Touch icon..."
    magick "$SOURCE_IMAGE" -resize 180x180 "$OUTPUT_DIR/apple-touch-icon.png"
    
    # Android Chrome icons
    print_status "Creating Android Chrome icons..."
    magick "$SOURCE_IMAGE" -resize 192x192 "$OUTPUT_DIR/android-chrome-192x192.png"
    magick "$SOURCE_IMAGE" -resize 512x512 "$OUTPUT_DIR/android-chrome-512x512.png"
    
    # Multi-resolution favicon.ico
    print_status "Creating multi-resolution favicon.ico..."
    magick "$SOURCE_IMAGE" -resize 16x16 temp-16.png
    magick "$SOURCE_IMAGE" -resize 32x32 temp-32.png
    magick "$SOURCE_IMAGE" -resize 48x48 temp-48.png
    magick temp-16.png temp-32.png temp-48.png "$OUTPUT_DIR/favicon.ico"
    rm temp-16.png temp-32.png temp-48.png
    
    print_success "All favicon files generated successfully!"
}

# Update web app manifest
update_manifest() {
    local manifest_file="$OUTPUT_DIR/site.webmanifest"
    
    print_status "Updating web app manifest..."
    
    cat > "$manifest_file" << EOF
{
  "name": "Daniel's Tech Blog",
  "short_name": "Daniel's Blog",
  "icons": [
    {
      "src": "/assets/icons/android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/assets/icons/android-chrome-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "theme_color": "#ffffff",
  "background_color": "#ffffff",
  "display": "standalone"
}
EOF
    
    print_success "Web app manifest updated: $manifest_file"
}

# Update Jekyll layout file
update_layout() {
    local layout_file="_layouts/default.html"
    
    if [[ ! -f "$layout_file" ]]; then
        print_warning "Layout file not found: $layout_file"
        return
    fi
    
    print_status "Updating Jekyll layout file..."
    
    # Create backup
    cp "$layout_file" "$layout_file.backup"
    print_status "Backup created: $layout_file.backup"
    
    # Check if favicon section already exists
    if grep -q "<!-- Favicons -->" "$layout_file"; then
        print_warning "Favicon section already exists in layout file."
        print_status "Please manually update the favicon URLs in $layout_file"
        print_status "Or remove the existing favicon section and run this script again."
    else
        print_status "Adding favicon links to layout file..."
        
        # Find the position after {%- seo -%}
        if grep -q "{%- seo -%}" "$layout_file"; then
            # Insert favicon section after seo tag
            sed -i '' '/{%- seo -%}/a\
\
  <!-- Favicons -->\
  <link rel="shortcut icon" href="{{ '\''/assets/icons/favicon.ico'\'' | relative_url }}?v={{ site.time | date: '\''%Y%m%d%H%M%S'\'' }}">\
  <link rel="icon" type="image/x-icon" href="{{ '\''/assets/icons/favicon.ico'\'' | relative_url }}?v={{ site.time | date: '\''%Y%m%d%H%M%S'\'' }}">\
  <link rel="icon" type="image/png" sizes="16x16" href="{{ '\''/assets/icons/favicon-16x16.png'\'' | relative_url }}?v={{ site.time | date: '\''%Y%m%d%H%M%S'\'' }}">\
  <link rel="icon" type="image/png" sizes="32x32" href="{{ '\''/assets/icons/favicon-32x32.png'\'' | relative_url }}?v={{ site.time | date: '\''%Y%m%d%H%M%S'\'' }}">\
  <link rel="icon" type="image/png" sizes="96x96" href="{{ '\''/assets/icons/favicon-96x96.png'\'' | relative_url }}?v={{ site.time | date: '\''%Y%m%d%H%M%S'\'' }}">\
  <link rel="apple-touch-icon" sizes="180x180" href="{{ '\''/assets/icons/apple-touch-icon.png'\'' | relative_url }}?v={{ site.time | date: '\''%Y%m%d%H%M%S'\'' }}">\
  <link rel="manifest" href="{{ '\''/assets/icons/site.webmanifest'\'' | relative_url }}?v={{ site.time | date: '\''%Y%m%d%H%M%S'\'' }}">\
' "$layout_file"
            
            print_success "Favicon links added to layout file"
        else
            print_warning "Could not find {%- seo -%} tag in layout file"
            print_status "Please manually add the favicon links to your layout file"
        fi
    fi
}

# Show generated files
show_results() {
    print_status "Generated files:"
    echo ""
    ls -la "$OUTPUT_DIR"/*.png "$OUTPUT_DIR"/*.ico "$OUTPUT_DIR"/*.webmanifest 2>/dev/null | while read line; do
        echo "  $line"
    done
    echo ""
    print_success "Favicon update completed!"
}

# Show usage information
show_usage() {
    echo "Favicon Generator Script for Jekyll Blog"
    echo ""
    echo "Usage: $0 [source-image] [output-directory]"
    echo ""
    echo "Arguments:"
    echo "  source-image    Path to source image (default: assets/icons/dai.png)"
    echo "  output-directory Output directory for favicon files (default: assets/icons)"
    echo ""
    echo "Examples:"
    echo "  $0                                    # Use defaults"
    echo "  $0 logo.png                          # Use custom source image"
    echo "  $0 logo.png assets/favicons          # Use custom source and output directory"
    echo ""
    echo "This script will:"
    echo "  - Generate all necessary favicon formats"
    echo "  - Create/update web app manifest"
    echo "  - Update Jekyll layout file with favicon links"
    echo "  - Add cache-busting parameters"
}

# Main execution
main() {
    echo "🎨 Favicon Generator Script"
    echo "=========================="
    echo ""
    
    # Show usage if help requested
    if [[ "$1" == "-h" || "$1" == "--help" ]]; then
        show_usage
        exit 0
    fi
    
    print_status "Starting favicon generation..."
    print_status "Source image: $SOURCE_IMAGE"
    print_status "Output directory: $OUTPUT_DIR"
    echo ""
    
    # Run all steps
    check_imagemagick
    check_source_image
    create_output_dir
    generate_favicons
    update_manifest
    update_layout
    show_results
    
    echo ""
    print_status "Next steps:"
    echo "  1. Review the generated files"
    echo "  2. Test locally: bundle exec jekyll serve"
    echo "  3. Commit and push changes: git add . && git commit -m 'Update favicon' && git push"
    echo ""
}

# Run main function
main "$@"
