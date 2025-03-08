document.addEventListener('DOMContentLoaded', function () {
    const codeElement = document.getElementById('code-display');
    const hoverLinks = document.querySelectorAll('.hover-link');
    let hoverTimeout;

    function updateHighlightedLines(lineRange) {
        if (!codeElement) return;

        const [a, b] = lineRange.split('-').map(Number);
        const rows = Array.from(codeElement.querySelector('tbody').children);

        rows.forEach((row, index) => {
            if (index + 1 >= a && index + 1 <= b) {
                row.style.transition = 'opacity 0.3s ease-in-out';
                row.style.opacity = '1.0';
            } else {
                row.style.transition = 'opacity 0.6s ease-in-out';
                row.style.opacity = '0.4';
            }
        });
    }

    hoverLinks.forEach(link => {
        link.addEventListener('mouseenter', function () {
            const lineRange = this.getAttribute('data-lines');
            hoverTimeout = setTimeout(() => {
                updateHighlightedLines(lineRange);
            }, 100);
        });
    });
});
