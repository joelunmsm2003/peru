app = angular.module('docsRestrictDirective', [])

app.controller('Controller', ['$scope','$http', function($scope,$http) {

   $scope.naomi = { name: 'Naomi', address: '1600 Amphitheatre' };
  $scope.vojta = { name: 'Vojta', address: '3456 Somewhere Else' };


  $http.get("http://www.w3schools.com/angular/customers.php")
    .success(function(response) {$scope.names = response.records;
      console.log($scope.names)

    });


  $scope.customer = {
    name: 'Naomi',
    address: '1600 Amphitheatre'
  };
}])


app.directive('myCustomer', function() {
  return {
    restrict: 'E',
    scope: {
      customerInfo: '=info'
    },
    templateUrl: '/static/html/costumer.html'
  };
});