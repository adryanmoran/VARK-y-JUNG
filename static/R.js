
    document.addEventListener('DOMContentLoaded', function () {
        const form = document.querySelector('form');

        form.addEventListener('submit', function (event) {
            event.preventDefault();

            const nombre = document.querySelector('input[name="nombre"]').value;
            const apellido_paterno = document.querySelector('input[name="apellido_paterno"]').value;
            const apellido_materno = document.querySelector('input[name="apellido_materno"]').value;
            const telefono = document.querySelector('input[name="telefono"]').value;
            const correo = document.querySelector('input[name="correo"]').value;
            const id_puesto = document.querySelector('select[name="id_puesto"]').value;

            if (nombre.trim() === '') {
                Swal.fire('Error', 'Por favor, ingresa un nombre válido.', 'error');
            } else if (apellido_paterno.trim() === '') {
                Swal.fire('Error', 'Por favor, ingresa un apellido paterno válido.', 'error');
            } else if (apellido_materno.trim() === '') {
                Swal.fire('Error', 'Por favor, ingresa un apellido materno válido.', 'error');
            } else if (telefono.trim() === '') {
                Swal.fire('Error', 'Por favor, ingresa un número de teléfono válido.', 'error');
            } else if (correo.trim() === '') {
                Swal.fire('Error', 'Por favor, ingresa un correo electrónico válido.', 'error');
            } else if (id_puesto.trim() === '') {
                Swal.fire('Error', 'Por favor, selecciona un puesto válido.', 'error');
            } else {
                // Si todos los campos están completos, puedes enviar el formulario
                form.submit();
            }
        });
    });

