// Aguarda o carregamento completo do documento HTML antes de executar o código
document.addEventListener('DOMContentLoaded', () => {
    // Obtém referências para o botão de captura e o elemento de vídeo
    const captureButton = document.getElementById('capture');
    const video = document.getElementById('video');

    // Acessa a webcam do usuário
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            // Exibe o stream de vídeo no elemento de vídeo
            video.srcObject = stream;
        })
        .catch(err => {
            // Exibe um erro caso não seja possível acessar a webcam
            console.error('Erro ao acessar a webcam:', err);
        });

    // Adiciona um evento de clique ao botão de captura
    captureButton.addEventListener('click', () => {
        // Cria um canvas para capturar a imagem do vídeo
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        // Desenha o frame atual do vídeo no canvas
        canvas.getContext('2d').drawImage(video, 0, 0);
        // Converte a imagem do canvas em formato base64
        const faceData = canvas.toDataURL('image/png');

        // Envia os dados do email e da imagem capturada para o servidor
        fetch('/register_capture', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email: document.querySelector('.email-display').innerText.split('Email: ')[1],
                face_data: faceData,
            }),
        })
        .then(response => response.json())
        .then(data => {
            // Exibe uma mensagem de sucesso ou erro com base na resposta do servidor
            if (data.status === 'success') {
                alert(data.message);
                window.location.href = '/login';
            } else {
                alert(data.message);
            }
        })
        .catch(error => {
            console.error('Erro:', error);
        });
    });
});