document.addEventListener('DOMContentLoaded', () => {
    // Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Theme Toggle
    const themeToggle = document.getElementById('themeToggle');
    const icon = themeToggle.querySelector('i');
    
    // Check local storage for theme
    if (localStorage.getItem('theme') === 'dark') {
        document.body.setAttribute('data-theme', 'dark');
        icon.classList.replace('fa-moon', 'fa-sun');
    }

    themeToggle.addEventListener('click', () => {
        if (document.body.getAttribute('data-theme') === 'dark') {
            document.body.removeAttribute('data-theme');
            icon.classList.replace('fa-sun', 'fa-moon');
            localStorage.setItem('theme', 'light');
        } else {
            document.body.setAttribute('data-theme', 'dark');
            icon.classList.replace('fa-moon', 'fa-sun');
            localStorage.setItem('theme', 'dark');
        }
    });

    // Scroll Reveal Animation
    const revealElements = document.querySelectorAll('.reveal');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, {
        threshold: 0.1
    });

    revealElements.forEach(el => revealObserver.observe(el));
});

// Modal Logic
function openModal(id) {
    const modal = document.getElementById('productModal');
    const dataDiv = document.getElementById(`product-data-${id}`);
    
    if (!dataDiv) return;

    const name = dataDiv.getAttribute('data-name');
    const desc = dataDiv.getAttribute('data-desc');
    const price = dataDiv.getAttribute('data-price');
    const discount = dataDiv.getAttribute('data-discount');
    const image = dataDiv.getAttribute('data-image');
    const rating = dataDiv.getAttribute('data-rating');
    const reviews = dataDiv.getAttribute('data-reviews');
    const category = dataDiv.getAttribute('data-category');

    document.getElementById('modal-name').innerText = name;
    document.getElementById('modal-desc').innerText = desc;
    document.getElementById('modal-image').src = image;
    document.getElementById('modal-rating').innerText = rating;
    document.getElementById('modal-reviews').innerText = reviews;
    document.getElementById('modal-category').innerText = category;

    const priceContainer = document.getElementById('modal-price-container');
    let finalPrice = price;
    if (discount && discount !== "None") {
        priceContainer.innerHTML = `₹${discount} <del style="font-size: 1.2rem; color: var(--text-light); font-weight: 400; margin-left: 10px;">₹${price}</del><span style="font-size: 1rem; background: var(--secondary-orange); color: white; padding: 4px 10px; border-radius: var(--radius-pill); margin-left: 15px; vertical-align: middle;">Sale</span>`;
        finalPrice = discount;
    } else {
        priceContainer.innerHTML = `₹${price}`;
    }

    const waText = `Hello, I would like to order:%0A- ${name} × 1%0ATotal Amount: ₹${finalPrice}`;
    document.getElementById('modal-wa-btn').href = `https://wa.me/${window.whatsappNumber}?text=${waText}`;

    modal.classList.add('show');
}

function closeModal() {
    const modal = document.getElementById('productModal');
    modal.classList.remove('show');
}

window.onclick = function(event) {
    const modal = document.getElementById('productModal');
    if (event.target == modal) {
        closeModal();
    }
}
