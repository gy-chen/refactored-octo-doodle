'use strict';

angular.module('feed')
  .component('feed', {
    templateUrl: 'feed/feed.template.html',
    controller: ['$routeParams', 'podcastsFactory', function($routeParams, podcastsFactory) {
      var feed = {};

      podcastsFactory.getFeed($routeParams.feedId, function(data) {
        this.feed = data.feed;
      }.bind(this));

      this.feed = feed;
    }]
  });
