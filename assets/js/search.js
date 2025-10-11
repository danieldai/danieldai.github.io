// Search functionality using Lunr.js
let searchIndex = null;
let searchData = null;

// Initialize search when page loads
document.addEventListener('DOMContentLoaded', function() {
  initializeSearch();
});

async function initializeSearch() {
  try {
    // Load search data
    const response = await fetch('/search.json');
    searchData = await response.json();
    
    // Build search index
    searchIndex = lunr(function() {
      this.ref('url');
      this.field('title', { boost: 10 });
      this.field('excerpt', { boost: 5 });
      this.field('content');
      this.field('tags', { boost: 3 });
      this.field('categories', { boost: 2 });
      
      // Add documents to index
      searchData.forEach(function(doc) {
        this.add(doc);
      }, this);
    });
    
    // Set up search input handler
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
      searchInput.addEventListener('input', debounce(performSearch, 300));
    }
  } catch (error) {
    console.error('Error initializing search:', error);
    showError('Failed to initialize search. Please refresh the page.');
  }
}

function performSearch(event) {
  const query = event.target.value.trim();
  const resultsContainer = document.getElementById('search-results');
  const noResults = document.getElementById('no-results');
  const loading = document.getElementById('search-loading');
  
  if (!query) {
    resultsContainer.innerHTML = '';
    noResults.classList.add('hidden');
    loading.classList.add('hidden');
    return;
  }
  
  loading.classList.remove('hidden');
  noResults.classList.add('hidden');
  
  try {
    const results = searchIndex.search(query);
    displayResults(results);
  } catch (error) {
    console.error('Search error:', error);
    showError('Search failed. Please try again.');
  }
  
  loading.classList.add('hidden');
}

function displayResults(results) {
  const resultsContainer = document.getElementById('search-results');
  const noResults = document.getElementById('no-results');
  
  if (results.length === 0) {
    resultsContainer.innerHTML = '';
    noResults.classList.remove('hidden');
    return;
  }
  
  noResults.classList.add('hidden');
  
  const resultsHTML = results.map(result => {
    const post = searchData.find(doc => doc.url === result.ref);
    if (!post) return '';
    
    return `
      <div class="card p-6">
        <div class="flex items-start justify-between mb-3">
          <h3 class="text-xl font-semibold text-gray-900">
            <a href="${post.url}" class="hover:text-primary-600 transition-colors duration-200">
              ${post.title}
            </a>
          </h3>
          <time datetime="${post.date}" class="text-sm text-gray-500 ml-4">
            ${new Date(post.date).toLocaleDateString('en-US', { 
              year: 'numeric', 
              month: 'short', 
              day: 'numeric' 
            })}
          </time>
        </div>
        
        <p class="text-gray-600 mb-4">${post.excerpt || ''}</p>
        
        ${post.tags && post.tags.length > 0 ? `
          <div class="flex flex-wrap gap-2 mb-4">
            ${post.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
          </div>
        ` : ''}
        
        <div class="flex items-center justify-between">
          <div class="flex items-center text-sm text-gray-500">
            <span class="bg-primary-100 text-primary-800 px-2 py-1 rounded text-xs font-medium">
              Score: ${result.score.toFixed(2)}
            </span>
          </div>
          <a href="${post.url}" class="text-primary-600 hover:text-primary-700 font-medium text-sm">
            Read more →
          </a>
        </div>
      </div>
    `;
  }).join('');
  
  resultsContainer.innerHTML = resultsHTML;
}

function showError(message) {
  const resultsContainer = document.getElementById('search-results');
  resultsContainer.innerHTML = `
    <div class="bg-red-50 border border-red-200 rounded-md p-4">
      <div class="flex">
        <svg class="h-5 w-5 text-red-400" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"></path>
        </svg>
        <div class="ml-3">
          <p class="text-sm text-red-800">${message}</p>
        </div>
      </div>
    </div>
  `;
}

// Debounce function to limit search frequency
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}
