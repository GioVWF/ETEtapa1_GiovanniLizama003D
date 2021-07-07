$(function() 
        {
            $("#form_validar").validate({
                rules: {
                    nombre: {
                        required: true,
                        minlength: 3,
                    },
                    apellidos: {
                        required: true,
                        minlength: 5,
                    },
                    correo: {
                        required: true,
                        email: true
                    },
                    telefono: {
                        required: true,
                    },
                    mensajeC: {
                        required: true,
                        minlength: 15
                    },
                },
                messages: {
                    nombre: {
                        required: "Por favor ingresa tu nombre.",
                        minlength: "Debes ingresar como mínimo 3 caracteres.",
                    },
                    apellidos: {
                        required: "Por favor ingresa tus apellidos.",
                        minlength: "Debes ingresar como mínimo 5 caracteres.",
                    },
                    correo: {
                        required: "Por favor ingresa tu correo electronico.",
                        email: "Ingresa un correo válido."
                    },
                    telefono : {
                        required: "Por favor ingresa tu teléfono",
                    },
                    mensajeC : {
                        required: "Por favor ingresa un mensaje.",
                        minlength: "Debes ingresar como mínimo 15 caracteres."
                    }
                }
            });
        });

        function Cambiarnombre()
        {
            var a = document.getElementById("nom");
            a.value = a.value.toUpperCase();
        }
        function CambiarNombrefoto()
        {
            var a = document.getElementById("nomF");
            a.value = a.value.charAt(0).toUpperCase()+a.value.slice(1).toLowerCase();      
        }
        function  CambiarEmail()
        {
            var a = document.getElementById("email");
            a.value = a.value.toLowerCase();
        }
function validacion()
{
    var nom, email, nom1, asunto, mensaje ;

    nom = document.getElementById("nom").value;
    email = document.getElementById("email").value;
    nom1 = document.getElementById("nomF").value;
    asunto = document.getElementById("Asunto").value;
    mensaje = document.getElementById("mensaje").value;

    if (nom == null || nom == ""){
    alert("Debe ingresar un nickname");
    document.datos.nom.focus();
    return false;
    }
    if (email == null || email ==""){
    alert("Debe ingresar un email")
    document.datos.email.focus();
    return false;
    }
    if (nom1 == null || nom == ""){
    alert("Debe ingresar un nombre para la foto");
    document.datos.nom1.focus();
    return false;
    }
    if (asunto == null || nom == ""){
    alert("Debe seleccionar una categoria");
    document.datos.asunto.focus();
    return false;
    }
    if (mensaje == null || mensaje == ""){
    alert("Debe escribir un mensaje")
    document.datos.mensaje.focus();
    return false;
    }
    return true;

}        