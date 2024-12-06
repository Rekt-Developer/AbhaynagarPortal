import os
import json
import yaml
import shutil
from markdown import markdown
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from bs4 import BeautifulSoup
import re

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

def parse_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    parts = content.split('---', 2)
    if len(parts) == 3:
        front_matter = yaml.safe_load(parts[1])
        markdown_content = parts[2]
    else:
        front_matter = {}
        markdown_content = content
    
    html_content = markdown(markdown_content)
    
    return front_matter, html_content

def generate_html_from_template(template_name, context, output_path):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    html_content = template.render(context)
    
    soup = BeautifulSoup(html_content, 'html.parser')
    pretty_html = soup.prettify()
    
    create_file(output_path, pretty_html)

def create_base_template():
    template_content = """
<!DOCTYPE html>
<html lang="{% block lang %}en{% endblock %}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Abhaynagar Portal{% endblock %}</title>
    <meta name="description" content="{% block description %}A modern, SEO-optimized portal about Abhaynagar Upazila, Bangladesh{% endblock %}">
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link href="/assets/css/style.css" rel="stylesheet">
    {% block meta %}{% endblock %}
    <script src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
</head>
<body class="flex flex-col min-h-screen bg-gray-100 dark:bg-gray-900" x-data="{ darkMode: false }" :class="{ 'dark': darkMode }">
    <header class="bg-white dark:bg-gray-800 shadow-md">
        <nav class="container mx-auto px-6 py-3">
            <div class="flex justify-between items-center">
                <a href="/" class="text-2xl font-bold text-gray-800 dark:text-white">Abhaynagar Portal</a>
                <div class="flex space-x-4">
                    <a href="/" class="text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white">Home</a>
                    <a href="/news" class="text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white">News</a>
                    <button @click="darkMode = !darkMode" class="text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white">
                        <span x-show="!darkMode">🌙</span>
                        <span x-show="darkMode">☀️</span>
                    </button>
                    <select id="language-selector" class="bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-md text-gray-700 dark:text-gray-300">
                        <option value="en">English</option>
                        <option value="bn">বাংলা</option>
                    </select>
                </div>
            </div>
        </nav>
    </header>

    <main class="flex-grow container mx-auto px-6 py-8">
        {% block content %}{% endblock %}
    </main>

    <footer class="bg-white dark:bg-gray-800 shadow-md mt-12">
        <div class="container mx-auto px-6 py-4">
            <div class="flex justify-between items-center">
                <p class="text-gray-600 dark:text-gray-400">&copy; 2023 Abhaynagar Portal</p>
                <nav>
                    <a href="/tos" class="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white ml-4">Terms of Service</a>
                </nav>
            </div>
        </div>
    </footer>

    <script src="/assets/js/script.js"></script>
</body>
</html>
"""
    create_file('templates/base.html', template_content)

