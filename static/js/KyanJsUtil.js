$.extend({
    getBookImg: function(name, size, callback) {
        size = size?size:'m';  // s,m,l
        if(!name){
            return ''
        }
        var book_search_api = 'https://api.douban.com/v2/book/search';
        $.ajax({
            type: 'GET',
            url: book_search_api,
            data: {
                'count':'1',
                'q':name
            },
            async: false,
            dataType: 'jsonp',
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                console.log("Ajax Error, XMLHttpRequest:");
                console.log("status: "+XMLHttpRequest.status);
                console.log("readyState: "+XMLHttpRequest.readyState);
                console.log("textStatus: "+textStatus);
            },
            success: function(data){
                var imgurl = "";
                if(data.books[0]){
                    if(data.books[0].title.indexOf(name) >= 0){
                        switch(size){
                            case 's':
                                imgurl = data.books[0].images.small;
                                break;
                            case 'm':
                                imgurl = data.books[0].images.medium;
                                break;
                            case 'l':
                                imgurl = data.books[0].images.large;
                                break;
                            default:
                                imgurl = data.books[0].images.medium;
                        }
                    }
                }
                callback(imgurl);
            }
        });
    },
    getBookPages: function(name, callback){
        var book_search_api = 'https://api.douban.com/v2/book/search';
        if(name != ''){
            $.get(book_search_api, {'count':'1','q':name}, function(data){
                var pages = ''
                if(data.books[0]){
                    if(data.books[0].title.indexOf(name) >= 0){
                        pages = data.books[0].pages
                    }
                }
                callback(pages);
            }, 'jsonp');
        }
    },
    getBookTags: function(name, callback){
        var book_search_api = 'https://api.douban.com/v2/book/search';
        if(name != ''){
            $.get(book_search_api, {'count':'1','q':name}, function(data){
                var tags = new Array()
                if(data.books[0]){
                    if(data.books[0].title.indexOf(name) >= 0){
                        if(data.books[0].tags[0]){
                            tags.push(data.books[0].tags[0].name)
                        }
                        if(data.books[0].tags[1]){
                            tags.push(data.books[0].tags[1].name)
                        }
                        if(data.books[0].tags[2]){
                            tags.push(data.books[0].tags[2].name)
                        }
                    }
                }
                callback(tags);
            }, 'jsonp');
        }
    },
    getBookRating: function(name, callback){
        var book_search_api = 'https://api.douban.com/v2/book/search';
        if(name != ''){
            $.get(book_search_api, {'count':'1','q':name}, function(data){
                var rating = '';
                if(data.books[0]){
                    if(data.books[0].title.indexOf(name) >= 0){
                        rating = data.books[0].rating.average
                    }
                }
                callback(rating)
            }, 'jsonp');
        }
    },
    getMovieTags: function(name, callback){
        var movie_search_api = 'https://api.douban.com/v2/movie/search';
        if(name != ''){
            $.get(movie_search_api, {'count':'1','q':name}, function(data){
                var tags = new Array()
                if(data.subjects[0]){
                    if(data.subjects[0].title.indexOf(name) >= 0){
                        tags = new Array(data.subjects[0].genres)
                    }
                }
                callback(tags);
            }, 'jsonp');
        }
    },
    getBookRating: function(name, callback){
        var movie_search_api = 'https://api.douban.com/v2/movie/search';
        if(name != ''){
            $.get(movie_search_api, {'count':'1','q':name}, function(data){
                var rating = "";
                if(data.subjects[0]){
                    if(data.subjects[0].title.indexOf(name) >= 0){
                        rating = data.subjects[0].rating.average
                    }
                }
                callback(rating)
            }, 'jsonp');
        }
    }
});
