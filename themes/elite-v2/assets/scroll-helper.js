/**
 * Optimized Scroll Helper Navigation Script
 * Uses IntersectionObserver to avoid layout thrashing and main thread load
 */

document.addEventListener('DOMContentLoaded', function () {
    const helpers = {
        home: document.querySelector('.scroll-down-helper'),
        services: document.querySelector('.scroll-helper-services'),
        about: document.querySelector('.scroll-helper-about'),
        contact: document.querySelector('.scroll-helper-contact')
    };

    const sectionElements = document.querySelectorAll('section[id]');

    // Hide all helpers initially
    const hideAllHelpers = () => {
        Object.values(helpers).forEach(h => { if (h) h.style.display = 'none'; });
    };

    // Intersection Observer setup
    const options = {
        root: null,
        rootMargin: '-10% 0px -10% 0px', // Trigger slightly before center
        threshold: 0.2 // 20% visibility
    };

    const observer = new IntersectionObserver((entries) => {
        // Find the entry that is most visible
        const visibleEntry = entries.find(entry => entry.isIntersecting);

        if (visibleEntry && window.innerWidth > 1024) {
            const id = visibleEntry.target.id;
            hideAllHelpers();
            if (helpers[id]) {
                helpers[id].style.display = 'block';
            }
        }
    }, options);

    // Initial check for mobile
    if (window.innerWidth <= 1024) {
        hideAllHelpers();
        return;
    }

    sectionElements.forEach(section => observer.observe(section));

    // Handle Resize (Throttle)
    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            if (window.innerWidth <= 1024) {
                hideAllHelpers();
            } else {
                // Force a check/refresh if needed
            }
        }, 250);
    }, { passive: true });
});
