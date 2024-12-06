import os
import json

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file(path, content):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

def create_portal():
    # Create directory structure
    create_directory('assets/css')
    create_directory('assets/js')
    create_directory('assets/images')
    create_directory('news')

    # Create index.html
    index_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abhaynagar News Portal | Bengali-English News</title>
    <meta name="description" content="Stay updated with the latest news from Abhaynagar Upazila. Bilingual news portal featuring Bengali and English content.">
    <link rel="canonical" href="https://rekt-developer.github.io/abhaynagar-portal/">
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <link href="https://fonts.maateen.me/kalpurush/font.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Abhaynagar News Portal",
      "url": "https://rekt-developer.github.io/abhaynagar-portal/",
      "potentialAction": {
        "@type": "SearchAction",
        "target": "https://rekt-developer.github.io/abhaynagar-portal/search?q={search_term_string}",
        "query-input": "required name=search_term_string"
      }
    }
    </script>
    <meta property="og:title" content="Abhaynagar News Portal | Bengali-English News">
    <meta property="og:description" content="Stay updated with the latest news from Abhaynagar Upazila. Bilingual news portal featuring Bengali and English content.">
    <meta property="og:image" content="https://rekt-developer.github.io/abhaynagar-portal/assets/images/banner.jpg">
    <meta property="og:url" content="https://rekt-developer.github.io/abhaynagar-portal/">
    <meta property="og:type" content="website">
</head>
<body class="font-inter bg-gray-100">
    <header class="bg-green-600 text-white sticky top-0 z-50">
        <nav class="container mx-auto px-4 py-4 flex justify-between items-center">
            <a href="/" class="text-2xl font-bold">Abhaynagar Portal</a>
            <div class="flex items-center space-x-4">
                <button id="langToggle" class="bg-white text-green-600 px-4 py-2 rounded transition duration-300 hover:bg-green-100">EN | বাং</button>
                <button id="darkModeToggle" class="text-white" aria-label="Toggle dark mode">
                    <i class="fas fa-moon"></i>
                </button>
            </div>
        </nav>
    </header>

    <main>
        <section class="hero bg-cover bg-center h-96 flex items-center" style="background-image: url('assets/images/mukteshwari_river.jpg');">
            <div class="container mx-auto px-4">
                <h1 class="text-4xl md:text-6xl font-bold text-white mb-4 shadow-text">Welcome to Abhaynagar Portal</h1>
                <p class="text-xl text-white shadow-text">Your bilingual gateway to Abhaynagar news and information</p>
            </div>
        </section>

        <section id="featured-news" class="container mx-auto px-4 py-8">
            <h2 class="text-3xl font-bold mb-6">Featured News</h2>
            <div id="featured-news-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Dynamically populated by JavaScript -->
            </div>
        </section>

        <section id="quick-facts" class="bg-white py-8">
            <div class="container mx-auto px-4">
                <h2 class="text-3xl font-bold mb-6">Quick Facts about Abhaynagar</h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="bg-green-100 p-6 rounded-lg shadow-md">
                        <h3 class="text-xl font-semibold mb-2">Population</h3>
                        <p>290,143 (2022)</p>
                    </div>
                    <div class="bg-green-100 p-6 rounded-lg shadow-md">
                        <h3 class="text-xl font-semibold mb-2">Area</h3>
                        <p>247.21 km²</p>
                    </div>
                    <div class="bg-green-100 p-6 rounded-lg shadow-md">
                        <h3 class="text-xl font-semibold mb-2">Postal Code</h3>
                        <p>7460</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="recent-updates" class="container mx-auto px-4 py-8">
            <h2 class="text-3xl font-bold mb-6">Recent Updates</h2>
            <div id="news-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Dynamically populated by JavaScript -->
            </div>
            <div class="mt-8 text-center">
                <button id="load-more" class="bg-green-600 text-white px-6 py-2 rounded hover:bg-green-700 transition duration-300">Load More</button>
            </div>
        </section>
    </main>

    <footer class="bg-green-800 text-white py-8">
        <div class="container mx-auto px-4">
            <div class="flex flex-wrap justify-between">
                <div class="w-full md:w-1/3 mb-6 md:mb-0">
                    <h3 class="text-xl font-bold mb-4">About Abhaynagar Portal</h3>
                    <p>Your trusted source for bilingual news and information about Abhaynagar Upazila.</p>
                </div>
                <div class="w-full md:w-1/3 mb-6 md:mb-0">
                    <h3 class="text-xl font-bold mb-4">Quick Links</h3>
                    <ul>
                        <li><a href="/" class="hover:underline">Home</a></li>
                        <li><a href="#featured-news" class="hover:underline">Featured News</a></li>
                        <li><a href="#recent-updates" class="hover:underline">Recent Updates</a></li>
                        <li><a href="tos.html" class="hover:underline">Terms of Service</a></li>
                    </ul>
                </div>
                <div class="w-full md:w-1/3">
                    <h3 class="text-xl font-bold mb-4">Contact</h3>
                    <p>Author: Likhon Sheikh</p>
                    <p>Email: sheikh@likhon.xyz</p>
                    <a href="https://t.me/RektDevelopers" target="_blank" rel="noopener noreferrer" class="inline-block mt-2 text-white hover:text-green-300 transition duration-300">
                        <i class="fab fa-telegram"></i> Join our Telegram Channel
                    </a>
                </div>
            </div>
            <div class="mt-8 text-center">
                <p>&copy; 2024 Abhaynagar Portal. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="assets/js/script.js"></script>
