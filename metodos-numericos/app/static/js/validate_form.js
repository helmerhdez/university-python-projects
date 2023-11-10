import showAlert from alerts.js

function validateForm(form) {
    event.preventDefault();
    var fields = form.getElementsByTagName('input');
    for (var i = 0; i < fields.length; i++) {
        var field = fields[i];
        if (field.value === '') {
            showAlert(`Por favor, complete el campo ${field.name} antes de enviar el formulario.`);
        return;
    }
}
    form.submit();
}