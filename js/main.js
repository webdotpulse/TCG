document.addEventListener('DOMContentLoaded', () => {
    // 1. Boxed Navigation Scroll Effect
    const headerContainer = document.getElementById('header-container');
    const navbar = document.getElementById('navbar');

    if (headerContainer && navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                // Shrink and make more opaque
                headerContainer.classList.add('pt-2');
                headerContainer.classList.remove('pt-4');
                navbar.classList.add('bg-white/95', 'shadow-md', 'shadow-slate-200/50');
                navbar.classList.remove('bg-white/80', 'shadow-sm');
            } else {
                // Return to floating boxed state
                headerContainer.classList.add('pt-4');
                headerContainer.classList.remove('pt-2');
                navbar.classList.remove('bg-white/95', 'shadow-md', 'shadow-slate-200/50');
                navbar.classList.add('bg-white/80', 'shadow-sm');
            }
        });
    }

    // 2. Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const closeMenuBtn = document.getElementById('close-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && closeMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.remove('hidden');
            // Small delay to allow display:block to apply before animating transform
            setTimeout(() => {
                mobileMenu.classList.remove('translate-x-full');
            }, 10);
            document.body.style.overflow = 'hidden'; // Prevent scrolling
        });

        closeMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.add('translate-x-full');
            setTimeout(() => {
                mobileMenu.classList.add('hidden');
            }, 300); // Wait for transition
            document.body.style.overflow = '';
        });
    }

    // 3. Cookie Banner Logic
    const cookieBanner = document.getElementById('cookie-banner');
    if (cookieBanner) {
        setTimeout(() => {
            cookieBanner.classList.remove('translate-y-[150%]');
        }, 1500); // Show after 1.5s
    }

    const dismissCookie = () => {
        if (cookieBanner) {
            cookieBanner.classList.add('translate-y-[150%]');
        }
    };

    const acceptCookiesBtn = document.getElementById('accept-cookies');
    const rejectCookiesBtn = document.getElementById('reject-cookies');

    if (acceptCookiesBtn) acceptCookiesBtn.addEventListener('click', dismissCookie);
    if (rejectCookiesBtn) rejectCookiesBtn.addEventListener('click', dismissCookie);

    // 4. Hero Typer Effect
    const typerWords = ["The Charge Grid Chargers", "Charge management", "Energy management"];
    let typerIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    const typerElement = document.getElementById('hero-typer');

    function typeEffect() {
        if (!typerElement) return;

        const currentWord = typerWords[typerIndex];

        if (isDeleting) {
            charIndex--;
        } else {
            charIndex++;
        }

        typerElement.textContent = currentWord.substring(0, charIndex);

        let typeSpeed = isDeleting ? 40 : 80;

        if (!isDeleting && charIndex === currentWord.length) {
            typeSpeed = 2000; // Pause at end of word
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            typerIndex = (typerIndex + 1) % typerWords.length;
            typeSpeed = 500; // Pause before next word
        }

        setTimeout(typeEffect, typeSpeed);
    }

    // Start typing effect after a short delay
    if (typerElement) {
        setTimeout(typeEffect, 500);
    }
});