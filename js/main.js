document.addEventListener('DOMContentLoaded', () => {
  // Mobile Menu Toggle
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const icon = mobileMenuBtn.querySelector('i');

  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
      if (mobileMenu.classList.contains('hidden')) {
        icon.classList.remove('fa-xmark');
        icon.classList.add('fa-bars');
      } else {
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-xmark');
      }
    });
  }

  // Mobile Submenu Toggles
  const submenuToggles = document.querySelectorAll('.mobile-submenu-toggle');
  submenuToggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
      const submenu = e.currentTarget.nextElementSibling;
      const chevron = e.currentTarget.querySelector('i');

      if (submenu && submenu.classList.contains('mobile-submenu')) {
        submenu.classList.toggle('hidden');
        if (submenu.classList.contains('hidden')) {
          chevron.style.transform = 'rotate(0deg)';
        } else {
          chevron.style.transform = 'rotate(180deg)';
        }
      }
    });
  });

  // Cookie Banner Logic
  const cookieBanner = document.getElementById('cookie-banner');
  const customizeModal = document.getElementById('cookie-customize-modal');
  const btnAccept = document.getElementById('btn-accept-cookies');
  const btnReject = document.getElementById('btn-reject-cookies');
  const btnCustomize = document.getElementById('btn-customize-cookies');
  const btnSavePrefs = document.getElementById('btn-save-preferences');
  const btnCloseModal = document.getElementById('close-customize-modal');

  // Show banner with a slight delay
  setTimeout(() => {
    if (cookieBanner) {
      cookieBanner.classList.remove('translate-y-full');
    }
  }, 1000);

  const hideBanner = () => {
    if (cookieBanner) {
      cookieBanner.classList.add('translate-y-full');
    }
  };

  const closeCustomizeModal = () => {
    if (customizeModal) {
      customizeModal.classList.add('hidden');
    }
  };

  if (btnAccept) btnAccept.addEventListener('click', hideBanner);
  if (btnReject) btnReject.addEventListener('click', hideBanner);
  if (btnSavePrefs) {
    btnSavePrefs.addEventListener('click', () => {
      closeCustomizeModal();
      hideBanner();
    });
  }

  if (btnCustomize) {
    btnCustomize.addEventListener('click', () => {
      if (customizeModal) customizeModal.classList.remove('hidden');
    });
  }

  if (btnCloseModal) btnCloseModal.addEventListener('click', closeCustomizeModal);
});