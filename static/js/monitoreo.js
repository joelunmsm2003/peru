
var App=angular.module('App', ['ngCookies','chart.js','ngAnimate']);

App.config(function($interpolateProvider){
$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});


campania = window.location.href.split("monitoreo/")[1].split("/")[0]



$(function () {
    // Create the chart
    $('#graph1').highcharts({
        chart: {
            type: 'column',
             events: {
                        load: function () {

                                serie1 = this.series

                                  var updateChart = function() {

                                $.getJSON("/botoneragraph/"+campania, function (result) {

                                    console.log('botoro llam',result)

       

                                    serie1[0].points[0].update(result['pPromesa'])
                                    serie1[0].points[1].update(result['pDirecto'])
                                    serie1[0].points[2].update(result['pIndirecto'])
                                    serie1[0].points[3].update(result['pNocontacto'])
                                    serie1[0].points[4].update(result['pAsterisk'])
                                    serie1[0].points[5].update(result['pPendiente'])
                                   

                          

                                   
                           
                                });

                            }

                        setTimeout(function(){updateChart()},1000);

                            }
                        }
        },
        title: {
            text: 'Cobertura Campaña'
        },
     
        xAxis: {


            categories: [
                'Promesa',
                'Contacto Directo',
                'Contacto Indirecto',
                'No Contacto',
                'Asterisk',
                'Pendiente'
           
            ],
            crosshair: true
        },
        yAxis: {
            title: {
                text: 'Porcentaje'
            }

        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                borderWidth: 0,
                dataLabels: {
                    enabled: true,
                    format: '{point.y:.1f}%'
                }
            }
        },

        tooltip: {
            headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
            pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
        },

        series: [{
            name: 'Llamadas',
            colorByPoint: true,
            data: [{
                name: 'Promesa',
                y: 56.33,
                drilldown: 'Promesa'
            }, {
                name: 'Directo',
                y: 24.03,
                drilldown: 'Directo'
            }, {
                name: 'Indirecto',
                y: 10.38,
                drilldown: 'Indirecto'
            }, {
                name: 'No Contacto',
                y: 4.77,
                drilldown: 'No Contacto'
            },
            {
                name: 'Asterik',
                y: 4.77,
                drilldown: 'Asterik'
            },

            {
                name: 'Pendiente',
                y: 4.77,
                drilldown: 'Pendiente'
            }]
        }],
        drilldown: {
            series: [{
                name: 'Promesa',
                id: 'Promesa',
                data: [3
            
                ]
            }, {
                name: 'Directo',
                id: 'Directo',
                data: [
                    [
                        'v40.0',
                        5
                    ],
                    [
                        'v41.0',
                        4.32
                    ],
                    [
                        'v42.0',
                        3.68
                    ],
                    [
                        'v39.0',
                        2.96
                    ],
                    [
                        'v36.0',
                        2.53
                    ],
                    [
                        'v43.0',
                        1.45
                    ],
                    [
                        'v31.0',
                        1.24
                    ],
                    [
                        'v35.0',
                        0.85
                    ],
                    [
                        'v38.0',
                        0.6
                    ],
                    [
                        'v32.0',
                        0.55
                    ],
                    [
                        'v37.0',
                        0.38
                    ],
                    [
                        'v33.0',
                        0.19
                    ],
                    [
                        'v34.0',
                        0.14
                    ],
                    [
                        'v30.0',
                        0.14
                    ]
                ]
            }, {
                name: 'Indirecto',
                id: 'Indirecto',
                data: [
                    [
                        'v35',
                        2.76
                    ],
                    [
                        'v36',
                        2.32
                    ],
                    [
                        'v37',
                        2.31
                    ],
                    [
                        'v34',
                        1.27
                    ],
                    [
                        'v38',
                        1.02
                    ],
                    [
                        'v31',
                        0.33
                    ],
                    [
                        'v33',
                        0.22
                    ],
                    [
                        'v32',
                        0.15
                    ]
                ]
            }, {
                name: 'No Contacto',
                id: 'No Contacto',
                data: [
                    [
                        'v8.0',
                        2.56
                    ],
                    [
                        'v7.1',
                        0.77
                    ],
                    [
                        'v5.1',
                        0.42
                    ],
                    [
                        'v5.0',
                        0.3
                    ],
                    [
                        'v6.1',
                        0.29
                    ],
                    [
                        'v7.0',
                        0.26
                    ],
                    [
                        'v6.2',
                        0.17
                    ]
                ]
            }]
        }
    });
});


