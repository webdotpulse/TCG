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

    // 5. Modal Logic
    const openModalBtn = document.getElementById('open-demo-modal');
    const demoModal = document.getElementById('demo-modal');
    const demoModalDialog = document.getElementById('demo-modal-dialog');
    const closeBtns = document.querySelectorAll('.close-modal');

    if (openModalBtn && demoModal && demoModalDialog) {
        openModalBtn.addEventListener('click', () => {
            demoModal.classList.remove('hidden');
            document.body.style.overflow = 'hidden';

            // Trigger animation after a tiny delay
            setTimeout(() => {
                demoModalDialog.classList.remove('scale-95', 'opacity-0');
                demoModalDialog.classList.add('scale-100', 'opacity-100');
            }, 10);
        });

        const closeModal = () => {
            demoModalDialog.classList.remove('scale-100', 'opacity-100');
            demoModalDialog.classList.add('scale-95', 'opacity-0');

            // Wait for transition to finish before hiding
            setTimeout(() => {
                demoModal.classList.add('hidden');
                document.body.style.overflow = '';
            }, 300);
        };

        closeBtns.forEach(btn => {
            btn.addEventListener('click', closeModal);
        });

        // Close on backdrop click
        demoModal.addEventListener('click', (e) => {
            if (e.target === demoModal.firstElementChild || e.target.classList.contains('fixed')) {
                closeModal();
            }
        });
    }

    // 6. Toast Logic
    const showToastBtn = document.getElementById('show-demo-toast');
    const demoToast = document.getElementById('demo-toast');
    let toastTimeout;

    if (showToastBtn && demoToast) {
        const closeToastBtn = demoToast.querySelector('.close-toast');

        const hideToast = () => {
            demoToast.classList.add('translate-x-full', 'opacity-0');
            setTimeout(() => {
                demoToast.classList.add('hidden');
            }, 300);
        };

        const showToast = () => {
            // Reset state
            clearTimeout(toastTimeout);
            demoToast.classList.remove('hidden');

            // Small delay to allow display:block to apply before animating
            setTimeout(() => {
                demoToast.classList.remove('translate-x-full', 'opacity-0');
            }, 10);

            // Auto hide after 3 seconds
            toastTimeout = setTimeout(() => {
                hideToast();
            }, 3000);
        };

        showToastBtn.addEventListener('click', showToast);

        if (closeToastBtn) {
            closeToastBtn.addEventListener('click', () => {
                clearTimeout(toastTimeout);
                hideToast();
            });
        }
    }

    // 7. Fullscreen Menu Toggle
    const fsMenuBtn = document.getElementById('fullscreen-menu-btn');
    const fsMenu = document.getElementById('fullscreen-menu');
    const minimalHeader = document.getElementById('minimal-header');

    if (fsMenuBtn && fsMenu && minimalHeader) {
        const logoText = document.getElementById('logo-text');
        const iconOpen = document.getElementById('menu-icon-open');
        const iconClose = document.getElementById('menu-icon-close');

        let isOpen = false;

        fsMenuBtn.addEventListener('click', () => {
            isOpen = !isOpen;

            if (isOpen) {
                // Open menu
                fsMenu.classList.remove('opacity-0', 'pointer-events-none');
                fsMenu.classList.add('opacity-100', 'pointer-events-auto');
                document.body.style.overflow = 'hidden';

                // Button styling
                fsMenuBtn.classList.add('bg-transparent', 'border-white/20', 'text-white');
                fsMenuBtn.classList.remove('bg-white', 'border-slate-100', 'text-slate-900', 'hover:bg-slate-50', 'hover:text-brand-blue');

                // Logo text styling
                if (logoText) {
                    logoText.classList.remove('text-slate-900');
                    logoText.classList.add('text-white');
                }

                // Icon toggle
                iconOpen.classList.add('opacity-0');
                iconClose.classList.remove('opacity-0');
            } else {
                // Close menu
                fsMenu.classList.add('opacity-0', 'pointer-events-none');
                fsMenu.classList.remove('opacity-100', 'pointer-events-auto');
                document.body.style.overflow = '';

                // Button styling
                fsMenuBtn.classList.remove('bg-transparent', 'border-white/20', 'text-white');
                fsMenuBtn.classList.add('bg-white', 'border-slate-100', 'text-slate-900', 'hover:bg-slate-50', 'hover:text-brand-blue');

                // Logo text styling
                if (logoText) {
                    logoText.classList.add('text-slate-900');
                    logoText.classList.remove('text-white');
                }

                // Icon toggle
                iconOpen.classList.remove('opacity-0');
                iconClose.classList.add('opacity-0');
            }
        });
    }

    // 8. Fancy Scroll to Top Button
    const scrollTopBtn = document.createElement('button');
    scrollTopBtn.innerHTML = '<i data-lucide="arrow-up" class="text-white"></i>';
    scrollTopBtn.className = 'fixed bottom-6 right-6 w-12 h-12 bg-brand-blue hover:bg-brand-teal text-white rounded-full shadow-xl flex items-center justify-center transition-all duration-300 transform translate-y-20 opacity-0 z-50 hover:-translate-y-1 hover:shadow-brand-blue/30';
    scrollTopBtn.setAttribute('aria-label', 'Scroll to top');
    document.body.appendChild(scrollTopBtn);

    // Initialize the icon in the new button
    if (typeof lucide !== 'undefined') {
        lucide.createIcons({
            root: scrollTopBtn
        });
    }

    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            scrollTopBtn.classList.remove('translate-y-20', 'opacity-0');
        } else {
            scrollTopBtn.classList.add('translate-y-20', 'opacity-0');
        }
    });

    scrollTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});