/* Optimized Scroll Animations & Sidenav Logic */

document.addEventListener('DOMContentLoaded', () => {
    /* --- Sidenav Logic (Mobile) --- */
    const initSidenav = () => {
        const toggleBtn = document.getElementById('menu-submit');
        const overlay = document.querySelector('.sidenav-overlay') || (() => {
            const el = document.createElement('div');
            el.className = 'sidenav-overlay';
            document.body.appendChild(el);
            return el;
        })();

        const closeSidenav = () => document.body.classList.remove('sidenav-active');
        const openSidenav = (e) => {
            if (e) e.preventDefault();
            document.body.classList.add('sidenav-active');
        };

        if (toggleBtn) toggleBtn.onclick = openSidenav;
        if (overlay) overlay.onclick = closeSidenav;

        document.querySelectorAll('#menu .menu-item').forEach(link => {
            link.addEventListener('click', closeSidenav, { passive: true });
        });
    };

    initSidenav();

    /* --- Smooth Scroll --- */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#' || !href) return;
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });

    /* --- Intersection Observers --- */
    const observerOptions = { threshold: 0.1 };

    // Reveal Observer
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                revealObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Nav Dot Observer
    const dots = document.querySelectorAll('.side-nav-dot');
    const navObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.id;
                if (!id) return;
                dots.forEach(dot => {
                    dot.classList.toggle('active', dot.getAttribute('href') === `#${id}`);
                });
            }
        });
    }, { threshold: 0.5 });

    // Multi-purpose Section Processing
    document.querySelectorAll('section').forEach(section => {
        // Ensure ID for scrollspy
        if (section.id) navObserver.observe(section);

        // Add fade-in except for hero
        if (!section.classList.contains('s-hm')) {
            section.classList.add('fade-in-section');
            revealObserver.observe(section);
        }
    });
});
