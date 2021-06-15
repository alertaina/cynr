// VARIABLES
var html_boton_atr_nuevo =`
<label class="control-label text-info" ><b>Atributo Nuevo</b></label>
<div class="form-row">
<div class="col-2">
<button  id="btn_nuevo_atr" type="button" class="btn btn-outline-info btn-block"><i class="fas fa-plus"> </i>
</div>
<div class="col">
<input type="text" placeholder="Nombre del Atributo" name="atributo nuevo" maxlength="250" class="form-control" required id="id_in_atr_nuevo">
</div>
</div>
`
$(document).ready(function(){
    $("#myInput").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#myTable tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
        });
    });
/***********************************************************
FUNCION PARA ARMAR UN CAMPO DEL FORMULARIO DE ATRIBUTOS
************************************************************/
function campo_form(clave,label,contenido){
  if (contenido.length == 0){
 var contenido_html = `
 <label class="control-label" for="id_${clave}"><dt>${label}</dt></label>
 <div class="form-row">
 <div class="col-12">
 <input type="text" name="${label}" maxlength="250" class="form-control atrib" id="id_${clave}" >
 </div>
 </div>`;
  } else {
    var contenido_html = `
    <label class="control-label" for="id_${clave}"><dt>${label}</dt></label>
    <div class="form-row">
    <div class="col-12">
    <select name="${label}" class="form-control atrib" id="id_${clave}">`
    contenido.forEach(elemento => {contenido_html +=`
    <option value="${elemento}">"${elemento}"</option>`
                     });
    contenido_html += `</select>
    </div>
    </div>`;  
  }
 return contenido_html;
}
/***********************************************************
FUNCION PARA ARMAR EL FORMULARIO DE ATRIBUTOS
************************************************************/
function atributos_infra(consulta_categorias){
// AL INICIARSE
/********************************************************/
// Vaciado del contenido de atributos
document.getElementById("atributos_campos").innerHTML="";
// Obtenemos la categoria
clave = $("#id_categoria").val();
// Completamos el formulario con los atributos de base
Object.keys(consulta_categorias[clave]).forEach(key => {
  document.getElementById("atributos_campos").innerHTML += campo_form(key,consulta_categorias[clave][key]["label"],consulta_categorias[clave][key]["valores"]);
});

// CUANDO SE CAMBIE LA CATEGORIA
/********************************************************/
$("#id_categoria").change(function() {
  // Vaciado del contenido de atributos
  document.getElementById("atributos_campos").innerHTML="";
  // Obtenemos la categoria
  clave = $("#id_categoria").val();
  // Completamos el formulario con los atributos de base
  Object.keys(consulta_categorias[clave]).forEach(key => {
    document.getElementById("atributos_campos").innerHTML += campo_form(key,consulta_categorias[clave][key]["label"],consulta_categorias[clave][key]["valores"]);
  });
})};
/***************************************************************************************/

/*****************************************************************************
FUNCION PARA ARMAR EL CAMPO DE UN ATRIBUTO NUEVO EN EL FORMULARIO DE ATRIBUTOS
******************************************************************************/
function atrNuevoForm(nombre){
  var clave = nombre.toLowerCase(); // sustituimos las mayusculas por minusculas
  clave=clave.replace(" ","_"); // cambiamos espacios por linea
  var contenido_html = `
  <div id=id_${clave}_fg class="form-group">
  <div class="col-md-12"><label class="control-label" for="id_${clave}"><dt>${nombre}</dt></label></div>
  <div class="form-row">
  <div class="col-md-11"><input type="text" name="${nombre}" maxlength="250" class="form-control" required id="id_${clave}" ></div>
  <div class="col-md-1"><button class="btn btn-outline-danger btn-block" onclick="document.getElementById('id_${clave}_fg').remove()"><i class="fas fa-minus"></i></button></div>
  </div>
  </div>`;
  var html_contenido_atr_nuevo = `
  <div id=id_${clave}_atr>
    <label class="control-label text-info" ><b>${nombre}</b></label>
    <div class="form-row">
    <div class="col-10"><input type="text" name="${nombre}" maxlength="250" class="form-control atrib" required id="id_${clave}" ></div>
    <div class="col"><button type="button" class="btn btn-outline-danger btn-block" onclick="document.getElementById('id_${clave}_atr').remove()"><i class="fas fa-minus"></i></button></div>
    </div>
  </div>
  `;
 return [html_contenido_atr_nuevo,`id_${clave}`,nombre];
}

