// Altera a cor do link quando o mouse passa sobre ele
document.querySelector('a').addEventListener('mouseover', function() {
    this.style.color = 'blue';
});

// Restaura a cor original do link quando o mouse sai dele
document.querySelector('a').addEventListener('mouseout', function() {
    this.style.color = 'black';
});

// Adiciona um evento de clique ao botão "start-recognition" - iniciar reconhecimento
document.getElementById('start-recognition').addEventListener('click', () => {
    // Obtém o valor do campo de email
    const email = document.getElementById('email').value;
    // Verifica se o campo de email está vazio
    if (!email) {
        alert('Por favor, preencha o campo de email.');
        return;
    }
    // Exibe a seção da câmera
    document.getElementById('camera-section').style.display = 'block';
    // Obtém o elemento de vídeo
    const video = document.getElementById('video');
    // Solicita acesso à webcam do usuário
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            // Exibe a transmissão de vídeo no elemento de vídeo
            video.srcObject = stream;
        })
        .catch(err => {
            console.error('Erro ao acessar a webcam:', err);
        });
});

// Adiciona um evento de clique ao botão "capture"
document.getElementById('capture').addEventListener('click', () => {
    // Obtém o valor do campo de email
    const email = document.getElementById('email').value;
    // Verifica se o campo de email está vazio
    if (!email) {
        alert('Por favor, preencha o campo de email.');
        return;
    }
    // Obtém o elemento de vídeo
    const video = document.getElementById('video');
    // Cria um canvas para capturar uma imagem do vídeo
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    // Desenha o frame atual do vídeo no canvas
    canvas.getContext('2d').drawImage(video, 0, 0);
    // Converte a imagem do canvas em formato base64
    const faceData = canvas.toDataURL('image/png');
    // Exibe os dados do email e da imagem capturada (apenas para depuração)
    console.log(`Email: ${email}`);
    console.log(`Dados da Face: ${faceData}`);
    // Envia os dados do email e da imagem capturada para o servidor
    fetch('/login_capture', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            face_data: faceData,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Exibe uma mensagem de sucesso ou erro com base na resposta do servidor
        if (data.status === 'success') {
            alert(data.message);
            window.location.href = data.redirect;
        } else {
            alert(data.message);
        }
    })
    .catch(err => {
        console.error('Erro durante a requisição:', err);
    });
});