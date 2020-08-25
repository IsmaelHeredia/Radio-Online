$(function() {

    $('#reproductor').toggle();

    $('#tabla_emisoras').DataTable({
        "language": {
            "decimal": "",
            "emptyTable": "No se encontraron datos",
            "info": "Mostrando _START_ de _END_ a _TOTAL_ entradas",
            "infoEmpty": "Mostrando 0 hasta 0 of 0 entradas",
            "infoFiltered": "(filtrando de _MAX_ entradas totales)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrando _MENU_ entradas",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar:",
            "zeroRecords": "No se encontraron datos",
            "paginate": {
                "first": "Primero",
                "last": "Ultimo",
                "next": "Siguiente",
                "previous": "Anterior"
            },
            "aria": {
                "sortAscending": ": activar para ordenar la columna ascendentemente",
                "sortDescending": ": activar para ordenar la columna descendentemente"
            }
        }
    });

    $('#tabla_generos').DataTable({
        "language": {
            "decimal": "",
            "emptyTable": "No se encontraron datos",
            "info": "Mostrando _START_ de _END_ a _TOTAL_ entradas",
            "infoEmpty": "Mostrando 0 hasta 0 of 0 entradas",
            "infoFiltered": "(filtrando de _MAX_ entradas totales)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrando _MENU_ entradas",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar:",
            "zeroRecords": "No se encontraron datos",
            "paginate": {
                "first": "Primero",
                "last": "Ultimo",
                "next": "Siguiente",
                "previous": "Anterior"
            },
            "aria": {
                "sortAscending": ": activar para ordenar la columna ascendentemente",
                "sortDescending": ": activar para ordenar la columna descendentemente"
            }
        }
    });
    
});