</body>
</html>
    '''
    create_file('index.html', index_html)

    # Create style.css
    style_css = '''
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';

/* Custom styles */
body {
    font-family: 'Inter', 'Kalpurush', sans-serif;
}

.font-bangla {
    font-family: 'Kalpurush', sans-serif;
}

/* Hover effects */
.hover-grow {
    transition: transform 0.3s ease;
}

.hover-grow:hover {
    transform: scale(1.05);
}

/* Custom animations */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.animate-fadeIn {
    animation: fadeIn 0.5s ease-in-out;
}

/* Custom color scheme */
.bg-abhaynagar-green {
    background-color: #2C5F2D;
}

.text-abhaynagar-gold {
    color: #FFD700;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .hero {
        height: 60vh;
    }
}

/* Accessibility improvements */
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border-width: 0;
}

/* Custom button styles */
.btn-primary {
    @apply bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition duration-300;
}

.btn-secondary {
    @apply bg-white text-green-600 border border-green-600 px-4 py-2 rounded hover:bg-green-100 transition duration-300;
}

/* Dark mode styles */
.dark {
    @apply bg-gray-900 text-white;
}

.dark .bg-white {
    @apply bg-gray-800;
}

.dark .text-gray-600 {
    @apply text-gray-300;
}

.dark .bg-green-100 {
    @apply bg-green-900;
}

.shadow-text {
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}
    '''
    create_file('assets/css/style.css', style_css)

    # Create script.js
    script_js = '''
// Language toggle functionality
const langToggle = document.getElementById('langToggle');
let currentLang = 'en';

langToggle.addEventListener('click', () => {
    currentLang = currentLang === 'en' ? 'bn' : 'en';
    updateLanguage();
});

function updateLanguage() {
    // Implement language switch logic here
    console.log(`Language switched to ${currentLang}`);
    // Update UI elements based on selected language
}

// Dark mode toggle
const darkModeToggle = document.getElementById('darkModeToggle');
const body = document.body;

darkModeToggle.addEventListener('click', () => {
    body.classList.toggle('dark');
    const isDarkMode = body.classList.contains('dark');
    localStorage.setItem('darkMode', isDarkMode);
    updateDarkModeIcon(isDarkMode);
});

function updateDarkModeIcon(isDarkMode) {
    const icon = darkModeToggle.querySelector('i');
    icon.className = isDarkMode ? 'fas fa-sun' : 'fas fa-moon';
}

// Check for saved dark mode preference
const savedDarkMode = localStorage.getItem('darkMode');
if (savedDarkMode === 'true') {
    body.classList.add('dark');
    updateDarkModeIcon(true);
}

// Fetch and display news
const newsGrid = document.getElementById('news-grid');
const featuredNewsGrid = document.getElementById('featured-news-grid');
let currentPage = 1;
const newsPerPage = 6;

async function fetchNews() {
    // Simulated API call to fetch news
    const response = await fetch(`https://api.example.com/news?page=${currentPage}&limit=${newsPerPage}`);
    const data = await response.json();
    return data.news;
}

function createNewsCard(article) {
    const card = document.createElement('div');
    card.className = 'bg-white rounded-lg shadow-md overflow-hidden hover-grow animate-fadeIn';
    card.innerHTML = `
        <img src="${article.image}" alt="${article.title}" class="w-full h-48 object-cover" loading="lazy">
        <div class="p-4">
            <h3 class="text-xl font-semibold mb-2">${article.title}</h3>
            <p class="text-gray-600 mb-4">${article.description}</p>
            <a href="${article.url}" class="btn-primary">Read More</a>
        </div>
    `;
    return card;
}

async function loadNews() {
    const news = await fetchNews();
    news.forEach(article => {
        const card = createNewsCard(article);
        newsGrid.appendChild(card);
    });
}

