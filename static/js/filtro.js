
var App=angular.module('App', ['ngCookies']);

App.config(function($interpolateProvider){
$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});

function Controller($scope,$http,$cookies,$filter) {


    campania = window.location.href.split("filtros/")[1].split("/")[0]
    $scope.camp = campania
    $scope.camp = campania
    var sortingOrder ='-id';
    $scope.sortingOrder = sortingOrder;
    $scope.reverse = false;
    $scope.filteredItems = [];
    $scope.groupedItems = [];
    $scope.itemsPerPage = 20;
    $scope.pagedItems = [];
    $scope.currentPage = 0;

    $scope.filtro = []

    $http.get("/resultado").success(function(response) {$scope.resultado = response;

    });

     $http.get("/getempresa").success(function(response) {

        $scope.empresax=response[0]
       
    });

    $http.get("/infocampania/"+campania).success(function(response) {

       console.log('info',response)
        $scope.campana = response[0]['nombre']
        $scope.cartera = response[0]['cartera__nombre']

       
    });

     $http.get("/header/"+campania).success(function(response) {$scope.header = response[0];

        console.log('header',$scope.header)


       
    });




    
    $http.get("/status_f/"+campania).success(function(response) {$scope.ciudad = response;

     

    });
    $http.get("/status_g/"+campania).success(function(response) {$scope.grupo = response;});
    $http.get("/status_h/"+campania).success(function(response) {$scope.segmento = response;});


     $http.get("/empresas").success(function(response) {$scope.empresas = response[0];


       
    });






    $http.get("/user").success(function(response) {$scope.user = response;

        $scope.user = $scope.user[0]

    });

    $http.get("/listafiltros/"+campania).success(function(response) {

        $scope.listafiltros = response; 

    });

    setInterval(function(){ 

    $http.get("/listafiltros/"+campania).success(function(response) {

    $scope.listafiltros = response; 

    console.log($scope.listafiltros)

    });


    },1000);


    $http.get("/nivel").success(function(response) {$scope.nivel = response;

        console.log('$scope.nivel',$scope.nivel)

    });

    $scope.activafiltro = function(contact,index) 



    {

        $('.filtro').css("background-color","#234 !important")
        console.log(campania)

        $http.get("/activafiltro/"+contact.id+'/'+campania).success(function(response) {


    });

    }

    $scope.next = function() 

    {

        window.location='/monitoreo/'+campania
         
    }


    $scope.desactivafiltro = function(contact,index) 

    {

         $http.get("/desactivafiltro/"+contact.id+'/'+campania).success(function(response) {

    });


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

            swal({      title: data +' agregado',   timer: 2000,   showConfirmButton: false });
    
    
    
        })

    
    };


        






      $scope.filtrado = function(dato) 

    {   

         $('#filtrop').modal('hide')
        $('.modal-backdrop').remove();

        var convArrToObj = function(array){

                var thisEleObj = new Object();
                if(typeof array == "object"){
                for(var i in array){
                var thisEle = convArrToObj(array[i]);
                thisEleObj[i] = thisEle;
                }
                }else {
                thisEleObj = array;
                }
                return thisEleObj;
        }
        object = convArrToObj(dato)
    
    

        
        

        console.log(object.ciudad)

        var todo={

            campania:campania,
            segmento:dato.segmento,
            grupo:dato.grupo,
            ciudad:dato.ciudad,
            resultado:dato.resultado,
            done:false
        }

        $http({

        url: "/agregarfiltro/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(r) {

            object.cantidad = r

            swal({   title: 'Filtro agregado',  type: "success",  timer: 1000,   showConfirmButton: false });

            $http.get("/listafiltros/"+campania).success(function(response) {

                    $scope.listafiltros = response; 

                    });




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

            swal({   title: "Asignacion de agentes",   text: data +' quitado',   timer: 1000,   showConfirmButton: false });
    
    
        })
    
    };

    $scope.numberOfPages = function() 

    {

    return Math.ceil($scope.clientes.length / $scope.pageSize);
    
    };

    $scope.eliminar = function(data,index) 

    {

    $scope.model = data
    $scope.model.index = index

    console.log('index',index)
    
    };

    $scope.eliminarfiltro = function(data) 

    {

        $('#eliminar').modal('hide')
        $('.modal-backdrop').remove();

        console.log('data',data.index)

        $scope.listafiltros.splice(data.index,1);

        

        var todo={

            dato: data,
            done:false
        }

        

        $http({

        url: "/eliminarfiltro/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

            swal({      title: 'Filtro eliminado :(',   timer: 1500,   showConfirmButton: false });
    
    
        })
        

    
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

        swal({     title: "Usuario "+data +" agregado",   type: "success",   confirmButtonColor: "#337ab7",   confirmButtonText: "Cerrar",   }, function(){   window.location.href = "/usuario" });
 
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

        swal({   title: "Usuario "+data +" editado",   type: "success",   confirmButtonColor: "#337ab7",   confirmButtonText: "Cerrar",   }, function(){   });
 
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