def create_index_template():
    template_content = """
{% extends 'base.html' %}

{% block title %}Abhaynagar Portal - Home{% endblock %}

{% block content %}
    <div class="mb-12">
        <h1 class="text-4xl font-bold mb-4 text-gray-900 dark:text-white">Welcome to Abhaynagar Portal</h1>
        <p class="text-xl text-gray-700 dark:text-gray-300">Explore the beauty and culture of Abhaynagar Upazila, Bangladesh</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-12">
        <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
            <h2 class="text-2xl font-semibold mb-4 text-gray-900 dark:text-white">Quick Facts</h2>
            <ul class="space-y-2 text-gray-700 dark:text-gray-300">
                <li><strong>Population:</strong> 290,143 (2022)</li>
                <li><strong>Area:</strong> 247.21 km²</li>
                <li><strong>Postal Code:</strong> 7460</li>
            </ul>
        </div>
        <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
            <h2 class="text-2xl font-semibold mb-4 text-gray-900 dark:text-white">Geography</h2>
            <p class="text-gray-700 dark:text-gray-300">Abhaynagar is located in the southwestern part of Bangladesh, known for its lush greenery and the Mukteshwari River.</p>
        </div>
        <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
            <h2 class="text-2xl font-semibold mb-4 text-gray-900 dark:text-white">Culture</h2>
            <p class="text-gray-700 dark:text-gray-300">Rich in Bengali culture, Abhaynagar is known for its traditional festivals, cuisine, and warm hospitality.</p>
        </div>
    </div>

    <div class="mb-12">
        <h2 class="text-3xl font-bold mb-6 text-gray-900 dark:text-white">Latest News</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {% for article in news_articles[:6] %}
                <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden">
                    {% if article.image %}
                        <img src="{{ article.image }}" alt="{{ article.title }}" class="w-full h-48 object-cover">
                    {% endif %}
                    <div class="p-6">
                        <h3 class="text-xl font-semibold mb-2 text-gray-900 dark:text-white">
                            <a href="{{ article.url }}" class="hover:text-blue-600 dark:hover:text-blue-400">{{ article.title }}</a>
                        </h3>
                        <p class="text-gray-700 dark:text-gray-300 mb-4">{{ article.description }}</p>
                        <p class="text-sm text-gray-600 dark:text-gray-400">{{ article.date }}</p>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
{% endblock %}

{% block meta %}
    <meta property="og:title" content="Abhaynagar Portal - Home">
    <meta property="og:description" content="Explore the beauty and culture of Abhaynagar Upazila, Bangladesh">
    <meta property="og:image" content="/assets/images/banner.jpg">
    <meta property="og:url" content="https://abhaynagar-portal.com">
    <meta property="og:type" content="website">
{% endblock %}
"""
    create_file('templates/index.html', template_content)

def create_news_template():
    template_content = """
{% extends 'base.html' %}

{% block title %}{{ title }} - Abhaynagar Portal{% endblock %}

{% block content %}
    <article class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-8">
        <h1 class="text-3xl font-bold mb-4 text-gray-900 dark:text-white">{{ title }}</h1>
        <p class="text-gray-600 dark:text-gray-400 mb-6">{{ date }}</p>
        {% if image %}
            <img src="{{ image }}" alt="{{ title }}" class="w-full h-64 object-cover rounded-lg mb-6">
        {% endif %}
        <div class="prose dark:prose-invert max-w-none">
            {{ content | safe }}
        </div>
    </article>
{% endblock %}

{% block meta %}
    <meta property="og:title" content="{{ title }} - Abhaynagar Portal">
    <meta property="og:description" content="{{ description }}">
    <meta property="og:image" content="{{ image }}">
    <meta property="og:url" content="https://abhaynagar-portal.com{{ url }}">
    <meta property="og:type" content="article">
{% endblock %}
"""
    create_file('templates/news_article.html', template_content)

def create_news_index_template():
    template_content = """
{% extends 'base.html' %}

{% block title %}News - Abhaynagar Portal{% endblock %}

{% block content %}
    <h1 class="text-3xl font-bold mb-8 text-gray-900 dark:text-white">Latest News</h1>
    
    <div class="mb-8">
        <label for="language-filter" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Filter by Language:</label>
        <select id="language-filter" class="block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500">
            <option value="all">All</option>
            <option value="en">English</option>
            <option value="bn">Bangla</option>
        </select>
    </div>

    <div id="news-container" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {% for article in news_articles %}
            <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden" data-language="{{ article.language }}">
                {% if article.image %}
                    <img src="{{ article.image }}" alt="{{ article.title }}" class="w-full h-48 object-cover">
                {% endif %}
                <div class="p-6">
                    <h2 class="text-xl font-semibold mb-2 text-gray-900 dark:text-white">
                        <a href="{{ article.url }}" class="hover:text-blue-600 dark:hover:text-blue-400">{{ article.title }}</a>
                    </h2>
                    <p class="text-gray-700 dark:text-gray-300 mb-4">{{ article.description }}</p>
                    <p class="text-sm text-gray-600 dark:text-gray-400">{{ article.date }}</p>
                </div>
            </div>
        {% endfor %}
    </div>

    <div id="pagination" class="mt-8 flex justify-center space-x-4">
        <!-- Pagination buttons will be dynamically inserted here -->
    </div>
{% endblock %}

{% block meta %}
    <meta property="og:title" content="News - Abhaynagar Portal">
    <meta property="og:description" content="Latest news and updates from Abhaynagar Upazila, Bangladesh">
    <meta property="og:image" content="/assets/images/banner.jpg">
    <meta property="og:url" content="https://abhaynagar-portal.com/news">
    <meta property="og:type" content="website">
{% endblock %}
"""
    create_file('templates/news_index.html', template_content)

