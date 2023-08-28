document.addEventListener('DOMContentLoaded', () => {
    const socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('message', data => {
        const container = document.getElementById('data-container');
        container.innerHTML = `Received: ${data.data}`;
    });
});
