document.addEventListener('DOMContentLoaded', function() {
    // テーマ切り替え機能
    const themeToggleButton = document.getElementById('theme-toggle-button');
    const htmlElement = document.documentElement;

    // localStorageからテーマを読み込む
    const savedTheme = localStorage.getItem('pico-theme') || 'light';
    htmlElement.setAttribute('data-theme', savedTheme);
    updateButtonText();

    themeToggleButton.addEventListener('click', () => {
        let currentTheme = htmlElement.getAttribute('data-theme');
        if (currentTheme === 'light') {
            htmlElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('pico-theme', 'dark');
        } else {
            htmlElement.setAttribute('data-theme', 'light');
            localStorage.setItem('pico-theme', 'light');
        }
        updateButtonText();
    });

    function updateButtonText() {
        const currentTheme = htmlElement.getAttribute('data-theme');
        if (currentTheme === 'light') {
            themeToggleButton.textContent = 'dark mode';
        } else {
            themeToggleButton.textContent = 'light mode';
        }
    }
});
