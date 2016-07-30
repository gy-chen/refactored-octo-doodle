'use strict';

angular.module('podcasts')
  .component('podcasts', {
    templateUrl: 'podcasts/podcasts.template.html',
    controller: ['podcastsFactory', function(podcastsFactory) {
      var feeds = [];

      podcastsFactory.getFeeds(function(data) {
        this.feeds = data['feeds'];
      }.bind(this));

      this.feeds = feeds;
    }]
  });
