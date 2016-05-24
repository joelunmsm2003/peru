
var App=angular.module('App', ['ngCookies','ngAnimate']);

App.config(function($interpolateProvider){
$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});



    /////


function Controller($scope,$http,$cookies,$filter,$interval,$location) {

    agente = window.location.href.split("teleoperador/")[1].split("/")[0]


    
    $http.get("/resultadototal").success(function(response) {$scope.resultado = response;
              
    });
    $http.get("/empresas").success(function(response) {$scope.empresas = response[0];
   
    });

     $http.get("/getempresa").success(function(response) {

        $scope.empresax=response[0]
       
    });


     $scope.promesa = 15
     $scope.directo = 16
     $scope.indirecto = 17
     $scope.nocontacto = 18


    $http.get("/cliente/"+agente).success(function(response) {

        $scope.cliente = response[0];

        console.log('Reg base',$scope.cliente)

        $scope.id_campania = $scope.cliente.id

        $http.get("/header/"+$scope.id_campania).success(function(response) {$scope.header = response[0];
    
        });

        $http.get("/listafiltros/"+$scope.id_campania).success(function(response) {$scope.filtros = response[0];
              
        });

        $scope.iniciollamada = new Date($scope.cliente.tiniciollamada)
             
    });


    $http.get("/user").success(function(response) {$scope.user = response;

        $scope.user = $scope.user[0]

        $scope.last_login = $scope.user.last_login

    });

    $http.get("/atendida/"+agente).success(function(response) {$scope.atendida = response;
       
        $scope.fechaa = new Date($scope.atendida)
        $scope.atendida = $scope.fechaa.getSeconds()
        $scope.at =formatSeconds($scope.atendida)

    });


    $http.get("/tgestion/"+agente).success(function(response) {

    $scope.tgestion = response;

    });

    function formatSeconds(seconds)
        {
            var date = new Date(1970,0,1);
            date.setSeconds(seconds);
            return date.toTimeString().replace(/.*(\d{2}:\d{2}:\d{2}).*/, "$1");
        }

   

    var tick = function() {

        $http.get("/tgestion/"+agente).success(function(response) {

        $scope.tgestion = response;

        });


        login = new Date($scope.last_login)
        d1 = new Date(); 

        d2 = new Date($scope.tgestion)  

        $scope.desfase = $scope.conectado-$scope.atendida
        $scope.des = formatSeconds($scope.desfase)
        $scope.diff = Math.abs(d1-d2);  

        $scope.conectado = parseInt(Math.abs(d1-login)/1000)

        $scope.con = formatSeconds($scope.conectado)

        $scope.tllamada = parseInt(Math.abs(d1-d2)/1000)

        $scope.tllamada = formatSeconds($scope.tllamada)

        sec = $scope.diff/1000

        $scope.secgestion = sec*4

        $scope.conteo = sec

        if (sec<30 && sec>0){

            $scope.color="#81C784"
        }

        if (sec>30 && sec<55){

            $scope.color="#2196F3"
        }

        if (sec>55){

            $scope.color="#EF5350"
            
        }

         

        $http.get("/cliente/"+agente).success(function(response) {

        $scope.cliente = response[0];

        console.log('Reg base',$scope.cliente)

        $scope.id_campania = $scope.cliente.id

       

        $http.get("/header/"+$scope.id_campania).success(function(response) {$scope.header = response[0];
                  
        });

        $http.get("/listafiltros/"+$scope.id_campania).success(function(response) {$scope.filtros = response[0];
                     
        });

        $scope.iniciollamada = new Date($scope.cliente.tiniciollamada)
             
        });

        $http.get("/agente/"+agente).success(function(response) {$scope.agente = response;

        data = JSON.parse($scope.agente['data'])

        $scope.datoagente =data[0] 

        });

        

      }

      tick();

      $interval(tick, 1000);

 

    $http.get("/agente/"+agente).success(function(response) {$scope.agente = response;


            data = JSON.parse($scope.agente['data'])

            $scope.datoagente =data[0] 

    

            $('#wrapper').fadeToggle("slow")
            $('.container-full').fadeToggle("slow")

    });

     $scope.signout = function(contact) 
    {
        console.log('signout')

        location.href = "/salir"

    }

    $scope.break = function() 
    {

        
   

        $http.get("/tgestion/"+agente).success(function(response) {

            $scope.tgestion = response;

            tick()


            });


   
            $scope.datatime = 30
            $scope.rosa=true
         $scope.datatime = 30

            setInterval(function(){

                $scope.datatime = $scope.datatime-1
               
                if ($scope.datatime==0){

                    $scope.rosa = false
                     $scope.datatime = 30
                }


            },1000);
            $http.get("/receso/"+agente).success(function(response) {

                $http.get("/agente/"+agente).success(function(response) {$scope.agente = response;

                data = JSON.parse($scope.agente['data'])

                $scope.datoagente =data[0] 

                });

              
        });


     swal({   title: "Break",    timer: 1000,   showConfirmButton: false });

    }

        $scope.servicios = function() 
    {

    
   

        $http.get("/tgestion/"+agente).success(function(response) {

            $scope.tgestion = response;


            });


   

        $scope.rosa=true
         $scope.datatime = 30

            setInterval(function(){

                $scope.datatime = $scope.datatime-1
               
                if ($scope.datatime==0){

                    $scope.rosa = false
                     $scope.datatime = 30
                }


            },1000);
        
        $http.get("/sshh/"+agente).success(function(response) {

                $http.get("/agente/"+agente).success(function(response) {$scope.agente = response;

                data = JSON.parse($scope.agente['data'])

                $scope.datoagente =data[0] 

                });

              
        });


     swal({   title: "Servicios",     timer: 1000,   showConfirmButton: false });

    }

     $scope.pausa = function() 


    {

     
   

            $http.get("/tgestion/"+agente).success(function(response) {

            $scope.tgestion = response;


            });

        $scope.datatime = 30

        $http.get("/getestado/"+agente).success(function(response) {


        console.log('Get estado',response)

        $scope.rosa=true

        if(response == 2 || response == 8 || response== 9 ){

            $scope.datatime = 30

            setInterval(function(){

                $scope.datatime = $scope.datatime-1
               

                if ($scope.datatime==0){

                    $scope.rosa = false
                     $scope.datatime = 30
                }


            },1000);




    }

   
    });
    


    console.log('hshshshs')
    $http.get("/pausa/"+agente).success(function(response) {

        $http.get("/agente/"+agente).success(function(response) {$scope.agente = response;

        data = JSON.parse($scope.agente['data'])

        $scope.datoagente =data[0] 

        });



    
              
    });

     swal({   title: "Pausa",   timer: 1000,   showConfirmButton: false });



    }

    $scope.playx=false
    $scope.pausax=true

    $scope.play = function() 

    {
        $http.get("/tgestion/"+agente).success(function(response) {

            $scope.tgestion = response;


            });
   

        $http.get("/tgestion/"+agente).success(function(response) {

            $scope.tgestion = response;


            });

        $scope.playx=false
        $scope.pausax=true

        var todo={
            agente:agente,
            done:false
            }


        $http({
            url: "/lanzaespera/",
            data: todo,
            method: 'POST',
            headers: {
            'X-CSRFToken': $cookies['csrftoken']
            }
            }).
            success(function(data) {

                    $http.get("/agente/"+agente).success(function(response) {$scope.agente = response;

                    data = JSON.parse($scope.agente['data'])

                    $scope.datoagente =data[0] 

                    });


        })


     swal({   title: "Play",   timer: 1000,   showConfirmButton: false });

    }

    $scope.colgar = function() 
    {

        location.href = "/finllamada/"+agente+'/'+$scope.cliente.id


    }

    $scope.botonexterno = function(data) 


    {       console.log('Btn Externo',data)

            var todo={

            boton: data,
            cliente : $scope.cliente,
            agente:agente,
            done:false
            }

            $http({
            url: "/botonexterno/",
            data: todo,
            method: 'POST',
            headers: {
            'X-CSRFToken': $cookies['csrftoken']
            }
            }).
            success(function(data) {

            })

            $http({
            url: "/lanzaespera/",
            data: todo,
            method: 'POST',
            headers: {
            'X-CSRFToken': $cookies['csrftoken']
            }
            }).
            success(function(data) {

            $http.get("/tgestion/"+agente).success(function(response) {

            $scope.tgestion = response;


                    $http.get("/agente/"+agente).success(function(response) {$scope.agente = response;

                    data = JSON.parse($scope.agente['data'])

                    $scope.datoagente =data[0] 

                    });


            });





            })



    }




    $scope.gestionlanza = function(contact) 

    {

    console.log(contact)

      var todo={

            gestion: contact,
            cliente : $scope.cliente,
            agente:agente,
            done:false
            }

            $http({
            url: "/gestionupdate/",
            data: todo,
            method: 'POST',
            headers: {
            'X-CSRFToken': $cookies['csrftoken']
            }
            }).
            success(function(data) {

                

            })
   
    };

    $scope.Agendar = function(contact) 
    
    {

            $('#agendar').modal('hide')
            $('.modal-backdrop').remove();
      

          var todo={

            base: $scope.cliente.id,
            agente:agente,
            fecha:contact,
            done:false
            }

            $http({
            url: "/agendar/",
            data: todo,
            method: 'POST',
            headers: {
            'X-CSRFToken': $cookies['csrftoken']
            }
            }).
            success(function(data) {

       
            swal({   title: "Agenda",   text: 'Llamada agendada',   timer: 1000,   showConfirmButton: false });

            })

    }



    $scope.word=0



    $scope.tipeo = function() 
    
    {
        var dateactual = new Date();
  
        $scope.word=$scope.word+1
   
        $scope.fechagestion = new Date(); 
         
        var todo={

        word:$scope.word,
        fechagestion: $scope.fechagestion,
        cliente : $scope.cliente,
        agente:agente,
        done:false

        }

        $http({
        url: "/gestion/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

            $http.get("/tgestion/"+agente).success(function(response) {

            $scope.tgestion = response;


            });
   

        })
       

     
    };



    $scope.botonera = function(contact) 
    {

       
        console.log(contact)

        if(contact['id']==15 || contact['id']==5){

            $('.gestionfecha').show()

            $('.gestionfecha').addClass('animated bounce')
        }
        else{
            $('.gestionfecha').hide()

        }

        var todo={

            resultado: contact,
            cliente : $scope.cliente,
            agente: agente,
            done:false
        }

        $http({
        url: "/botonera/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

            $http.get("/cliente/"+agente).success(function(response) {

            $scope.cliente = response[0];

 
             
    });



   

        })
 
    };



    
    Controller.$inject = ['$scope', '$filter'];

}

