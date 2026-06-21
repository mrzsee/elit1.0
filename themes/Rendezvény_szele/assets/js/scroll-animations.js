document.addEventListener("DOMContentLoaded", function () {
    const revealElements = document.querySelectorAll(".reveal-on-scroll");

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("active");
                // Opcionális: ha csak egyszer akarjuk lejátszani, akkor unobserve
                observer.unobserve(entry.target);
            }
        });
    }, {
        root: null,
        threshold: 0.15, // 15%-a látszódjon az elemnek
        rootMargin: "0px"
    });

    revealElements.forEach((el) => {
        revealObserver.observe(el);
    });
});
