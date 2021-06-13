var portfolioApp = angular.module('portfolioApp',[]);

portfolioApp.controller('GalleryListCtrl', function($scope)
{
    $scope.galleries = 
    [
        { 'title':'Mustang Super Snake',
        'when':'2020',
        'thumbnailUrl':'img/Mustang Shelby Super Snake.jpg'
        },
        { 'title':'Mustang Shelby GT500',
        'when':'2013',
        'thumbnailUrl':'img/Mustang Shelby GT500 2013.jpg'
        },
        { 'title':'Mustang Classic',
        'when':'1968',
        'thumbnailUrl':'img/Mustang Classic.jpg'
        },
        { 'title':'Mustang Shelby GT500',
        'when':'2021',
        'thumbnailUrl':'img/Mustang Shelby GT500 2021.jpg'
        },
        { 'title':'Mustang Ghia',
        'when':'1980',
        'thumbnailUrl':'img/Mustang 1980.jpg'
        },
        { 'title':'Mustang Cobra',
        'when':'1996',
        'thumbnailUrl':'img/Mustang 1996.jpeg'
        }
    ];
    $scope.sortList = 
    [
        {
            'label':'Alfabetycznie',
            'value':'title'
        },
        {
            'label':'Chronologicznie',
            'value':'when'
        },
        {
            'label':'Od Najnowszych',
            'value':'-when'
        },
    ];
});