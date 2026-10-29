/**
 * Main JavaScript functionality for Arvin Roman Agramon Portfolio
 */

// Theme Management
(function () {
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark');
    }
})();

function toggleTheme() {
    const isDark = document.documentElement.classList.toggle('dark');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    if (window.lucide) {
        window.lucide.createIcons();
    }
}

// Global Alpine data stores or helper functions
document.addEventListener('DOMContentLoaded', () => {
    // Initialize Lucide icons
    if (window.lucide) {
        window.lucide.createIcons();
    }

    // Auto-dismiss alert notifications after 6 seconds
    const alerts = document.querySelectorAll('.flash-toast');
    alerts.forEach((alert) => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';
            alert.style.transition = 'all 0.4s ease';
            setTimeout(() => alert.remove(), 400);
        }, 6000);
    });
});

// Re-run lucide on Alpine component updates
document.addEventListener('alpine:initialized', () => {
    if (window.lucide) {
        window.lucide.createIcons();
    }
});
