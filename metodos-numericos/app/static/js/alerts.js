function showAlert(message) {
    document.getElementById('alertText').textContent = message;
    document.getElementById('alert').classList.remove('hidden');
}

function closeAlert() {
    document.getElementById('alertText').textContent = '';
    document.getElementById('alert').classList.add('hidden');
}