//-----


$(function () {
    // Create the chart
    $('#graph2').highcharts({
        chart: {
            type: 'column',
             events: {
                        load: function () {

                                serie1 = this.series

                                  var updateChart = function() {

                                $.getJSON("/botoneragraph/"+campania, function (result) {

                                    console.log('botoro llam',result)

       

                                    serie1[0].points[0].update(result['Promesa'])
                                    serie1[0].points[1].update(result['Contacto Directo'])
                                    serie1[0].points[2].update(result['Contacto Indirecto'])
                                    serie1[0].points[3].update(result['No Contacto'])
                                    serie1[0].points[4].update(result['fallecido'])
                                    serie1[0].points[5].update(result['consultatramite'])
                                    serie1[0].points[5].update(result['contactosinpromesa'])
                                    serie1[0].points[5].update(result['dificultadpago'])
                                    serie1[0].points[5].update(result['acuerdoconfecha'])
                                    serie1[0].points[5].update(result['reclamoinstitucion'])
                                    serie1[0].points[5].update(result['refinanciaconvenio'])
                                    serie1[0].points[5].update(result['renuenterehuye'])
                                    serie1[0].points[5].update(result['pagoboucher'])
                                    serie1[0].points[5].update(result['desconocidomudado'])
                                    serie1[0].points[5].update(result['novivelabora'])
                                    serie1[0].points[5].update(result['sivivelabora'])

     
                           
                                });

                            }

                        setTimeout(function(){updateChart()},1000);

                            }
                        }
        },
        title: {
            text: 'Cobertura Campaña'
        },
     
        xAxis: {


            categories: [
                'Promesa',
                'Contacto Directo',
                'Contacto Indirecto',
                'No Contacto',
                'Fallecido',
                'Consulta en tramite',
                'Contacto sin promesa',
                'Dificultad de Pago',
                'Acuerdo con fecha de pago',
                'Reclamo Institucion',
                'Refinancia/Convenio',
                'Renuente/Rehuye',
                'Ya pago con boucher',
                'Tit.desconocido/ Mudado',
                'Msj Tercero(No vive/labora)',
                'Msj Tercero(Si vive/labora)'

            ],
            crosshair: true
        },
        yAxis: {
            title: {
                text: 'Porcentaje'
            }

        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                borderWidth: 0,
                dataLabels: {
                    enabled: true,
                    format: '{point.y:.1f}%'
                }
            }
        },

        tooltip: {
            headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
            pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
        },

         


        series: [{
            name: 'Llamadas',
            colorByPoint: true,
            data: [{
                name: 'Promesa',
                y: 56.33,
                drilldown: 'Promesa'
            }, {
                name: 'Directo',
                y: 24.03,
                drilldown: 'Directo'
            }, {
                name: 'Indirecto',
                y: 10.38,
                drilldown: 'Indirecto'
            }, {
                name: 'Fallecido',
                y: 4.77,
                drilldown: 'Fallecido'
            },
            {
                name: 'Consulta en tramite',
                y: 4.77,
                drilldown: 'Consulta en tramit'
            },



            {
                name: 'Contacto sin promesa',
                y: 4.77,
                drilldown: 'Contacto sin promesa'
            },

            {
                name: 'Dificultad de Pago',
                y: 4.77,
                drilldown: 'Dificultad de Pago'
            }
            ,
            {
                name: 'Acuerdo con fecha de pago',
                y: 4.77,
                drilldown: 'Acuerdo con fecha de pago'
            },

            {
                name: 'Reclamo Institucion',
                y: 4.77,
                drilldown: 'Reclamo Institucion'
            },

            {
                name: 'Refinancia/Convenio',
                y: 4.77,
                drilldown: 'Refinancia/Convenio'
            },

            {
                name: 'Renuente/Rehuye',
                y: 4.77,
                drilldown: 'Renuente/Rehuye'
            },

            {
                name: 'Ya pago con boucher',
                y: 4.77,
                drilldown: 'Ya pago con boucher'
            },
            {
                name: 'Tit.desconocido/ Mudado',
                y: 4.77,
                drilldown: 'Tit.desconocido/ Mudado'
            },
            {
                name: 'Msj Tercero(No vive/labora)',
                y: 4.77,
                drilldown: 'Msj Tercero(No vive/labora)'
            },
            {
                name: 'Msj Tercero(Si vive/labora)',
                y: 4.77,
                drilldown: 'Msj Tercero(Si vive/labora)'
            }]
        }],
        drilldown: {
            series: [{
                name: 'Promesa',
                id: 'Promesa',
                data: [3
            
                ]
            }, {
                name: 'Directo',
                id: 'Directo',
                data: [
                    [
                        'v40.0',
                        5
                    ],
                    [
                        'v41.0',
                        4.32
                    ],
                    [
                        'v42.0',
                        3.68
                    ],
                    [
                        'v39.0',
                        2.96
                    ],
                    [
                        'v36.0',
                        2.53
                    ],
                    [
                        'v43.0',
                        1.45
                    ],
                    [
                        'v31.0',
                        1.24
                    ],
                    [
                        'v35.0',
                        0.85
                    ],
                    [
                        'v38.0',
                        0.6
                    ],
                    [
                        'v32.0',
                        0.55
                    ],
                    [
                        'v37.0',
                        0.38
                    ],
                    [
                        'v33.0',
                        0.19
                    ],
                    [
                        'v34.0',
                        0.14
                    ],
                    [
                        'v30.0',
                        0.14
                    ]
                ]
            }, {
                name: 'Indirecto',
                id: 'Indirecto',
                data: [
                    [
                        'v35',
                        2.76
                    ],
                    [
                        'v36',
                        2.32
                    ],
                    [
                        'v37',
                        2.31
                    ],
                    [
                        'v34',
                        1.27
                    ],
                    [
                        'v38',
                        1.02
                    ],
                    [
                        'v31',
                        0.33
                    ],
                    [
                        'v33',
                        0.22
                    ],
                    [
                        'v32',
                        0.15
                    ]
                ]
            }, {
                name: 'No Contacto',
                id: 'No Contacto',
                data: [
                    [
                        'v8.0',
                        2.56
                    ],
                    [
                        'v7.1',
                        0.77
                    ],
                    [
                        'v5.1',
                        0.42
                    ],
                    [
                        'v5.0',
                        0.3
                    ],
                    [
                        'v6.1',
                        0.29
                    ],
                    [
                        'v7.0',
                        0.26
                    ],
                    [
                        'v6.2',
                        0.17
                    ]
                ]
            }]
        }
    });
});



