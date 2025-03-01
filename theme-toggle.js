const button = document.getElementById('theme-toggle'); // button
const lightTheme = document.getElementById('light-theme'); // css sheet
const darkTheme = document.getElementById('dark-theme'); // css sheet

// Check for saved theme preference or default to light
const savedTheme = localStorage.getItem('theme') || 'light';
document.body.setAttribute('data-theme', savedTheme);

// Set initial theme based on saved preference
if (savedTheme === 'dark') {
    darkTheme.disabled = false;
    lightTheme.disabled = true;
} else {
    darkTheme.disabled = true;
    lightTheme.disabled = false;
}

button.addEventListener('click', () => {
    // Add a class for animation during transition
    button.classList.add('animating');

    // If moon theme is currently active, switch to solarized theme
    if (darkTheme.disabled) {
        // Set a small delay to allow the animation to complete
        setTimeout(() => {
            darkTheme.disabled = false;  // Enable the moon theme
            lightTheme.disabled = true; // Disable the solarized theme
            document.body.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
        }, 150);
    } else {
        setTimeout(() => {
            darkTheme.disabled = true;   // Disable the moon theme
            lightTheme.disabled = false; // Enable the solarized theme
            document.body.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
        }, 150);
    }

    // Remove the animation class after transition
    setTimeout(() => {
        button.classList.remove('animating');
    }, 300);
});