async function loadFeaturedNews() {
    const featuredNews = await fetchNews(); // Assume this returns featured news
    featuredNews.slice(0, 3).forEach(article => {
        const card = createNewsCard(article);
        featuredNewsGrid.appendChild(card);
    });
}

// Load more functionality
const loadMoreBtn = document.getElementById('load-more');
loadMoreBtn.addEventListener('click', () => {
    currentPage++;
    loadNews();
});

// Initial load
loadFeaturedNews();
loadNews();

// Intersection Observer for lazy loading
const lazyLoadObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            observer.unobserve(img);
        }
    });
});

document.querySelectorAll('img[data-src]').forEach(img => {
    lazyLoadObserver.observe(img);
});

// Add smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e)anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Implement a simple search functionality
const searchInput = document.getElementById('search-input');
const searchButton = document.getElementById('search-button');

searchButton.addEventListener('click', performSearch);
searchInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        performSearch();
    }
});

function performSearch() {
    const searchTerm = searchInput.value.toLowerCase();
    const allNewsItems = document.querySelectorAll('.news-item');
    
    allNewsItems.forEach(item => {
        const title = item.querySelector('h3').textContent.toLowerCase();
        const description = item.querySelector('p').textContent.toLowerCase();
        
        if (title.includes(searchTerm) || description.includes(searchTerm)) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}

// Add a back-to-top button
const backToTopButton = document.createElement('button');
backToTopButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
backToTopButton.className = 'back-to-top hidden fixed bottom-5 right-5 bg-green-600 text-white p-3 rounded-full shadow-lg';
document.body.appendChild(backToTopButton);

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
        backToTopButton.classList.remove('hidden');
    } else {
        backToTopButton.classList.add('hidden');
    }
});

backToTopButton.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});
    '''
    create_file('assets/js/script.js', script_js)

    # Create sitemap.xml
    sitemap_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://rekt-developer.github.io/abhaynagar-portal/</loc>
    <lastmod>2024-12-06</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://rekt-developer.github.io/abhaynagar-portal/tos.html</loc>
    <lastmod>2024-12-06</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <!-- Add more URLs for news articles dynamically -->
</urlset>'''
    create_file('sitemap.xml', sitemap_xml)

    # Create robots.txt
    robots_txt = '''User-agent: *
Allow: /
Allow: /news/

Disallow: /assets/

Sitemap: https://rekt-developer.github.io/abhaynagar-portal/sitemap.xml'''
    create_file('robots.txt', robots_txt)

    # Create 404.html
    not_found_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found | Abhaynagar Portal</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="bg-gray-100 flex items-center justify-center h-screen">
    <div class="text-center">
        <h1 class="text-6xl font-bold text-green-600 mb-4">404</h1>
        <p class="text-xl mb-8">Oops! The page you're looking for doesn't exist.</p>
        <a href="/" class="btn-primary">Go Back to Homepage</a>
    </div>