def create_404_template():
    template_content = """
{% extends 'base.html' %}

{% block title %}404 Not Found - Abhaynagar Portal{% endblock %}

{% block content %}
    <div class="flex flex-col items-center justify-center h-full">
        <h1 class="text-4xl font-bold mb-4 text-gray-900 dark:text-white">404 - Page Not Found</h1>
        <p class="text-xl text-gray-700 dark:text-gray-300 mb-8">Oops! The page you're looking for doesn't exist.</p>
        <a href="/" class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Go Back Home
        </a>
    </div>
{% endblock %}
"""
    create_file('templates/404.html', template_content)

def create_tos_template():
    template_content = """
{% extends 'base.html' %}

{% block title %}Terms of Service - Abhaynagar Portal{% endblock %}

{% block content %}
    <h1 class="text-3xl font-bold mb-8 text-gray-900 dark:text-white">Terms of Service</h1>
    <div class="prose dark:prose-invert max-w-none">
        <h2>1. Acceptance of Terms</h2>
        <p>By accessing and using the Abhaynagar Portal, you agree to comply with and be bound by these Terms of Service.</p>

        <h2>2. Use of Content</h2>
        <p>All content provided on this website is for informational purposes only. You may not reproduce, distribute, or transmit any content without our prior written permission.</p>

        <h2>3. User Contributions</h2>
        <p>If you submit any content to our website, you grant us a non-exclusive, royalty-free license to use, modify, and distribute your content.</p>

        <h2>4. Privacy Policy</h2>
        <p>Your use of the Abhaynagar Portal is also governed by our Privacy Policy. Please review our Privacy Policy to understand our practices.</p>

        <h2>5. Disclaimer of Warranties</h2>
        <p>The Abhaynagar Portal is provided "as is" without any warranties, expressed or implied. We do not guarantee the accuracy or completeness of any information on our website.</p>

        <h2>6. Limitation of Liability</h2>
        <p>In no event shall Abhaynagar Portal be liable for any damages arising out of the use or inability to use the materials on our website.</p>

        <h2>7. Changes to Terms</h2>
        <p>We reserve the right to modify these Terms of Service at any time. Please check this page periodically for updates.</p>

        <h2>8. Contact Information</h2>
        <p>If you have any questions about these Terms, please contact us at info@abhaynagar-portal.com.</p>
    </div>
{% endblock %}

{% block meta %}
    <meta property="og:title" content="Terms of Service - Abhaynagar Portal">
    <meta property="og:description" content="Terms of Service for the Abhaynagar Portal website">
    <meta property="og:url" content="https://abhaynagar-portal.com/tos">
    <meta property="og:type" content="website">
{% endblock %}
"""
    create_file('templates/tos.html', template_content)

def create_css_file():
    css_content = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
@import url('https://fonts.maateen.me/kalpurush/font.css');

@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
    --font-inter: 'Inter', sans-serif;
    --font-kalpurush: 'Kalpurush', sans-serif;
}

body {
    font-family: var(--font-inter);
}

.bn {
    font-family: var(--font-kalpurush);
}

.prose img {
    @apply rounded-lg shadow-md;
}

.prose a {
    @apply text-blue-600 hover:text-blue-800 dark:text-blue-400 dark:hover:text-blue-200;
}

