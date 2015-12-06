
var App=angular.module('App', ['ngCookies']);

App.config(function($interpolateProvider){
$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});



function Controller($scope,$http,$cookies,$filter,$interval) {

    $('.gestion').hide()


    agente = window.location.href.split("teleoperador/")[1].split("/")[0]

    
    $http.get("/resultado").success(function(response) {$scope.resultado = response;
              
    });


    $http.get("/empresas").success(function(response) {$scope.empresas = response[0];
   
       
    });


    $http.get("/cliente/"+agente).success(function(response) {

        $scope.cliente = response[0];

        $scope.iniciollamada = new Date($scope.cliente.tiniciollamada)
             
    });

    $http.get("/user").success(function(response) {$scope.user = response;

        $scope.user = $scope.user[0]

        $scope.last_login = $scope.user.last_login

    });

    $http.get("/atendida/"+agente).success(function(response) {$scope.atendida = response;

       
        $scope.fechaa = new Date($scope.atendida)
        $scope.atendida = $scope.fechaa.getSeconds()

        console.log($scope.atendida)
    });

    //$http.get("/desfase/"+agente).success(function(response) {$scope.desfase = response;

       
    //});

    $http.get("/tgestion/"+agente).success(function(response) {

    $scope.tgestion = response;
  

    });

   

      var tick = function() {


        last_login = $scope.last_login
        login = new Date(last_login)
       

        $scope.desfase = $scope.conectado-$scope.atendida
        inicio = $scope.iniciollamada

        d1 = new Date(); //"now"
        d2 = new Date($scope.tgestion)  // some date

        $scope.diff = Math.abs(d1-d2);  // difference in milliseconds
        $scope.conectado = parseInt(Math.abs(d1-login)/1000)
        $scope.tllamada = parseInt(Math.abs(d1-inicio)/1000)
        sec = $scope.diff/1000

        $scope.secgestion = sec*2

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

      }
      tick();
      $interval(tick, 1000);

 

    $http.get("/agente/"+agente).success(function(response) {$scope.agente = response;


            data = JSON.parse($scope.agente['data'])

            $scope.datoagente =data[0]      

    });



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






    $scope.word=0



    $scope.tipeo = function() 
    
    {
        var dateactual = new Date();

        console.log('fecha_gestion',$scope.fechagestion)

       

        $scope.word=$scope.word+1

        if($scope.word<2){


            $scope.fechagestion = new Date(); 

            
            $scope.datoagente['estado__nombre'] = "En gestion"
             
            var todo={

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
        }

     
    };



    $scope.botonera = function(contact) 
    {

       
        console.log(contact)

        if(contact['id']==11){

            $('.gestion').show()

            $('.gestion').addClass('animated bounce')
        }
        else{
            $('.gestion').hide()

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

   

        })
 
    };

    
    Controller.$inject = ['$scope', '$filter'];

}

