
var App=angular.module('App', ['ngCookies','ngAnimate']);

App.config(function($interpolateProvider){
$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});


function Controller($scope,$http,$cookies,$filter) {


    var sortingOrder ='-id';
    $scope.sortingOrder = sortingOrder;
    $scope.reverse = false;
    $scope.filteredItems = [];
    $scope.groupedItems = [];
    $scope.itemsPerPage = 20;
    $scope.pagedItems = [];
    $scope.currentPage = 0;


    
    $http.get("/campanias").success(function(response) {$scope.clientes = response;

        $scope.search();
       
    });

    $http.get("/empresas").success(function(response) {$scope.empresas = response[0];

        
       
    });

    $http.get("/supervisores").success(function(response) {$scope.supervisores = response;

      
       
    });

   
    
    $scope.mpass= true


    $http.get("/user").success(function(response) {$scope.user = response;

        $scope.user = $scope.user[0]

        if($scope.user['nivel']==2){

            $scope.mpass= false

        }

           

    });


    $scope.Admin = function(contact) 
    {

    console.log(contact.id)

    nivel = $scope.user['nivel']

    if (nivel==5){

        window.location="/monitoreo/"+contact.id
    }
    else{

        window.location="/adminCampania/"+contact.id

    }




    
    
    };

    $scope.Reasignar = function(contact) 
    {

        $scope.model = angular.copy(contact);
        console.log($scope.model)
 
    };

     $scope.reasig = function(contact) 
    {

        console.log('jjjj',contact)

        var todo={

            add: "New",
            dato: contact,
            done:false
        }

        $http({
        url: "/reasignarsupervisor/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        swal({   title: "Supervisor actualizado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Aceptar",   }, function(){   window.location.href = "/campania" });

         
         $scope.agregar=""


        })


 
    };






    $scope.numberOfPages = function() 
    {

    return Math.ceil($scope.clientes.length / $scope.pageSize);
    
    };







    $scope.addNew=function(agregar){

      



        var todo={

            add: "New",
            dato: agregar,
            done:false
        }

        $http({
        url: "/empresas/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

       swal({   title: "Perucall",   text: "Empresa "+data +" agregado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Agregado",   }, function(){   window.location.href = "/empresa" });

         
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
        url: "/empresas/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

            swal({title: "Perucall", text: "Empresa "+data +" editado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Editado",   }, function(){  });


        })


    };



    $scope.eliminarContact = function (idx,currentPage) {


        $('#eliminar').modal('hide')
        $('.modal-backdrop').remove();


        $http.get("/user").success(function(response) {$scope.user = response;

        $scope.user = $scope.user[0]


        });


        if($scope.user.nivel==1){

            var todo={

                dato: $scope.model,
                add: "Eliminar",
                done:false
            }


            $http({
            url: "/campanias/",
            data: todo,
            method: 'POST',
            headers: {
            'X-CSRFToken': $cookies['csrftoken']
            }
            }).
            success(function(data) {

            $scope.contador =$scope.contador-1

            $http.get("/campanias").success(function(response) {$scope.clientes = response;

            $scope.search();

            });


            })
        }


        if($scope.user.nivel==2){


            swal({ 
                title: "Ingrese clave secreta",   
                   
                type: "input",   
                confirmButtonColor: "#b71c1c",
                showCancelButton: true,   
                closeOnConfirm: false,   
                animation: "slide-from-top",   
                inputPlaceholder: "Ingrese clave secreta" }, 

            function(inputValue){   if (inputValue === false) return false;      if (inputValue === "") {     

                swal.showInputError("Ingrese la clave");  

                return false   } 

                else{

                    $http.get("/passcampania/"+$scope.model.id).success(function(response) {$scope.pass = response;

                    $scope.passcampania = $scope.pass[0]

                    console.log('pass',inputValue,$scope.passcampania)

                    if (parseInt(inputValue) == parseInt($scope.passcampania.password)){

                        var todo={

                            dato: $scope.model,
                            add: "Eliminar",
                            done:false
                        }


                        $http({
                        url: "/campanias/",
                        data: todo,
                        method: 'POST',
                        headers: {
                        'X-CSRFToken': $cookies['csrftoken']
                        }
                        }).
                        success(function(data) {

                        $scope.contador =$scope.contador-1

                        })



                        swal({title: "Campaña Eliminada ",   type: "success", confirmButtonColor: "#b71c1c",   confirmButtonText: "Aceptar",   }, function(){   });

                        $http.get("/campanias").success(function(response) {$scope.clientes = response;

                            $scope.search();
                           
                        });

                    }
                    else{

                        swal({   title: "Contraseña incorrecta, lo siento ",    timer: 800,   showConfirmButton: false });
                    }


                    });



                    


                }     

                


            });

        }

            




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

