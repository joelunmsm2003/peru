app = angular.module('App', [])

app.controller('Controller', ['$scope','$http','$filter', function($scope,$http,$filter) {



    var _name = 'Brian';
  $scope.user = {
    name: function(newName) {
     // Note that newName can be undefined for two reasons:
     // 1. Because it is called as a getter and thus called with no arguments
     // 2. Because the property should actually be set to undefined. This happens e.g. if the
     //    input is invalid
     console.log(newName)
     return arguments.length ? (_name = newName) : _name;
    }
  };


setInterval(ajaxCall, 3500); 

function ajaxCall() {


    $http.get("/empresas/").success(function(response) {$scope.clientes = response;

      console.log(ObjectLength($scope.clientes))

      $scope.contpre = ObjectLength($scope.clientes)

      

      if ($scope.contant!=$scope.contpre){

        $scope.search()

      }

      
      $scope.contant = ObjectLength($scope.clientes)

    });

}


    var sortingOrder = '-id';
    $scope.sortingOrder = sortingOrder;
    $scope.reverse = false;
    $scope.filteredItems = [];
    $scope.groupedItems = [];
    $scope.itemsPerPage = 20;
    $scope.pagedItems = [];
    $scope.currentPage = 0;




    $scope.numberOfPages = function() 
    {

    return Math.ceil($scope.clientes.length / $scope.pageSize);
    
    };


    $scope.Pato = function() 
    {

    console.log($scope.agregar)
    
    };





    $scope.sort_by = function(newSortingOrder,currentPage) {


         

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
    
 
        var output = {};

        console.log($filter('filter')($scope.clientes,$scope.tipo))

        obj = $filter('filter')($scope.clientes,$scope.tipo)

        $scope.contador = ObjectLength(obj)


        $scope.filteredItems = $filter('filter')($scope.clientes,$scope.tipo);
        $scope.currentPage = 0;

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
        $scope.currentPage = this.n;
    };

    
    app.$inject = ['$scope', '$filter'];

    



}])


app.directive('myEmpresa', function() {
  return {
    restrict: 'E',
    templateUrl: '/static/html/empresa.html'
  };
});