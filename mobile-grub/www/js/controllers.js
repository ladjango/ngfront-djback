'use strict';

angular.module('mobileGrub')

  .controller('HomeCtrl',
    function ($scope, $http) {
      $scope.intro = 'Welcome to Mobile Grub!';

      $scope.categories = [];
      $http({url: 'http://localhost:8001/api/categories/'})
        .then(function (result) {
          angular.copy(result.data, $scope.categories);
        });
    })

  .controller('CategoryCtrl',
    function ($scope, category) {
      $scope.category = category;
    })
;
