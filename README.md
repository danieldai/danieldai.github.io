# Daniel's Tech Blog

A modern, responsive tech blog built with Jekyll and Tailwind CSS, featuring search functionality, tags/categories, and GitHub Discussions-based comments.

## Features

- 🎨 **Modern Design**: Clean, responsive design with Tailwind CSS
- 🔍 **Full-Text Search**: Client-side search powered by Lunr.js
- 🏷️ **Tags & Categories**: Organize posts with tags and categories
- 💬 **Comments**: GitHub Discussions integration via Giscus
- 📱 **Mobile Responsive**: Optimized for all device sizes
- ⚡ **Fast Loading**: Static site generation with Jekyll
- 🚀 **GitHub Pages Ready**: Deploy directly to GitHub Pages

## Tech Stack

- **Jekyll 4.x**: Static site generator
- **Tailwind CSS 3.x**: Utility-first CSS framework
- **Lunr.js**: Client-side search engine
- **Giscus**: GitHub Discussions-based comments
- **GitHub Pages**: Hosting platform

## Quick Start

### Prerequisites

- Ruby 2.7+ (for Jekyll)
- Node.js 16+ (for Tailwind CSS)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/danieldai/danieldai.github.io.git
   cd danieldai.github.io
   ```

2. **Install Ruby dependencies**
   ```bash
   bundle install
   ```

3. **Install Node.js dependencies**
   ```bash
   npm install
   ```

4. **Build Tailwind CSS**
   ```bash
   npm run build-css-prod
   ```

5. **Start the development server**
   ```bash
   bundle exec jekyll serve
   ```

6. **Open your browser**
   Navigate to `http://localhost:4000`

## Development Workflow

### Writing Posts

1. Create a new file in `_posts/` with the format: `YYYY-MM-DD-post-title.md`
2. Add front matter to your post:

```yaml
---
layout: post
title: "Your Post Title"
date: 2024-01-15 10:00:00 +0000
categories: [Category1, Category2]
tags: [tag1, tag2, tag3]
author: "Your Name"
reading_time: 5
---

Your post content here...
```

### Styling Changes

1. **For development**: Run `npm run build-css` to watch for changes
2. **For production**: Run `npm run build-css-prod` to build minified CSS

### Adding Pages

1. Create `.html` or `.md` files in the root directory
2. Add front matter:

```yaml
---
layout: default
title: "Page Title"
permalink: /page-url/
---
```

## Configuration

### Site Settings (`_config.yml`)

Update the following settings in `_config.yml`:

```yaml
# Site information
title: "Your Blog Title"
description: "Your blog description"
author: "Your Name"
email: "your-email@example.com"
url: "https://yourusername.github.io"
baseurl: ""

# Navigation
navigation:
  - title: "Home"
    url: "/"
  - title: "About"
    url: "/about"
  # Add more navigation items
```

### Giscus Comments Setup

1. **Enable GitHub Discussions** on your repository
2. **Install Giscus** app on your GitHub account
3. **Get your repository ID**:
   ```bash
   curl -H "Accept: application/vnd.github.v3+json" \
        https://api.github.com/repos/yourusername/yourusername.github.io
   ```
4. **Get your category ID**:
   ```bash
   curl -H "Accept: application/vnd.github.v3+json" \
        https://api.github.com/repos/yourusername/yourusername.github.io/discussions/categories
   ```
5. **Update `_config.yml`**:
   ```yaml
   giscus:
     repo: "yourusername/yourusername.github.io"
     repo_id: "YOUR_REPO_ID"
     category: "General"
     category_id: "YOUR_CATEGORY_ID"
     # ... other settings
   ```

## Deployment

### GitHub Pages

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Initial blog setup"
   git push origin main
   ```

2. **Enable GitHub Pages**:
   - Go to repository Settings → Pages
   - Select "Deploy from a branch"
   - Choose "main" branch and "/ (root)" folder
   - Save

3. **Build CSS for production**:
   ```bash
   npm run build-css-prod
   git add assets/css/style.css
   git commit -m "Update CSS for production"
   git push origin main
   ```

### Custom Domain (Optional)

1. Add a `CNAME` file to the root directory with your domain
2. Configure DNS settings with your domain provider
3. Update `url` in `_config.yml`

## Cross-Platform Development

This blog is designed to work seamlessly on both Windows and macOS:

### Windows Setup

1. **Install Ruby** using RubyInstaller
2. **Install Node.js** from nodejs.org
3. **Use Git Bash** or Windows Subsystem for Linux for terminal commands

### macOS Setup

1. **Install Ruby** using Homebrew: `brew install ruby`
2. **Install Node.js** using Homebrew: `brew install node`
3. **Use Terminal** for all commands

## File Structure

```
danieldai.github.io/
├── _config.yml          # Jekyll configuration
├── _layouts/            # Page layouts
│   ├── default.html     # Base layout
│   ├── post.html        # Blog post layout
│   └── home.html        # Homepage layout
├── _includes/           # Reusable components
│   ├── header.html      # Site header
│   ├── footer.html      # Site footer
│   ├── post-card.html   # Post preview component
│   └── comments.html    # Comments component
├── _posts/              # Blog posts
├── assets/              # Static assets
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript files
│   └── images/         # Images
├── tags.html            # Tags page
├── categories.html      # Categories page
├── search.html          # Search page
├── about.md             # About page
├── 404.html             # 404 error page
├── Gemfile              # Ruby dependencies
├── package.json         # Node.js dependencies
└── tailwind.config.js   # Tailwind configuration
```

## Customization

### Colors and Styling

Edit `tailwind.config.js` to customize colors and theme:

```javascript
theme: {
  extend: {
    colors: {
      primary: {
        // Your custom color palette
      }
    }
  }
}
```

### Layout Modifications

- **Header**: Edit `_includes/header.html`
- **Footer**: Edit `_includes/footer.html`
- **Post Cards**: Edit `_includes/post-card.html`

### Adding Features

- **New Pages**: Create HTML/Markdown files in root directory
- **Custom Components**: Add to `_includes/` directory
- **Additional Styles**: Add to `assets/css/main.css`

## Troubleshooting

### Common Issues

1. **Jekyll serve fails**:
   ```bash
   bundle exec jekyll serve --trace
   ```

2. **CSS not updating**:
   - Run `npm run build-css` to rebuild styles
   - Clear browser cache

3. **Search not working**:
   - Check browser console for JavaScript errors
   - Ensure `search.json` is generated correctly

4. **Comments not showing**:
   - Verify Giscus configuration in `_config.yml`
   - Check if GitHub Discussions are enabled
   - Ensure repository is public

### Getting Help

- Check Jekyll documentation: https://jekyllrb.com/docs/
- Tailwind CSS docs: https://tailwindcss.com/docs
- Giscus documentation: https://giscus.app/

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy Blogging!** 🚀
