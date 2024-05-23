document.addEventListener('DOMContentLoaded', function () {
    let radius = 115; // радиус круга
    let center = {x: 115, y: 115}; // центр круга


    const container = $('.wrapper');
    console.log(container);
    for (let i = 0; i < container.length; i++) {
        container[i].style.position = "relative";
        if (".bw" in container[i].classList) {
            radius = 140; // радиус круга
            center = {x: 140, y: 140};
        }
    }

    for (let i = 0; i < container.length; i++) {
        const angle = (Math.PI * 2 / container.length) * i;
        const x = center.x + radius * Math.cos(angle);
        const y = center.y + radius * Math.sin(angle);
        container[i].style.position = 'absolute';
        container[i].style.left = x + 'px';
        container[i].style.top = y + 'px';
    }
});