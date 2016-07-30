'use strict';

angular.module('core.podcastsFactory')
  .factory('podcastsFactory', ['$http', 'core.config', function($http, config) {

    var getFeeds = function(callback) {
      $http({
        method: 'GET',
        url: config['basePath'] + 'feeds'
      }).then(function(response) {
        callback(response.data);
      });
    };

    var getFeed = function(feedId, callback) {
      $http({
        method: 'GET',
        url: config['basePath'] + 'feed/' + feedId
      }).then(function(response) {
        callback(response.data);
      });
    };

    return {
      'getFeeds': getFeeds,
      'getFeed': getFeed
    };
  }]);