//------


$(function () {
    $('#pie3D').highcharts({
        chart: {
            type: 'pie',
            options3d: {
                enabled: true,
                alpha: 45,
                beta: 0
            },
            events: {
                        load: function () {

                                var serie3 = this.series[0];

                                  var updateChartpie = function() {

                                $.getJSON("/botoneragraph/"+campania, function (response) {

                     
                                    nocontesta = response['No Contesta']
                                    buzon = response['Buzon']
                                    error = response['Congestion de Red']
                                    contesta = response['Contesta']

                                    serie3.data[0].update(nocontesta);
                                    serie3.data[1].update(buzon);
                                    serie3.data[2].update(error);
                                    serie3.data[3].update(contesta);
                                                       
                           
                                });

                            }


                        setTimeout(function(){updateChartpie()},1000);

                       

                            }
                        }
        },
        title: {
            text: 'Monitoreo de Llamadas'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                depth: 35,
                dataLabels: {
                    enabled: true,
                    format: '{point.name}'
                }
            }
        },
        series: [{
            type: 'pie',
            name: 'Cantidad',
            data: [


                ['No Contesta', 45.0],
                ['Buzon', 26.8],
             
                ['Error', 8.5],
                ['Contesta', 6.2]
               
            ]
        }]
    });
});


$(function () {

    $('#pie').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie',
            events: {
                    load: function () {

                        // set up the updating of the chart each second
                        var series = this.series[0];


        var updateChart = function() {
            
        $.getJSON("/estllamada/"+campania, function (result) {


            console.log('grafica',result)
       
            series.data[0].update(result['porbarrer']);
            series.data[1].update(result['barridos']);
          
        });   


        }      
              
        setInterval(function(){updateChart()},1000);

                    }
                }



        },
        title: {
            text: 'Tráfico'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                showInLegend: true,
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },

         
        series: [{

            name: "Total",
            colorByPoint: true,
            data: [
            {
                name: "Por Barrer",
                y: 0,

            }, {
                name: "Barridos",
                y: 0,
            }
            ]
        }]

    });
});


