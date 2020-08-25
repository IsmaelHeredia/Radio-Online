var reproductor = null;

var id_emisora = "";
var nombre_emisora = "";
var url_emisora = "";
var generos_emisora = "";
var string_emisora = "";

var en_linea = false;

window["volumenBtn"] = document.getElementById("volumenBtn");
window["volumen"] = document.getElementById("volumen");
window["deslizarBtn"] = document.getElementById("deslizarBtn");

$(document).ready(function() {

  $('#btnBuscar').on("click", function() {

    $('#mensaje').text("");

    if(nombre_emisora != "") {
      if(en_linea == true) {
        detener();
      } else {
        detener_reproductor();
      }
    } else {
      detener_reproductor();
    }

    $("#listaEmisoras > tbody").html("");

    $.each(emisoras, function(index, value) {
      var id = value.id;
      var nombre = value.nombre;
      var url = value.url;
      var generos = value.generos;
      var string = value.string;
      $('#listaEmisoras').append('<tr class="itemSeleccionado"> \
              <td class="ocultar">' + id + '</td> \
              <td>' + nombre + '</td> \
              <td class="ocultar">' + url + '</td> \
              <td>' + generos + '</td> \
              <td class="ocultar">' + string + '</td> \
      </tr>');
    });

    if(emisoras.length == 0) {
      $('#mensaje').text("No se encontraron emisoras");
    }

    $('#modal_buscador').modal('show');
  });

  $("#listaEmisoras").on("click", "tr", function() {
    $('#modal_buscador').modal('hide');
    id_emisora = $(this).closest('tr').find('td:nth-child(1)').text();
    nombre_emisora = $(this).closest('tr').find('td:nth-child(2)').text();
    url_emisora = $(this).closest('tr').find('td:nth-child(3)').text();
    generos_emisora = $(this).closest('tr').find('td:nth-child(4)').text();
    string_emisora = $(this).closest('tr').find('td:nth-child(5)').text();
    if(nombre_emisora != "") {
      $("#titulo").text("Cargado : " + nombre_emisora);
    }
  });

  $('#buscarTexto').on('input', function() {
    $('#mensaje').text("");
    $("#listaEmisoras > tbody").html("");
    var encontrado = false;
    $.each(emisoras, function(index, value) {
      var patron = $('#buscarTexto').val().toLowerCase();
      var id = value.id;
      var nombre = value.nombre;
      var url = value.url;
      var generos = value.generos;
      var string = value.string.toLowerCase();
      if(string.indexOf(patron) !== -1) {
        $('#listaEmisoras').append('<tr class="itemSeleccionado"> \
                <td class="ocultar">' + id + '</td> \
                <td>' + nombre + '</td> \
                <td class="ocultar">' + url + '</td> \
                <td>' + generos + '</td> \
                <td class="ocultar">' + string + '</td> \
        </tr>');
        encontrado = true;
      }
    });

    if(encontrado == false) {
      $('#mensaje').text("No se encontraron emisoras");
    }

  });

  $('#btnReproducir').on("click", function() {
    reproducir();
  });

  $('#btnDetener').on("click", function() {
    detener();
  });

  $('#btnRetroceder').on("click", function() {
    retroceder();
  });

  $('#btnAdelantar').on("click", function() {
    adelantar();
  });  

});

function cargarEmisoras() {
  var idata;

  $.ajax({
    type: 'GET',
    url: "emisoras/listaJson",
    data: {},
    dataType: 'json',
    async: false,
    success: function(result){idata = result;}
  });

  return idata;
}

function cargarIdsEmisoras() {
  var ids = [];
  $.each(emisoras, function(index, value) {
    var id = value.id;
    ids.push(id);
  });
  return ids;
}

function reproducir() {

  if(url_emisora == "") {
    toastr.warning("Seleccione una emisora");
  }
  else if(en_linea == true) {
    toastr.warning("El reproductor ya esta iniciado");
  } else {
    reproductor = new Howl({
      src: [url_emisora],
      html5: true,
      format: ["mp3", "aac"],
      onplay: function() {
        wave.container.style.display = "block";
        barra.style.display = "none";

        $("#titulo").text("Reproduciendo : " + nombre_emisora);

        btnReproducir.style.display = "none";
        btnDetener.style.display = "block";
    
        en_linea = true;
      },
      onend: function() {
        wave.container.style.display = "none";
        barra.style.display = "block";
      },
      onstop: function() {
        wave.container.style.display = "none";
        barra.style.display = "block";
      },
      onloaderror: function(error) {
        toastr.error("Ha ocurrido un error en la reproducción");
      }
    });

    reproductor.play();
  }
}

function detener_reproductor() {
  if(reproductor != null) {
    reproductor.stop();
    reproductor.unload();
    reproductor = null;
    btnReproducir.style.display = "block";
    btnDetener.style.display = "none";
    en_linea = false;
  }
}

