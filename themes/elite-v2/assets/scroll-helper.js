/**
 * Scroll Helper Navigation Script
 * Dynamically shows/hides scroll helpers based on scroll position
 */

document.addEventListener('DOMContentLoaded', function () {
    // Get all scroll helpers
    const helpers = {
        home: document.querySelector('.scroll-down-helper'),
        services: document.querySelector('.scroll-helper-services'),
        about: document.querySelector('.scroll-helper-about'),
        contact: document.querySelector('.scroll-helper-contact')
    };

    // Get all sections
    const sections = {
        home: document.querySelector('section#home'),
        services: document.querySelector('section#services'),
        about: document.querySelector('section#about'),
        contact: document.querySelector('section#contact')
    };

    // Function to check which section is in view
    function updateScrollHelpers() {
        const scrollPos = window.scrollY + window.innerHeight / 2;

        // Hide all helpers first
        Object.values(helpers).forEach(helper => {
            if (helper) helper.style.display = 'none';
        });

        // Show appropriate helper based on scroll position
        if (sections.home && isInViewport(sections.home)) {
            if (helpers.home) helpers.home.style.display = 'block';
        } else if (sections.services && isInViewport(sections.services)) {
            if (helpers.services) helpers.services.style.display = 'block';
        } else if (sections.about && isInViewport(sections.about)) {
            if (helpers.about) helpers.about.style.display = 'block';
        } else if (sections.contact && isInViewport(sections.contact)) {
            if (helpers.contact) helpers.contact.style.display = 'block';
        }
    }

    // Helper function to check if element is in viewport
    function isInViewport(element) {
        if (!element) return false;
        const rect = element.getBoundingClientRect();
        const windowHeight = window.innerHeight || document.documentElement.clientHeight;

        // Element is in viewport if its center is visible
        const elementCenter = rect.top + rect.height / 2;
        return elementCenter >= 0 && elementCenter <= windowHeight;
    }

    // Update on scroll
    window.addEventListener('scroll', updateScrollHelpers);

    // Update on load (to ensure images are loaded and layout is stable)
    window.addEventListener('load', updateScrollHelpers);

    // Initial update immediately
    updateScrollHelpers();

    // Check again after a short delay to handle browser scroll restoration
    setTimeout(updateScrollHelpers, 100);
    setTimeout(updateScrollHelpers, 500);

    // Note: Native CSS scroll-behavior: smooth ensures perfect sync with side-nav dots.
});
