document.addEventListener('DOMContentLoaded', function () {
    const radius = 100; // радиус круга
    const center = {x: 100, y: 100}; // центр круга


    const container = $('.wrapper');
    console.log(container);
    for (let i = 0; i < container.length; i++) {
        container[i].style.position = "relative";
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