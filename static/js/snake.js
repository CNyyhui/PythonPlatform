document.getElementById('start-button').addEventListener('click', function() {
    fetch('/start_game')
        .then(response => response.json())
        .then(data => {
            document.getElementById('game-status').innerText = data.status;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});