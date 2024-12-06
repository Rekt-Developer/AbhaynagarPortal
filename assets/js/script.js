
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
    