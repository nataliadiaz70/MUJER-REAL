document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevenir el envío del formulario hasta que se valide

    let isValid = true;
    const fields = ['nombre', 'email', 'telefono', 'motivo'];
    fields.forEach(function(field) {
        const input = document.getElementById(field);
        if (!input.value) {
            isValid = false;
            input.style.borderColor = 'red';
        } else {
            input.style.borderColor = '#ccc';
        }
    });

    const radios = document.getElementsByName('noticias');
    let radioChecked = false;
    radios.forEach(function(radio) {
        if (radio.checked) {
            radioChecked = true;
        }
    });
    if (!radioChecked) {
        isValid = false;
        radios[0].parentElement.style.color = 'red';
    } else {
        radios[0].parentElement.style.color = 'black';
    }

    const checkbox = document.getElementById('terminos');
    if (!checkbox.checked) {
        isValid = false;
        checkbox.parentElement.style.color = 'red';
    } else {
        checkbox.parentElement.style.color = 'black';
    }

    if (isValid) {
        alert('Formulario enviado correctamente');
        // Aquí puedes agregar la lógica para enviar el formulario
    } else {
        alert('Por favor, complete todos los campos obligatorios');
    }
});
