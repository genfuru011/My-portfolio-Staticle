document.addEventListener('DOMContentLoaded', function() {
    // ハンバーガーメニュー機能
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const navMenu = document.querySelector('.nav-menu');

    if (hamburgerMenu && navMenu) {
        hamburgerMenu.addEventListener('click', function() {
            hamburgerMenu.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // メニューのリンクをクリックしたらメニューを閉じる
        const menuLinks = navMenu.querySelectorAll('a');
        menuLinks.forEach(link => {
            link.addEventListener('click', function() {
                hamburgerMenu.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });

        // ウィンドウサイズが変更されたとき、ハンバーガーメニューの状態をリセット
        window.addEventListener('resize', function() {
            if (window.innerWidth > 768) {
                hamburgerMenu.classList.remove('active');
                navMenu.classList.remove('active');
            }
        });
    }
});
