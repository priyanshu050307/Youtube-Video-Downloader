document.getElementById('videoBtn').addEventListener('click', function () {
    download('video');
});

document.getElementById('audioBtn').addEventListener('click', function () {
    download('audio');
});

function download(type) {
    const url = document.getElementById('url').value;
    if (!url) {
        alert('Please enter a valid YouTube URL.');
        return;
    }

    const formData = new FormData();
    formData.append('url', url);

    const endpoint = type === 'video' ? '/download_video' : '/download_audio';

    fetch(endpoint, {
        method: 'POST',
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            const status = document.getElementById('status');
            status.textContent = data.message;
            status.style.color = data.status === 'success' ? 'green' : 'red';
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}
