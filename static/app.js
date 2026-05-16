console.log('Pathukkalam App Loaded');

if ('serviceWorker' in navigator) {

    window.addEventListener('load', function() {

        navigator.serviceWorker.register('/static/sw.js')

        .then(function(registration) {
            console.log('SW registered');
        })

        .catch(function(error) {
            console.log('SW failed');
        });

    });
}