$(function () {
    $('#pie1').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie',
            events: {
                    load: function () {

                        // set up the updating of the chart each second
                        var series = this.series[0];


        var updateChart = function() {
            
        $.getJSON("/estllamada/"+campania, function (result) {


            console.log('grafica',result)

            
            
            series.data[0].update(result['errados']);
            series.data[1].update(result['correctos']);
          

            

        });   


        }      
              
        setInterval(function(){updateChart()},1000);



                    }
                }



        },
        title: {
            text: 'Estado '
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                showInLegend: true,
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },

         
        series: [{

            name: "Estado ",
            colorByPoint: true,
            data: [
            {
                name: "Errados",
                y: 0,

            }, {
                name: "Correctos",
                y: 0,
            }
            ]
        }]

    });
});



$(function () {
    $('#xy').highcharts({
        chart: {
            type: 'column',
            events: {
                        load: function () {

                                serie = this.series

                                var updateChart = function() {

                                $.getJSON("/botoneragraph/"+campania, function (result) {
                                    
                                    serie[0].points[0].update(result['Promesa'])
                                    serie[0].points[1].update(result['Contacto Directo'])
                                    serie[0].points[2].update(result['Contacto Indirecto'])
                                    serie[0].points[3].update(result['No Contacto'])
                                    serie[0].points[4].update(result['Marcador'])
                                    serie[0].points[4].update(result['Sin Gestion'])

                          
                                });

                                }

                                setInterval(function(){updateChart()},1000);

                        

                            }
                        }
        },


        title: {
            text: 'Detalle'
        },
        subtitle: {
            text: 'Cantidad'
        },
        xAxis: {


            categories: [
                'Promesa',
                'Contacto Directo',
                'Contacto Indirecto',
                'No Contacto',
                'Marcador',
                'Sin Gestion'
           
            ],
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Cantidad'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.0f}</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: 'Resultado',
            data: [0, 0, 0, 0, 0]

        }]
    });
    
    $.getJSON("/botoneragraph/"+campania, function (result) {

    })

});


$(function () {

    $('#ga').highcharts({

        chart: {
            type: 'gauge',
            plotBackgroundColor: null,
            plotBackgroundImage: null,
            plotBorderWidth: 0,
            plotShadow: false,
            events: {
                        load: function () {

                                // set up the updating of the chart each second
                                var series = this.series[0].points[0];
                                var updateChart = function() {

                                $.getJSON("/estllamada/"+campania, function (result) {

                                console.log('grafica',result['barridos'])
                                
                                  series.update(result['barridos']);

                                });   

                                }      
                                setInterval(function(){updateChart()},1000);

                            }
                        }
        },

        title: {
            text: 'Llamadas'
        },

        pane: {
            startAngle: -150,
            endAngle: 150,
            background: [{
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#FFF'],
                        [1, '#333']
                    ]
                },
                borderWidth: 0,
                outerRadius: '109%'
            }, {
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#333'],
                        [1, '#FFF']
                    ]
                },
                borderWidth: 1,
                outerRadius: '107%'
            }, {
                // default background
            }, {
                backgroundColor: '#DDD',
                borderWidth: 0,
                outerRadius: '105%',
                innerRadius: '103%'
            }]
        },

        // the value axis
        yAxis: {
            min: 0,
            max: 30,

            minorTickInterval: 'auto',
            minorTickWidth: 1,
            minorTickLength: 10,
            minorTickPosition: 'inside',
            minorTickColor: '#666',

            tickPixelInterval: 30,
            tickWidth: 2,
            tickPosition: 'inside',
            tickLength: 10,
            tickColor: '#666',
            labels: {
                step: 2,
                rotation: 'auto'
            },
            title: {
                text: ''
            },
            plotBands: [{
                from: 0,
                to: 10,
                color: '#55BF3B' // green
            }, {
                from: 10,
                to: 20,
                color: '#DDDF0D' // yellow
            }, {
                from: 20,
                to: 30,
                color: '#DF5353' // red
            }]
        },

        series: [{
            name: 'Speed',
            data: [80],
            tooltip: {
                valueSuffix: ' km/h'
            }
        }]

    },
    // Add some life
    function (chart) {
        if (!chart.renderer.forExport) {
           
                var point = chart.series[0].points[0],
                    newVal,
                    inc = Math.round((Math.random() - 0.5) * 20);

                newVal = point.y + inc;
                if (newVal < 0 || newVal > 200) {
                    newVal = point.y - inc;
                }

                point.update(4);

           
        }
    });
});


