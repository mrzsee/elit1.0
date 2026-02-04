/* Scroll Animations & Sidenav Logic */

document.addEventListener('DOMContentLoaded', () => {

    /* --- Sidenav Logic (Mobile) --- */
    const initSidenav = () => {
        const toggleBtn = document.getElementById('menu-submit');
        const menuNav = document.getElementById('menu');
        const body = document.body;

        // Create Overlay if not exists
        let overlay = document.querySelector('.sidenav-overlay');
        if (!overlay) {
            overlay = document.createElement('div');
            overlay.className = 'sidenav-overlay';
            document.body.appendChild(overlay);
        }

        const closeSidenav = () => {
            body.classList.remove('sidenav-active');
        };

        const openSidenav = (e) => {
            if (e) e.preventDefault();
            body.classList.add('sidenav-active');
        };

        // Event Listeners
        if (toggleBtn) {
            // Remove old listeners by cloning (simple trick) or just add new one
            // Ideally we just add.
            toggleBtn.onclick = openSidenav;
        }

        if (overlay) {
            overlay.onclick = closeSidenav;
        }

        // Close on link click (optional, for SPA feel)
        const links = document.querySelectorAll('#menu .menu-item');
        links.forEach(link => {
            link.addEventListener('click', closeSidenav);
        });
    };

    initSidenav();


    /* --- Smooth Scroll & Animations --- */

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return; // Ignore empty anchors

            e.preventDefault();
            const targetElement = document.querySelector(href);

            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Landing Page Scroll Reveal Effect
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.fade-in-section');
    animatedElements.forEach(el => observer.observe(el));

    /* --- Side Nav & Scroll Spy Logic --- */
    const updateSideNav = () => {
        const sections = document.querySelectorAll('section');
        const dots = document.querySelectorAll('.side-nav-dot');

        const observerConfig = {
            threshold: 0.5 /* Trigger when 50% visible */
        };

        const navObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.getAttribute('id');
                    if (id) {
                        dots.forEach(dot => {
                            dot.classList.remove('active');
                            if (dot.getAttribute('href') === `#${id}`) {
                                dot.classList.add('active');
                            }
                        });
                    }
                }
            });
        }, observerConfig);

        sections.forEach(section => {
            // Assign ID if missing for tracking (fallback)
            if (!section.id) {
                // Logic to skip assigning if not needed or manual check
            }
            navObserver.observe(section);
        });
    };

    updateSideNav();

    // Auto-add fade to sections
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        if (!section.classList.contains('s-hm')) {
            section.classList.add('fade-in-section');
            observer.observe(section);
        }
    });
});
