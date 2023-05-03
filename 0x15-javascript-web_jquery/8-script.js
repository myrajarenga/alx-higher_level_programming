$(document).ready(function() {
  $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
    var movieList = "";
    $.each(data.results, function(index, movie) {
      movieList += "<li>" + movie.title + "</li>";
    });
    $("ul#list_movies").html(movieList);
  });
});
