# Author: James Rowan
# GitHub username: jamesrowan672
# Date: Tues Nov 29
# Description: Project 10

class Movie ():

    def __init__(self, title, genre, director, year):
        '''Initialize movie object.'''
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year
    
    def get_title(self):
        '''Get title of movie.'''
        return self._title
    
    def get_genre(self):
        '''Get genre of movie.'''
        return self._genre

    def get_year(self):
        '''Get year of movie.'''
        return self._year

class StreamingService ():

    def __init__(self, name):
        '''Initialize Streaming Service object.'''
        self._name = name
        self._catalog = {}

    def get_name(self):
        '''Get name of streaming service.'''
        return self._name

    def get_catalog(self):
        '''Get catalog of streaming service.'''
        return self._catalog

    def add_movie(self, movie):
        '''Add movie to catalog.'''
        self._catalog[movie.get_title()] = [movie.get_genre(), movie.get_year()]

    def delete_movie(self, movie):
        '''Remove movie from catalog.'''
        del self._catalog[movie]

class StreamingGuide ():

    def __init__(self):
        '''Initialize Streaming Guide object.'''
        self._streaming_services = []

    def add_streaming_service(self, streaming_service):
        '''Add streaming service to streaming guide.'''
        self._streaming_services.append(streaming_service)

    def delete_streaming_service(self, streaming_service):
        '''Delete streaming service from streaming guide.'''
        if streaming_service in self._streaming_services:
            self._streaming_services.remove(streaming_service)

    def where_to_watch(self, movie):
        '''Get list of streaming services for movie.'''
        service_list = []
        for i in self._streaming_services:
            catalog = i.get_catalog()
            if movie in catalog:
                movie_list = [movie + ' ' + f'({catalog[movie][1]})']
                service_list.append(i.get_name())
        return movie_list + service_list
