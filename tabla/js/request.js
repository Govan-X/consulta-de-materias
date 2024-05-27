var data ={}
var xhr = new XMLHttpRequest();
var requestUrl = "https:/cursosapi.com/cursos";
tbody= document.getElementById("tableBodyData");
btnRemove=document.getElementById("btnRemove");
btnRemove.addEventListener("click",function(e){
    tbody.innerHTML = "";
});

//consumir api
function getData(url){
    xhr.open("GET", requestUrl, true); 
    xhr.onload = function(url){
        console.log(xhr.responseText);
        // Handle data
        array = JSON.parse(xhr.responseText);
        data.json=array;
        array.forEach(element => {
            tbody.append(genTr(element));
        });
        console.log(filtered);
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

    td1.innerText = json.idAsignatura;
    td2.innerText = json.claveAsignatura;
    td3.innerText = json.nombreAsignatura;
    td4.innerText = json.grupo;
    td5.innerText = json.profesor;
    td6.innerText = json.salon;
    td7.innerText = json.dia;
    t8.innerText = json.hora;
    td9.innerText = json.lugaresDisponibles;
    tr.append(td1,td2,td3,td4,td5,td6,td7, td8, td9 );
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