/***********************************************************
FUNCION PARA CARGAR LOS ATIRBUTOS DE FORMULARIO EN EL id_atributos
/ campo este que recibe django
************************************************************/
/*function cargarAtr(consulta_categorias){
  document.getElementById("id_atributos").innerHTML="";
  var infra = $('#id_categoria').val();
  var obj_atributos = "{"
  Object.keys(consulta_categorias[infra]).forEach(key => {
    var contenido = $(`#id_${key}`).val();
    obj_atributos += `"${key}":"${contenido}",`;
    });
    obj_atributos = obj_atributos.substring(0, obj_atributos.length - 1); //quitamos la coma de mas
obj_atributos += "}";
document.getElementById("id_atributos").innerHTML +=obj_atributos;
}; */
function cargarAtr(){
  document.getElementById("id_atributos").innerHTML="";
  var atrib_cargados = {};
  var atrib_form = $('.atrib');
  for (var i=0;i<atrib_form.length;i++){
    var clave = atrib_form[i].id;
    var label = atrib_form[i].name;
    var contenido = atrib_form[i].value;
    atrib_cargados[clave]={"label":label,"valores":contenido};
  }
  document.getElementById("id_atributos").innerHTML=JSON.stringify(atrib_cargados);
}
/***********************************************************
FUNCION QUE INICIALIZA EL MAPA DEL FORMULARIO DE ATRIBUTOS
************************************************************/
function map_infra_inicializa(){
          // Layer Here Map
          var here = {
            apiKey:'TrmcsLnJvsLlMjB2vWD1qAIFTVsIMhbezlXDnMc3Omw'
            }
var hereTileUrlhybridday = `https://2.aerial.maps.ls.hereapi.com/maptile/2.1/maptile/newest/hybrid.day/{z}/{x}/{y}/256/png8?apiKey=${here.apiKey}&lg=spa&pview=ARG`
var hereTileUrlnormalday = `https://2.base.maps.ls.hereapi.com/maptile/2.1/maptile/newest/normal.day/{z}/{x}/{y}/512/png8?apiKey=${here.apiKey}&ppi=320&lg=spa&pview=ARG`;
var hybriddayLayer = L.tileLayer(hereTileUrlhybridday);
var normaldayLayer = L.tileLayer(hereTileUrlnormalday);
var baseMaps = {
  "Mapa": normaldayLayer,
  "Satélite": hybriddayLayer,
              };  

var map = L.map('mapid',{drawControl: true,
                        center: [-31.384057, -58.019295],
                        zoom: 5,
                        layers:[normaldayLayer,hybriddayLayer],
                      });
L.control.layers(baseMaps).addTo(map);
L.control.scale({metric:true,imperial:false}).addTo(map);
// add leaflet-geoman controls with some options to the map
map.pm.addControls({
    position: 'topleft',
    drawCircle: false,
    drawRectangle:false,
    drawCircleMarker:false,
                  });
                  
$('#crearItemModal').on('shown.bs.modal', function(){
  map.invalidateSize(); // para que se vea bien el mapa
});
return map;
}

/***********************************************************
FUNCION QUE INICIALIZA EL MAPA PARA VER LA INFRAESTRUCTURA
************************************************************/
function map_ver_infra_inicializa(geometria){
  // Layer Here Map
  var here = {
    apiKey:'TrmcsLnJvsLlMjB2vWD1qAIFTVsIMhbezlXDnMc3Omw'
    }
var hereTileUrlhybridday = `https://2.aerial.maps.ls.hereapi.com/maptile/2.1/maptile/newest/hybrid.day/{z}/{x}/{y}/256/png8?apiKey=${here.apiKey}&lg=spa&pview=ARG`
var hereTileUrlnormalday = `https://2.base.maps.ls.hereapi.com/maptile/2.1/maptile/newest/normal.day/{z}/{x}/{y}/512/png8?apiKey=${here.apiKey}&ppi=320&lg=spa&pview=ARG`;
var hybriddayLayer = L.tileLayer(hereTileUrlhybridday);
var normaldayLayer = L.tileLayer(hereTileUrlnormalday);
var baseMaps = {
"Mapa": normaldayLayer,
"Satélite": hybriddayLayer,
      };  

var map = L.map('mapid',{drawControl: true,
                center: [-31.384057, -58.019295],
                zoom: 5,
                layers:[normaldayLayer,hybriddayLayer],
              });
L.control.layers(baseMaps).addTo(map);
L.control.scale({metric:true,imperial:false}).addTo(map);
var dato = { "type": "GeometryCollection", "geometries": [ { "type": "Point", "coordinates": [ -57.336444854736335, -27.42373798589281 ] } ] }
L.geoJSON(geometria).addTo(map);          
$('#crearItemModal').on('shown.bs.modal', function(){
map.invalidateSize(); // para que se vea bien el mapa
});
return map;
}

