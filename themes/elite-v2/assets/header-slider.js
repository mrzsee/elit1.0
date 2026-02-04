document.addEventListener("DOMContentLoaded", function () {
    const headerBg = document.querySelector('.s-hn .s-bg-l');
    if (!headerBg) return;

    // Használja a pontos útvonalat
    const assetBase = (typeof THEME_ASSETS_URL !== 'undefined') ? THEME_ASSETS_URL : 'themes/elite-v2/assets/';
    console.log("Slider Path:", assetBase);

    const images = ['header_bg.png', 'header_slider_1.png', 'header_slider_2.png', 'header_slider_3.png', 'header_slider_4.png', 'header_slider_5.png'];

    // Töröljük az eredeti hátteret
    headerBg.style.backgroundImage = 'none';

    // Slide rétegek
    const s1 = document.createElement('div');
    const s2 = document.createElement('div');

    [s1, s2].forEach(d => {
        d.style.position = 'absolute'; d.style.top = '0'; d.style.left = '0';
        d.style.width = '100%'; d.style.height = '100%';
        d.style.backgroundSize = '100% auto'; d.style.backgroundPosition = 'center top';
        d.style.backgroundRepeat = 'no-repeat'; d.style.transition = 'opacity 1.5s ease-in-out';
        headerBg.appendChild(d);
    });

    // Kezdőállapot
    let idx = 0;
    s1.style.backgroundImage = `url('${assetBase}${images[0]}')`; s1.style.opacity = '1'; s1.style.zIndex = '2';
    s2.style.backgroundImage = `url('${assetBase}${images[1]}')`; s2.style.opacity = '0'; s2.style.zIndex = '1';

    setInterval(() => {
        const nextIdx = (idx + 1) % images.length;
        const url = `url('${assetBase}${images[nextIdx]}')`;

        if (s1.style.opacity === '1') {
            s2.style.backgroundImage = url;
            s2.style.zIndex = '2'; s1.style.zIndex = '1';
            s2.style.opacity = '1'; s1.style.opacity = '0';
        } else {
            s1.style.backgroundImage = url;
            s1.style.zIndex = '2'; s2.style.zIndex = '1';
            s1.style.opacity = '1'; s2.style.opacity = '0';
        }
        idx = nextIdx;
    }, 3000);
});
