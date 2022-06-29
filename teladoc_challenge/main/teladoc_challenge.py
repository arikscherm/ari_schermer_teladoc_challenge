import requests

#Creates and returns a list of movie titles found on a specified page number of results.
def get_movie_titles_from_page(search_parameter,page_number):
	response = requests.get('https://jsonmock.hackerrank.com/api/movies/search/', params={"Title": search_parameter, "page":page_number}).json()
	titles = [movie_object["Title"] for movie_object in response["data"]] #Extract the movie titles from the response and create a list
	return titles

#Creates and returns an alphabetically sorted list of movie titles from all pages associated with a specified search parameter.
def get_movie_titles(search_parameter):
	page_number = 1
	response = requests.get('https://jsonmock.hackerrank.com/api/movies/search/', params={"Title": search_parameter, "page":page_number}).json() #Make first call to Movie Titles API to get the total number of pages and the first page of movie titles
	titles = sorted([movie_object["Title"] for movie_object in response["data"]]) #Extract the movie titles from the response and create a sorted list
	total_pages =  response["total_pages"]
	page_number += 1
	while(page_number <= total_pages): #Continue getting movie titles from the next page until we have reached the last page.
		titles.extend(sorted(get_movie_titles_from_page(search_parameter,page_number)))
		page_number += 1	
	return titles