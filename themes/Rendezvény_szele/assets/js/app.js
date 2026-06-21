// ==========================================================================
// RENDEZVÉNY SZELE – Main Application JavaScript
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
    console.log('🎪 Rendezvény Szele téma betöltve.');

    // ==========================================
    // SCROLL REVEAL (IntersectionObserver)
    // ==========================================
    const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');

    if (revealElements.length > 0) {
        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            root: null,
            threshold: 0.12,
            rootMargin: '0px 0px -50px 0px'
        });

        revealElements.forEach(el => revealObserver.observe(el));
    }

    // ==========================================
    // ANIMATED COUNTER (Count-up on scroll)
    // ==========================================
    const counterElements = document.querySelectorAll('[data-counter]');

    if (counterElements.length > 0) {
        const counterObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        counterElements.forEach(el => counterObserver.observe(el));
    }

    function animateCounter(element) {
        const target = parseInt(element.getAttribute('data-counter'));
        const suffix = element.getAttribute('data-suffix') || '';
        const duration = 2000;
        const startTime = performance.now();

        function updateCounter(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);

            // Ease-out cubic
            const easeOut = 1 - Math.pow(1 - progress, 3);
            const currentValue = Math.floor(easeOut * target);

            element.textContent = currentValue.toLocaleString('hu-HU') + suffix;

            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            }
        }

        requestAnimationFrame(updateCounter);
    }

    // ==========================================
    // SMOOTH SCROLL for anchor links
    // ==========================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                const navHeight = document.getElementById('main-nav')?.offsetHeight || 80;
                const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY - navHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ==========================================
    // PARALLAX EFFECT (Hero background)
    // ==========================================
    const parallaxElements = document.querySelectorAll('[data-parallax]');

    if (parallaxElements.length > 0) {
        let ticking = false;

        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    const scrollY = window.scrollY;
                    parallaxElements.forEach(el => {
                        const speed = parseFloat(el.getAttribute('data-parallax')) || 0.3;
                        el.style.transform = `translateY(${scrollY * speed}px)`;
                    });
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });
    }

    // ==========================================
    // IMAGE LAZY LOADING with fade-in
    // ==========================================
    const lazyImages = document.querySelectorAll('img[data-src]');

    if (lazyImages.length > 0) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.add('animate-fade-in');
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            });
        }, { rootMargin: '200px' });

        lazyImages.forEach(img => imageObserver.observe(img));
    }

    // ==========================================
    // ACTIVE NAV LINK HIGHLIGHTING
    // ==========================================
    const sections = document.querySelectorAll('section[id]');

    if (sections.length > 0) {
        const navLinks = document.querySelectorAll('#desktop-menu a[href^="#"]');

        const sectionObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const currentId = '#' + entry.target.id;
                    navLinks.forEach(link => {
                        link.classList.remove('font-bold');
                        if (link.getAttribute('href') === currentId) {
                            link.classList.add('font-bold');
                        }
                    });
                }
            });
        }, {
            threshold: 0.3,
            rootMargin: '-80px 0px -50% 0px'
        });

        sections.forEach(section => sectionObserver.observe(section));
    }

    // ==========================================
    // LEFT SLIDE DRAWER WITH GESTURES (Pointer Events)
    // ==========================================
    const drawer = document.getElementById('left-drawer');
    const backdrop = document.getElementById('left-drawer-backdrop');
    const trigger = document.getElementById('left-drawer-trigger');
    const closeBtn = document.getElementById('close-drawer-btn');
    const drawerLinks = document.querySelectorAll('.drawer-link');
    
    if (drawer && backdrop) {
        let isOpen = false;
        let isDragging = false;
        let maybeDragging = false;
        let startX = 0;
        let startY = 0;
        let currentX = 0;
        let currentY = 0;
        
        function getDrawerWidth() {
            return Math.min(280, window.innerWidth * 0.85);
        }
        
        function openDrawer() {
            isOpen = true;
            drawer.style.transition = 'transform 0.3s cubic-bezier(0.16, 1, 0.3, 1)';
            drawer.style.transform = 'translateX(0)';
            backdrop.classList.remove('hidden');
            if (trigger) trigger.style.display = 'none'; // Hide trigger when drawer is open
            setTimeout(() => {
                backdrop.style.opacity = '1';
                backdrop.style.pointerEvents = 'auto';
            }, 10);
            document.body.style.overflow = 'hidden'; // Prevent body scrolling
        }
        
        function closeDrawer() {
            isOpen = false;
            drawer.style.transition = 'transform 0.3s cubic-bezier(0.16, 1, 0.3, 1)';
            drawer.style.transform = 'translateX(-100%)';
            backdrop.style.opacity = '0';
            backdrop.style.pointerEvents = 'none';
            if (trigger) trigger.style.display = ''; // Show trigger when drawer is closed
            setTimeout(() => {
                if (!isOpen) backdrop.classList.add('hidden');
            }, 300);
            document.body.style.overflow = '';
        }
        
        if (closeBtn) {
            closeBtn.addEventListener('click', closeDrawer);
            closeBtn.addEventListener('pointerdown', (e) => e.stopPropagation());
        }
        backdrop.addEventListener('click', closeDrawer);
        backdrop.addEventListener('pointerdown', (e) => {
            e.preventDefault();
            closeDrawer();
        });
        
        drawerLinks.forEach(link => {
            link.addEventListener('click', closeDrawer);
            link.addEventListener('pointerdown', (e) => e.stopPropagation());
        });

        const tab = document.getElementById('left-drawer-tab');
        if (tab) {
            tab.addEventListener('click', (e) => {
                e.stopPropagation();
                openDrawer();
            });

            // Leállítjuk a pulzálást, ha interakció történik az oldalon
            const stopTabPulse = () => {
                tab.classList.remove('pulse-active');
                window.removeEventListener('touchstart', stopTabPulse);
                window.removeEventListener('mousedown', stopTabPulse);
                window.removeEventListener('scroll', stopTabPulse);
            };
            window.addEventListener('touchstart', stopTabPulse, { passive: true });
            window.addEventListener('mousedown', stopTabPulse, { passive: true });
            window.addEventListener('scroll', stopTabPulse, { passive: true });
        }
        
        // Pointer down handler
        function handlePointerDown(e) {
            if (!e.isPrimary) return;
            
            startX = e.clientX;
            startY = e.clientY;
            currentX = startX;
            currentY = startY;
            
            maybeDragging = true;
            isDragging = false;
        }
        
        // Register pointer down listeners
        if (trigger) trigger.addEventListener('pointerdown', handlePointerDown);
        drawer.addEventListener('pointerdown', handlePointerDown);
        
        // Pointer move
        window.addEventListener('pointermove', (e) => {
            if (!maybeDragging && !isDragging) return;
            if (!e.isPrimary) return;
            
            currentX = e.clientX;
            currentY = e.clientY;
            
            const deltaX = currentX - startX;
            const deltaY = currentY - startY;
            
            if (maybeDragging && !isDragging) {
                // Determine if gesture is horizontal and has sufficient distance
                const distX = Math.abs(deltaX);
                const distY = Math.abs(deltaY);
                
                if (distX > 10 && distX > distY) {
                    // Check direction
                    if (!isOpen && deltaX > 0) {
                        // Dragging right to open
                        isDragging = true;
                        drawer.style.transition = 'none';
                        backdrop.classList.remove('hidden');
                    } else if (isOpen && deltaX < 0) {
                        // Dragging left to close
                        isDragging = true;
                        drawer.style.transition = 'none';
                    } else {
                        // Wrong direction
                        maybeDragging = false;
                    }
                } else if (distY > 10) {
                    // Vertical scroll took precedence
                    maybeDragging = false;
                }
            }
            
            if (isDragging) {
                // Prevent browser default actions (like page scrolling or back navigation)
                if (e.cancelable) e.preventDefault();
                
                const width = getDrawerWidth();
                
                if (!isOpen) {
                    // Pulling open: transform from -width to 0
                    let tx = Math.min(0, -width + deltaX);
                    drawer.style.transform = `translateX(${tx}px)`;
                    const progress = Math.min(1, Math.max(0, deltaX / width));
                    backdrop.style.opacity = progress.toString();
                } else {
                    // Pushing closed: transform from 0 to -width
                    let tx = Math.min(0, Math.max(-width, deltaX));
                    drawer.style.transform = `translateX(${tx}px)`;
                    const progress = Math.min(1, Math.max(0, 1 + deltaX / width));
                    backdrop.style.opacity = progress.toString();
                }
            }
        }, { passive: false }); // Needs to be non-passive to allow e.preventDefault()
        
        // Pointer up / cancel
        const handlePointerUp = (e) => {
            if (!e.isPrimary) return;
            if (!maybeDragging && !isDragging) return;
            
            const wasDragging = isDragging;
            maybeDragging = false;
            isDragging = false;
            
            if (wasDragging) {
                const deltaX = currentX - startX;
                const width = getDrawerWidth();
                
                if (!isOpen) {
                    // Open if dragged more than 30% of the drawer width
                    if (deltaX > width * 0.3) {
                        openDrawer();
                    } else {
                        closeDrawer();
                    }
                } else {
                    // Close if dragged left more than 30% of the drawer width
                    if (deltaX < -width * 0.3) {
                        closeDrawer();
                    } else {
                        openDrawer();
                    }
                }
            }
        };
        
        window.addEventListener('pointerup', handlePointerUp);
        window.addEventListener('pointercancel', handlePointerUp);
    }
});
