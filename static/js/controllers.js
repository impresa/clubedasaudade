var app = angular.module('keywordSearchApp', []).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});

app.controller('SearchCtrl', function ($scope,$http) {
    $scope.search = function(search_terms) {
        $http.get('search?search_terms=' + encodeURIComponent(search_terms)).success(function(data) {
            $scope.entries = data;
        });
        console.log('asd');
    };
});