</body>
</html>'''
    create_file('404.html', not_found_html)

    # Create tos.html
    tos_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terms of Service | Abhaynagar Portal</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="bg-gray-100">
    <header class="bg-green-600 text-white">
        <nav class="container mx-auto px-4 py-4">
            <a href="/" class="text-2xl font-bold">Abhaynagar Portal</a>
        </nav>
    </header>

    <main class="container mx-auto px-4 py-8">
        <h1 class="text-3xl font-bold mb-6">Terms of Service</h1>
        <div class="bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-xl font-semibold mb-4">1. Acceptance of Terms</h2>
            <p class="mb-4">By accessing and using the Abhaynagar Portal, you agree to be bound by these Terms of Service.</p>

            <h2 class="text-xl font-semibold mb-4">2. Use of Content</h2>
            <p class="mb-4">All content provided on this website is for informational purposes only. You may not reproduce, distribute, or transmit any content without prior written permission.</p>

            <h2 class="text-xl font-semibold mb-4">3. User Contributions</h2>
            <p class="mb-4">Users may submit comments or feedback. By doing so, you grant Abhaynagar Portal a non-exclusive license to use, reproduce, and publish such contributions.</p>

            <h2 class="text-xl font-semibold mb-4">4. Disclaimer</h2>
            <p class="mb-4">The information provided on this website is for general informational purposes only. We make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability or availability of the information.</p>

            <h2 class="text-xl font-semibold mb-4">5. Contact Information</h2>
            <p>For any questions or concerns regarding these Terms of Service, please contact:</p>
            <p>Likhon Sheikh</p>
            <p>Email: sheikh@likhon.xyz</p>
        </div>
    </main>

    <footer class="bg-green-800 text-white py-8 mt-8">
        <div class="container mx-auto px-4 text-center">
            <p>&copy; 2024 Abhaynagar Portal. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>'''
    create_file('tos.html', tos_html)

    # Create README.md
    readme_md = '''# Abhaynagar Portal

A modern, SEO-optimized static news portal about Abhaynagar Upazila, Bangladesh, featuring bilingual (Bangla & English) grids and an advanced layout using modern CDNs.

## Features

- Bilingual content (Bangla and English)
- Fully responsive design with Tailwind CSS
- SEO optimization with structured data and meta tags
- Dynamic news fetching system
- Lazy loading for improved performance
- Dark mode support
- Smooth scrolling and back-to-top functionality

## Quick Facts

- Population: 290,143 (2022)
- Area: 247.21 km²
- Postal Code: 7460

## Live Demo

Access the portal here: [Abhaynagar Portal](https://rekt-developer.github.io/abhaynagar-portal/)

## Usage Instructions for GitHub Pages Deployment

1. Fork this repository
2. Go to the repository settings
3. Navigate to the "Pages" section
4. Under "Source", select the branch you want to deploy (usually `main` or `master`)
5. Click "Save"
6. Your site will be published at `https://<username>.github.io/abhaynagar-portal/`

## Development

To set up the project locally:

1. Clone the repository
2. Open `index.html` in your browser
3. For live reloading and development, you can use a local server like `live-server`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Likhon Sheikh
Email: sheikh@likhon.xyz
Telegram: [@RektDevelopers](https://t.me/RektDevelopers)

## License

This project is licensed under the MIT License.'''
    create_file('README.md', readme_md)

    # Create a sample news article in Markdown
    sample_news_md = '''---
title: "BNP Leader's House Bombed: Investigation Reopened"
title_bn: "বিএনপি নেতা কর্মীদের বাড়ি বাড়ি বোমা বিস্ফোরণের ঘটনা পুনরায় তদন্ত"
date: "2024-12-06"
image: "/assets/images/news/bnp_leader_house.jpg"
description: "Local authorities have reopened the investigation into the bombing of a BNP leader's house in Abhaynagar."
description_bn: "আভয়নগরে বিএনপি নেতার বাড়িতে বোমা হামলার ঘটনায় স্থানীয় কর্তৃপক্ষ পুনরায় তদন্ত শুরু করেছে।"
---

# BNP Leader's House Bombed: Investigation Reopened

Local authorities in Abhaynagar have decided to reopen the investigation into the bombing incident at a BNP leader's residence. The incident, which occurred last month, had initially been closed due to lack of evidence.

## Key Points:

1. The bombing took place on November 15, 2024
2. No casualties were reported, but significant property damage occurred
3. New evidence has emerged, prompting the reopening of the case
4. Local police are calling for any witnesses to come forward

The BNP (Bangladesh Nationalist Party) has welcomed the decision to reopen the investigation, stating that they hope for a fair and thorough inquiry into the matter.

---

# বিএনপি নেতা কর্মীদের বাড়ি বাড়ি বোমা বিস্ফোরণের ঘটনা পুনরায় তদন্ত

আভয়নগরের স্থানীয় কর্তৃপক্ষ একজন বিএনপি নেতার বাসায় বোমা হামলার ঘটনায় তদন্ত পুনরায় খোলার সিদ্ধান্ত নিয়েছে। গত মাসে ঘটা এই ঘটনাটি প্রাথমিকভাবে প্রমাণের অভাবে বন্ধ করে দেওয়া হয়েছিল।

## মূল বিষয়সমূহ:

1. বোমা হামলাটি ২০২৪ সালের ১৫ নভেম্বর সংঘটিত হয়
2. কোনো হতাহতের খবর পাওয়া যায়নি, তবে যথেষ্ট সম্পত্তির ক্ষতি হয়েছে
3. নতুন প্রমাণ পাওয়া গেছে, যা মামলাটি পুনরায় খোলার কারণ হয়েছে
4. স্থানীয় পুলিশ যেকোনো সাক্ষীকে এগিয়ে আসার আহ্বান জানিয়েছে

বিএনপি (বাংলাদেশ জাতীয়তাবাদী দল) তদন্ত পুনরায় খোলার সিদ্ধান্তকে স্বাগত জানিয়েছে, এবং তারা আশা করছে যে বিষয়টি নিয়ে একটি ন্যায্য ও পূর্ণাঙ্গ তদন্ত হবে।'''
    create_file('news/BNP_Leader_News.md', sample_news_md)

    print("Abhaynagar Portal project structure and files have been created successfully!")

if __name__ == "__main__":
    create_portal()
