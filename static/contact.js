function validateForm() {
    var nombre = document.getElementById("nombre").value;
    var correo = document.getElementById("correo").value;
    var asunto = document.getElementById("asunto").value;
    var mensaje = document.getElementById("mensaje").value;

    if (nombre === "") {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Por favor, ingrese su nombre.',
        });
        return false;
    }

    if (correo === "") {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Por favor, ingrese su correo electrónico.',
        });
        return false;
    }

    if (asunto === "") {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Por favor, ingrese el asunto.',
        });
        return false;
    }

    if (mensaje === "") {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Por favor, ingrese un mensaje.',
        });
        return false;
    }

    return true;
}