function detener() {
  if(reproductor != null && en_linea != false) {
    detener_reproductor();
    $("#titulo").text("Seleccione una emisora");
    id_emisora = "";
    nombre_emisora = "";
    url_emisora = "";
    generos_emisora = "";
    string_emisora = "";
  } else {
    toastr.warning("El reproductor no está iniciado");
  }
}

function retroceder() {
  if(url_emisora == "") {
    toastr.warning("Seleccione una emisora");
  } else {
    var index_emisora = ids_emisoras.indexOf(parseInt(id_emisora));
    if(index_emisora <= 0) {
      toastr.warning("No se puede seguir retrocediendo");
    } else {
      var id_emisora_atras = emisoras[index_emisora - 1];
      $.each(emisoras, function(index, value) {
        if(id_emisora_atras.id == value.id) {
          id_emisora = value.id;
          nombre_emisora = value.nombre;
          url_emisora = value.url;
          generos_emisora = value.generos;
          string_emisora = value.string;
          detener_reproductor();
          $("#titulo").text("Cargado : " + nombre_emisora);
        }
      });
    }
  }
}

function adelantar() {
  if(url_emisora == "") {
    toastr.warning("Seleccione una emisora");
  } else {
    var index_emisora = ids_emisoras.indexOf(parseInt(id_emisora));
    if(index_emisora >= emisoras.length - 1) {
      toastr.warning("No se puede seguir adelantando");
    } else {
      var id_emisora_adelante = emisoras[index_emisora + 1];
      $.each(emisoras, function(index, value) {
        if(id_emisora_adelante.id == value.id) {
          id_emisora = value.id;
          nombre_emisora = value.nombre;
          url_emisora = value.url;
          generos_emisora = value.generos;
          string_emisora = value.string;
          detener_reproductor();
          $("#titulo").text("Cargado : " + nombre_emisora);
        }
      });
    }
  }
}
    
function seleccionarVolumen(val) {
  Howler.volume(val);
  var barraAncho = (val * 90) / 100;
  barraCompleta.style.width = (barraAncho * 100) + '%';
  deslizarBtn.style.left = (window.innerWidth * barraAncho + window.innerWidth * 0.05 - 25) + 'px';
}

function mostrarBarraVolumen() {
  var display = (volumen.style.display === 'block') ? 'none' : 'block';

  setTimeout(function() {
    volumen.style.display = display;
  }, (display === 'block') ? 0 : 500);

  volumen.className = (display === 'block') ? 'fundir' : 'desvanecer';
}

volumenBtn.addEventListener('click', function() {
  mostrarBarraVolumen();
});
volumen.addEventListener('click', function() {
  mostrarBarraVolumen();
});

barraVacia.addEventListener('click', function(event) {
  var per = event.layerX / parseFloat(barraVacia.scrollWidth);
  seleccionarVolumen(per);
});
deslizarBtn.addEventListener('mousedown', function() {
  window.sliderDown = true;
});
deslizarBtn.addEventListener('touchstart', function() {
  window.sliderDown = true;
});
volumen.addEventListener('mouseup', function() {
  window.sliderDown = false;
});
volumen.addEventListener('touchend', function() {
  window.sliderDown = false;
});

var mover = function(event) {
  if (window.sliderDown) {
    var x = event.clientX || event.touches[0].clientX;
    var startX = window.innerWidth * 0.05;
    var layerX = x - startX;
    var per = Math.min(1, Math.max(0, layerX / parseFloat(barraVacia.scrollWidth)));
    seleccionarVolumen(per);
  }
};

volumen.addEventListener('mousemove', mover);
volumen.addEventListener('touchmove', mover);

var wave = new SiriWave({
  container: animacion,
  width: window.innerWidth,
  height: window.innerHeight * 0.3,
  cover: true,
  speed: 0.03,
  amplitude: 0.7,
  frequency: 2
});

wave.start();

var dimensionar = function() {
  var height = window.innerHeight * 0.3;
  var width = window.innerWidth;
  wave.height = height;
  wave.height_2 = height / 2;
  wave.MAX = wave.height_2 - 4;
  wave.width = width;
  wave.width_2 = width / 2;
  wave.width_4 = width / 4;
  wave.canvas.height = height;
  wave.canvas.width = width;
  wave.container.style.margin = -(height / 2) + 'px auto';

  if (reproductor) {
    var vol = reproductor.volume();
    var barraAncho = (vol * 0.9);
    deslizarBtn.style.left = (window.innerWidth * barraAncho + window.innerWidth * 0.05 - 25) + 'px';
  }

};

window.addEventListener('resize', dimensionar);
dimensionar();

var emisoras = cargarEmisoras();
var ids_emisoras = cargarIdsEmisoras();