@media (prefers-color-scheme: dark) {
    body {
        @apply bg-gray-900 text-white;
    }
}
"""
    create_file('assets/css/style.css', css_content)

def create_js_file():
    js_content = """
// Dark mode toggle
document.addEventListener('alpine:init', () => {
    Alpine.store('darkMode', {
        on: false,
        toggle() {
            this.on = !this.on;
            document.documentElement.classList.toggle('dark');
        }
    });
});

// News filtering and pagination
document.addEventListener('DOMContentLoaded', (event) => {
    const languageFilter = document.getElementById('language-filter');
    const newsContainer = document.getElementById('news-container');
    const paginationContainer = document.getElementById('pagination');
    const articlesPerPage = 9;
    let currentPage = 1;

    if (languageFilter && newsContainer) {
        languageFilter.addEventListener('change', filterNews);
        filterNews();
    }

    function filterNews() {
        const selectedLanguage = languageFilter.value;
        const articles = newsContainer.querySelectorAll('[data-language]');
        let visibleArticles = [];

        articles.forEach(article => {
            if (selectedLanguage === 'all' || article.dataset.language === selectedLanguage) {
                article.style.display = '';
                visibleArticles.push(article);
            } else {
                article.style.display = 'none';
            }
        });

        updatePagination(visibleArticles);
    }

    function updatePagination(visibleArticles) {
        const pageCount = Math.ceil(visibleArticles.length / articlesPerPage);
        paginationContainer.innerHTML = '';

        for (let i = 1; i <= pageCount; i++) {
            const button = document.createElement('button');
            button.innerText = i;
            button.classList.add('px-3', 'py-1', 'bg-blue-600', 'text-white', 'rounded');
            button.addEventListener('click', () => changePage(i, visibleArticles));
            paginationContainer.appendChild(button);
        }

        changePage(1, visibleArticles);
    }

    function changePage(page, visibleArticles) {
        currentPage = page;
        const start = (page - 1) * articlesPerPage;
        const end = start + articlesPerPage;

        visibleArticles.forEach((article, index) => {
            if (index >= start && index < end) {
                article.style.display = '';
            } else {
                article.style.display = 'none';
            }
        });
    }
});
"""
    create_file('assets/js/script.js', js_content)

def create_sitemap(news_articles):
    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://abhaynagar-portal.com/</loc>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://abhaynagar-portal.com/news</loc>
        <changefreq>daily</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://abhaynagar-portal.com/tos</loc>
        <changefreq>monthly</changefreq>
        <priority>0.3</priority>
    </url>
    {% for article in news_articles %}
    <url>
        <loc>https://abhaynagar-portal.com{{ article.url }}</loc>
        <lastmod>{{ article.date }}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.6</priority>
    </url>
    {% endfor %}
</urlset>"""
    env = Environment(loader=FileSystemLoader('.'))
    template = env.from_string(sitemap_content)
    xml_content = template.render({'news_articles': news_articles})
    create_file('sitemap.xml', xml_content)

def create_robots_txt():
    robots_content = """User-agent: *
Allow: /
Disallow: /private/

Sitemap: https://abhaynagar-portal.com/sitemap.xml"""
    create_file('robots.txt', robots_content)

def create_404_page():
    generate_html_from_template('404.html', {}, '404.html')

def create_tos_page():
    generate_html_from_template('tos.html', {}, 'tos.html')

def create_readme():
    readme_content = """# Abhaynagar Portal

A modern, SEO-optimized portal about Abhaynagar Upazila, Bangladesh. Featuring news, history, demographics, and more.

## Features

- Responsive design using Tailwind CSS
- Dynamic news fetching from Markdown files
- Bilingual support (Bangla and English)
- SEO optimization with structured data
- Dark mode support

## Getting Started

1. Clone this repository
2. Run the build script: `python create_portal.py`
3. Serve the generated static files using a web server of your choice

## Deploying to GitHub Pages

1. Push the generated static files to the `main` branch
2. Enable GitHub Pages in your repository settings
3. Set the source to the `main` branch and the root directory

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
"""
    create_file('README.md', readme_content)

