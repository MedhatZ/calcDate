function startConfetti() {
    const canvas = document.getElementById("confetti");
    const ctx = canvas.getContext("2d");

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    let pieces = [];

    const colors = ["#ff0a54", "#ff477e", "#ff7096", "#fbb1bd", "#ffd6e0"];

    for (let i = 0; i < 150; i++) {
        pieces.push({
            x: Math.random() * canvas.width,
            y: -Math.random() * canvas.height,   // 👈 يبدأ من فوق
            r: Math.random() * 6 + 2,
            speed: Math.random() * 4 + 2,
            color: colors[Math.floor(Math.random() * colors.length)]
        });
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        pieces.forEach(p => {
            ctx.fillStyle = p.color;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
            ctx.fill();

            p.y += p.speed;

            if (p.y > canvas.height) {
                p.y = -10; // 👈 يرجع من فوق تاني
                p.x = Math.random() * canvas.width;
            }
        });

        requestAnimationFrame(draw);
    }

    draw();
}