/***********************************************************
FUNCION QUE INICIALIZA EL MAPA PARA EL VISOR
************************************************************/
function map_visual_inicializa(){
  // Layer Here Map
  var here = {
    apiKey:'TrmcsLnJvsLlMjB2vWD1qAIFTVsIMhbezlXDnMc3Omw'
    }
var hereTileUrlhybridday = `https://2.aerial.maps.ls.hereapi.com/maptile/2.1/maptile/newest/hybrid.day/{z}/{x}/{y}/256/png8?apiKey=${here.apiKey}&lg=spa&pview=ARG`
var hereTileUrlnormalday = `https://2.base.maps.ls.hereapi.com/maptile/2.1/maptile/newest/normal.day/{z}/{x}/{y}/512/png8?apiKey=${here.apiKey}&ppi=320&lg=spa&pview=ARG`;
var hybriddayLayer = L.tileLayer(hereTileUrlhybridday);
var normaldayLayer = L.tileLayer(hereTileUrlnormalday);
var baseMaps = {
"Mapa": normaldayLayer,
"Satélite": hybriddayLayer,
      };  

var map = L.map('mapid',{
                center: [-31.384057, -58.019295],
                zoom: 5,
                layers:[normaldayLayer,hybriddayLayer],
              });
L.control.layers(baseMaps).addTo(map);
L.control.scale({metric:true,imperial:false}).addTo(map);
L.geoJSON(geometria).addTo(map);          
$('#crearItemModal').on('shown.bs.modal', function(){
map.invalidateSize(); // para que se vea bien el mapa
});
return map;
}

/******************************************************
FUNCION PARA ARMAR CADENA DE TEXTO CON EL FORMATO KWT
PARA GUARDAR LA GEOMETRIA EN LA BASE DE DATOS
*******************************************************/
function cargarGeo(map) {
wkt_collection = "GEOMETRYCOLLECTION(";
var geom = map.pm.getGeomanLayers();
if (geom.length > 0){ // chequea si se agregó algo a la geometria
  geom.forEach(function(item){
    switch (item["pm"]["_shape"]) {
        case "Marker":
        wkt_collection = wkt_collection + "POINT("+item["_latlng"]["lng"]+" "+item["_latlng"]["lat"]+"),"; 
        break;
        case "Line":
        var line_points ="LINESTRING(";
        item["_latlngs"].forEach(coord => line_points = line_points + coord["lng"] + " " + coord["lat"]+ ",")
        line_points = line_points.substring(0,line_points.length-1); // quitamos la ultima coma que no va y genera un error en el GEOSGeometry() de django
        line_points = line_points + "),";
        wkt_collection = wkt_collection + line_points;       
        break;
        case "Polygon":
        var first_point = item["_latlngs"][0][0].lng + " " + item["_latlngs"][0][0].lat // primer punto del poligono para repetir al final
        var polig_points = "POLYGON(("
        item["_latlngs"][0].forEach(coord => polig_points = polig_points + coord["lng"] + " " + coord["lat"]+ ",")
        polig_points = polig_points + first_point ; // repetimos el primer punto
        polig_points = polig_points + ")),";
        wkt_collection = wkt_collection + polig_points;       
        break;
    }
  })
  wkt_collection = wkt_collection.substring(0,wkt_collection.length-1); // quitamos la ultima coma que no va y genera un error en el GEOSGeometry() de django
  wkt_collection = wkt_collection + ")";
  return wkt_collection;}
  else {
    return ""; 
  }
                        }
// PRUEBA PARA OBTENER EL VALOR SELECCIONADO EN UNA OPCION DE UN SELECT
$(document).ready(function(){
  $('select#id_uso').on('change',function(){
    var valor = $(this).val();
    alert(valor);
});
});