function Controller($scope,$http,$cookies,$filter) {







    console.log(window.location.href.split("monitoreo/"))

    campania = window.location.href.split("monitoreo/")[1].split("/")[0]
    $scope.camp = campania
    var sortingOrder ='-id';
    $scope.sortingOrder = sortingOrder;
    $scope.reverse = false;
    $scope.filteredItems = [];
    $scope.groupedItems = [];
    $scope.itemsPerPage = 20;
    $scope.pagedItems = [];
    $scope.currentPage = 0;

    $http.get("/agentes/"+campania).success(function(response) {$scope.agentes = response;

    });

    $http.get("/estllamada/"+campania).success(function(response) {$scope.nllam = response['barridos'];

        console.log('llammm',$scope.nllam)

    });

    $http.get("/infocampania/"+campania).success(function(response) {

        $scope.campana = response[0]['nombre']
        $scope.cartera = response[0]['cartera__nombre']
        $scope.mascara = response[0]['supervisor__user__empresa__mascaras']



       
    });

    $http.get("/preguntas/1").success(function(response) {$scope.preguntas = response;

    });

    $http.get("/examen").success(function(response) {$scope.examen = response;

        $scope.primer = response[0]

        console.log('criterio 1',response[0])

    });

    $http.get("/nota/").success(function(response) {$scope.nota = response;

    });

    setInterval(function(){ 

    $http.get("/agentes/"+campania).success(function(response) {$scope.agentes = response;

    console.log('agentes',$scope.agentes)

    });

    }, 1000);

    


     $http.get("/agentescampania/"+campania).success(function(response) {$scope.usuarioscampania = response;

        

    });

 

    $http.get("/empresas").success(function(response) {$scope.empresas = response[0];


       
    });
     $http.get("/getempresa").success(function(response) {

        $scope.empresax=response[0]
       
    });

     $http.get("/agentescampania/"+campania).success(function(response) {

        //$scope.campana = response[0]['campania__nombre']
        //$scope.cartera = response[0]['campania__cartera__nombre']


    });






    $http.get("/user").success(function(response) {$scope.user = response;

        $scope.user = $scope.user[0]

    });


    $http.get("/nivel").success(function(response) {$scope.nivel = response;

     

    });

    $scope.btnpregunta = 'True'

    $scope.monitor = function(data) 

    {    
        console.log(data)
        
        $http.get("/accionmonitor/"+data.campania__supervisor__user__anexo+"/"+data.agente__anexo).success(function(response) {

          swal({   title: response,   timer: 1000,   showConfirmButton: false });   
            
        });
  
    }

    $scope.susurro = function(data) 

    {    

       
        $http.get("/accionsusurro/"+data.campania__supervisor__user__anexo+"/"+data.agente__anexo).success(function(response) {

          swal({   title: response,   timer: 1000,   showConfirmButton: false });   
            
        });
    }


    $scope.criterio = function(cri) 

    {       
            $scope.btnpregunta = 'True'
            $scope.btncalifica = 'False'


            if (parseInt(cri.id)<4){


                    console.log(cri.id)

                    nucri = parseInt(cri.id)+1

                    $http.get("/examen").success(function(response) {$scope.examen = response;

                    $scope.primer = response[cri.id]

                    });


                    $http.get("/preguntas/"+nucri).success(function(response) {

                    $scope.preguntas = response;


                    });

            }
            if (parseInt(cri.id)==3){

                console.log('>5...')

                $scope.btnpregunta = 'False'
                $scope.btncalifica = 'True'

            }

     
        




    }

   $scope.model  = {}
   $scope.dato  = {}


   $scope.calificacion = function(data) 

    {

          $('#eliminar').modal('hide')
        $('.modal-backdrop').remove();

    


    }



    $scope.calificarsi = function(data) 

    {

  

        $scope.pregunta = data


   
        $scope.pregunta.estadosi= true
        $scope.pregunta.estadono= false

        $scope.model.campania = campania
        $scope.model.user = $scope.user
        $scope.model.pregunta = data
        $scope.model.respuesta = 'Si'
        $scope.model.agente =   $scope.agente

        console.log('Calificar SI',$scope.model)

        $http({

        url: "/calificar/",
        data: $scope.model,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        })

    }

    

     $scope.calificarno = function(data) 

    {
         
        $scope.pregunta = data
        $scope.pregunta.estadono= true
        $scope.pregunta.estadosi= false

        $scope.model.campania = campania
        $scope.model.user = $scope.user
        $scope.model.pregunta = data
        $scope.model.respuesta = 'No'

        console.log($scope.model)


        $http({

        url: "/calificar/",
        data: $scope.model,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        })
    }



    $scope.agregar = function(index,contact) 

    {


    $scope.usuarioscampania.push(contact);
    $scope.usuarios.splice(index,1);

        var todo={

            campania: campania,
            dato: contact,
            done:false
        }

        $http({

        url: "/agregaragente/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

            swal({   title: "Asignacion de agentes",   text: data +' agregado',   timer: 2000,   showConfirmButton: false });
    
    
    
        })

    
    };

    $scope.quitar = function(index,contact) 

    {

    $scope.usuarios.push(contact);
    $scope.usuarioscampania.splice(index,1);

            var todo={

            campania: campania,
            dato: contact,
            done:false
        }

        $http({

        url: "/quitaragente/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

            swal({   title: "Asignacion de agentes",   text: data +' quitado',   timer: 2000,   showConfirmButton: false });
    
    
        })
    
    };

    
    $('.monixxx').show()
    $scope.bb = 'False'
    $scope.bbi = 'True'
    $scope.mon = function() 

    {

    console.log('jjdjdjddjj')

    $('.monixxx').show()
    $scope.bb = 'False'
    $scope.bbi = 'True'

    };

    $scope.ocultarmon = function() 

    {


    $('.monixxx').hide()
    $scope.bb = 'True'
    $scope.bbi = 'False'


    };

    $scope.numberOfPages = function() 

    {

    return Math.ceil($scope.clientes.length / $scope.pageSize);
    
    };

    $scope.evaluar = function(nota,index) 

    {

    $http.get("/preguntas/1").success(function(response) {$scope.preguntas = response;

    });

    $http.get("/examen").success(function(response) {$scope.examen = response;

        $scope.primer = response[0]

        console.log('criterio 1',response[0])


    });


    console.log('pregunta',$scope.preguntas)

    $scope.agente = nota

    console.log('nota',nota)

    $scope.user = nota
    
    };




    $scope.addNew=function(agregar){


        console.log('agregar',agregar)

        var todo={

            add: "New",
            dato: agregar,
            done:false
        }

        $http({
        url: "/usuarios/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        swal({   title: "Perucall",   text: "Usuario "+data +" agregado",   type: "success",   confirmButtonColor: "#337ab7",   confirmButtonText: "OK",   }, function(){   window.location.href = "/usuario" });
 
        $scope.agregar=""

        })


    };

    $scope.saveContact = function (idx,currentPage) {


        $scope.pagedItems[currentPage][idx] = angular.copy($scope.model);
        $('#edit').modal('hide')
        $('.modal-backdrop').remove();


        var todo={

            add: "Edit",
            dato: $scope.model,
            done:false
        }


        $http({
        url: "/usuarios/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        swal({   title: "Perucall",   text: "Usuario "+data +" editado",   type: "success",   confirmButtonColor: "#337ab7",   confirmButtonText: "OK",   }, function(){   });
 
        })


        $('#Edit').modal('hide')
        $('.modal-backdrop').remove();
    };



    $scope.eliminarContact = function (idx,currentPage) {

        $('#eliminar').modal('hide')
        $('.modal-backdrop').remove();

        $scope.pagedItems[currentPage].splice(idx,1);

        var todo={

            dato: $scope.model,
            add: "Eliminar",
            done:false
        }


        $http({
        url: "/usuarios/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        $scope.contador =$scope.contador-1

        })

    };


    $scope.editContact = function (contact,index,currentPage) {

        $scope.index = index;
        $scope.numberPage =currentPage;
        $scope.model = angular.copy(contact);
        console.log('edit',$scope.model);

    };

    $scope.calificar = function (contact,user) {


        $('#notificacion').modal('hide')
        $('.modal-backdrop').remove();

        $http.get("/examen").success(function(response) {$scope.examen = response;

        $scope.primer = response[0]

        });


        $http.get("/preguntas/1").success(function(response) {

        $scope.preguntas = response;


        });

        /*

        msj = contact.respuesta +" " +contact.nota.tipo

        username = user.agente__user__username


        var todo={

            msj: msj,
            username: username,
            done:false
        }

        $http({

        url: "/enviar/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

            swal({   title: "Perucall",   text: "Agente "+user.agente__user__first_name +" calificado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "OK",   }, function(){   });
            $scope.pregunta=""
        
        })

*/
    };

    $scope.notificar = function (contact,user) {


        
        $('#notificacion').modal('hide')
        $('.modal-backdrop').remove();



        msj = contact

        username = user.agente__user__username


        var todo={

            msj: msj,
            username: username,
            done:false
        }

        $http({

        url: "/notificar/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

            swal({      title: "Agente "+user.agente__user__first_name +" notificado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Cerrar",   }, function(){   });
            $scope.notificacion=""
    
        })
    };



    $scope.sort_by = function(newSortingOrder,currentPage) {


        function sortByKey(array, key) {
            return array.sort(function(a, b) {
            var x = a[key]; var y = b[key];
            return ((x < y) ? -1 : ((x > y) ? 1 : 0));
            });
        }

    

        function sortByKey(array, key) {
            return array.sort(function(a, b) {
            var x = a[key]; var y = b[key];
            return ((x < y) ? -1 : ((x > y) ? 1 : 0));
            });
        }

    
        if ($scope.sortingOrder == newSortingOrder)
            $scope.reverse = !$scope.reverse;

        $scope.sortingOrder = newSortingOrder;


        people = sortByKey($scope.clientes, newSortingOrder);

        if ($scope.reverse){

            console.log($scope.reverse);
            people = sortByKey(people, newSortingOrder).reverse();
            
        }
  

        $scope.clientes = people

        $scope.search()


        // icon setup
        $('th i').each(function(){
            // icon reset
            $(this).removeClass().addClass('icon-sort');
        });
        if ($scope.reverse)
            $('th.'+newSortingOrder+' i').removeClass().addClass('icon-chevron-up');
        else
            $('th.'+newSortingOrder+' i').removeClass().addClass('icon-chevron-down');
    
    };

    $scope.search = function () {

        
        console.log('search')

        String.prototype.capitalizeFirstLetter = function() {

        return this.charAt(0).toUpperCase() + this.slice(1);

        }

        var output = {};

        obj = $filter('filter')($scope.clientes,$scope.tipo)

        $scope.contador = ObjectLength(obj)
       
        console.log('$scope.tipo',$scope.tipo)

        $scope.filteredItems = $filter('filter')($scope.clientes,$scope.tipo);

        $scope.currentPage = 0;

        console.log('$scope.filteredItems',$scope.filteredItems)

        $scope.groupToPages();

    };


    function ObjectLength( object ) {
    var length = 0;
    for( var key in object ) {
        if( object.hasOwnProperty(key) ) {
            ++length;
        }
    }
    return length;
    };


    $scope.groupToPages = function () {

        console.log('Grupo')
        $scope.pagedItems = [];
        
        for (var i = 0; i < $scope.filteredItems.length; i++) {


            if (i % $scope.itemsPerPage === 0) {
                $scope.pagedItems[Math.floor(i / $scope.itemsPerPage)] = [ $scope.filteredItems[i] ];
            } else {
                $scope.pagedItems[Math.floor(i / $scope.itemsPerPage)].push($scope.filteredItems[i]);
            }
        }

        console.log('$scope.pagedItems',$scope.pagedItems[0])

             var input =[]

            for (var i = 1; i <= $scope.pagedItems.length; i++) input.push(i);

            $scope.toto = input

    };


    $scope.prevPage = function () {
        if ($scope.currentPage > 0) {
            $scope.currentPage--;
        }
    };
    
    $scope.nextPage = function () {
        if ($scope.currentPage < $scope.pagedItems.length - 1) {
            $scope.currentPage++;
        }
    };
    
    $scope.setPage = function () {
        $scope.currentPage = this.n-1;
    };

    
    Controller.$inject = ['$scope', '$filter'];

}

