
document.addEventListener('DOMContentLoaded', () => {
    const heartBtn = document.getElementById('heartBtn');

    heartBtn.addEventListener('click', () => {
        createHearts();
    });
});

function createHearts() {
    const heart = document.createElement('div');
    heart.classList.add('heart');
    heart.style.left = `${Math.random() * 100}%`; // Posición horizontal aleatoria
    document.body.appendChild(heart);

    // Eliminar el corazón después de un tiempo
    setTimeout(() => {
        heart.remove();
    }, 4000); // Tiempo en milisegundos (4 segundos)
}