def create_sample_news_article():
    news_content = """---
title: "New Community Center Opens in Abhaynagar"
description: "A state-of-the-art community center has been inaugurated in Abhaynagar, providing a space for local events and gatherings."
date: "2023-06-15"
image: "/assets/images/community-center.jpg"
language: "en"
---

# New Community Center Opens in Abhaynagar

Abhaynagar, Bangladesh - June 15, 2023

A new state-of-the-art community center has been officially opened in Abhaynagar, marking a significant milestone for the local community. The center, which has been in development for the past two years, aims to provide a modern space for various community events, educational programs, and social gatherings.

## Features of the New Community Center

The newly inaugurated community center boasts several impressive features:

1. **Multipurpose Hall**: A large hall that can accommodate up to 500 people for events such as weddings, conferences, and cultural programs.
2. **Library**: A well-stocked library with both Bengali and English books, as well as digital resources.
3. **Computer Lab**: A modern computer lab with high-speed internet access, providing digital literacy opportunities for the local community.
4. **Sports Facilities**: Indoor sports facilities including table tennis and badminton courts.
5. **Green Spaces**: Beautifully landscaped gardens and outdoor seating areas for relaxation and small gatherings.

## Community Impact

The opening of this new center is expected to have a significant positive impact on the Abhaynagar community. Local resident Fatima Begum expressed her excitement, saying, "This center will be a great place for our children to learn and for our community to come together. We're very grateful for this new addition to our upazila."

## Future Plans

Local authorities have announced plans to organize regular events and programs at the community center, including:

- Weekly computer literacy classes for seniors
- Monthly health awareness seminars
- Seasonal cultural festivals celebrating local traditions

The community center is now open to the public, and residents are encouraged to visit and make use of its facilities. For more information on upcoming events and how to book the space for community activities, please visit the Abhaynagar Upazila official website.
"""
    create_file('news/community-center-opens.md', news_content)

def create_portal():
    # Create directory structure
    create_directory('assets/css')
    create_directory('assets/js')
    create_directory('assets/images')
    create_directory('news')
    create_directory('templates')

    # Create template files
    create_base_template()
    create_index_template()
    create_news_template()
    create_news_index_template()
    create_404_template()
    create_tos_template()

    # Create sample news article
    create_sample_news_article()

    # Process news articles
    news_articles = []
    for filename in os.listdir('news'):
        if filename.endswith('.md'):
            file_path = os.path.join('news', filename)
            front_matter, html_content = parse_markdown_file(file_path)
            
            output_path = f"news/{filename.replace('.md', '.html')}"
            generate_html_from_template('news_article.html', {
                'title': front_matter.get('title', ''),
                'date': front_matter.get('date', ''),
                'description': front_matter.get('description', ''),
                'image': front_matter.get('image', ''),
                'content': html_content,
                'url': f"/news/{filename.replace('.md', '.html')}"
            }, output_path)
            
            news_articles.append({
                'title': front_matter.get('title', ''),
                'date': front_matter.get('date', ''),
                'description': front_matter.get('description', ''),
                'image': front_matter.get('image', ''),
                'url': f"/news/{filename.replace('.md', '.html')}",
                'language': front_matter.get('language', 'en')
            })

    # Sort news articles by date
    news_articles.sort(key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=True)

    # Generate index.html
    generate_html_from_template('index.html', {'news_articles': news_articles}, 'index.html')

    # Generate news index page
    generate_html_from_template('news_index.html', {'news_articles': news_articles}, 'news/index.html')

    # Create other necessary files
    create_css_file()
    create_js_file()
    create_sitemap(news_articles)
    create_robots_txt()
    create_404_page()
    create_tos_page()
    create_readme()

    print("Abhaynagar Portal project structure and files have been created successfully!")

if __name__ == "__main__":
    create_portal()

