function guardar() {
    var Titulo = document.getElementById('Titulo').value
    var Descripcion = document.getElementById('Descripcion').value
    var Genero = document.getElementById('Genero').value
    var fila="<tr><td>"+Titulo+"</td><td>"+Descripcion +"</td><td>"+Genero+"</td></tr>";
    var btn = document.createElement("tr");
   	btn.innerHTML=fila;
    document.getElementById("registro").appendChild(btn);
}