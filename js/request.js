var data ={}
var xhr = new XMLHttpRequest();
var requestUrl = "http://127.0.0.1:5000/cursos";
tbody= document.getElementById("tableBodyData");
btnRemove=document.getElementById("btnRemove");
btnRemove.addEventListener("click",function(e){
    tbody.innerHTML = "";
});
xhr.addEventListener('load', (datos) => {
    console.log('Datos recibidos');
    });
xhr.addEventListener('error', () => {
    console.log('Error, imposible conectar');
});
//consumir api
function getData(url){
    xhr.open("GET", requestUrl, true); 
    xhr.onload = function(url){
         console.log(xhr.responseText);
        // Handle data
        try{
        array = JSON.parse(xhr.responseText);
        data.json=array;
        data.forEach(element => {
            tbody.append(genTr(element));
        });
    }catch (error){
        console.error("error al obtener los datos", error);
    }
    };
    xhr.send(); 
}
function genTr(json) {
    tr = document.createElement("tr");
    td1 = document.createElement("td");
    td2 = document.createElement("td");
    td3 = document.createElement("td");
    td4 = document.createElement("td");
    td5 = document.createElement("td");
    td6 = document.createElement("td");
    td7 = document.createElement("td");
    td8 = document.createElement("td");
    td9 = document.createElement("td");

    td1.innerText = json.idAsignaturas;
    td2.innerText = json.claveAsignatura;
    td3.innerText = json.nombreAsignatura;
    td4.innerText = json.grupo;
    td5.innerText = json.profesor;
    td6.innerText = json.salon;
    td7.innerText = json.dia;
    t8.innerText = json.hora;
    td9.innerText = json.lugaresDisponibles;
    tr.append(td1,td2,td3,td4,td5,td6,td7,td8,td9);
    return tr;
}

btcLoad = document.getElementById("btnLoad")
btnLoad.addEventListener("click", function(e){
    getData();
})

btnSearch = document.getElementById("btnSearch");
input = document.getElementById("inputSearch");
btnSearch.addEventListener("click",function(e){
    tbody.innerHTML="";
    filtered = data.json.filter(e=>e.title.includes(input.value));
    filtered.forEach(function(i){
        tbody.append( genTr(i));
    });
});


getData();

//console.log(filtered);
