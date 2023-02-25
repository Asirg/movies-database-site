# from django.shortcuts import render
# from django.http import JsonResponse

# from watchlist.models import Movie


# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {'movies': list(movies.values())}

#     return JsonResponse(
#         data,
#         status=201
#     )

# def movie_detail(request, pk):
#     movies = Movie.objects.get(id=pk)
#     data = {
#         'name': movies.name,
#         'description': movies.description,
#         'active': movies.active,
#     }

#     return JsonResponse(
#         data,
#         status=201
#     )
