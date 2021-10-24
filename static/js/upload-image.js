const input_perfil_img = document.getElementById("input-upload-image")
const perfil_image = document.getElementById("perfil-image")

function remove_url_image(){
    URL.revokeObjectURL(perfil_image.src)
}

function upload_image(event){
    perfil_image.src = URL.createObjectURL(event.target.files[0])
    perfil_image.onload = remove_url_image
}

input_perfil_img.addEventListener('input', upload_image)