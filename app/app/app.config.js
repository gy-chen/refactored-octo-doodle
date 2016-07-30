'use strict';

angular.module('app')
  .config(function($routeProvider, $locationProvider) {
    $routeProvider
      .when('/', {
        template: '<podcasts></podcasts>'
      })
      .when('/feed/:feedId', {
        template: '<feed></feed>'
      })
      .otherwise('/');
  });
