movie_schedules = {
    "Terminator":"11:00am",
    "The Eternals":"3:00pm",
    "Bond":"4:00pm"
}

print('Following movies are being played')
for key in movie_schedules:
    print(key)

movie = input('Enter a movie')
schedule = movie_schedules.get(movie)

if not schedule:
    print('Requested move', movie,'is not being played')
else:
    print('Requested movie', movie, 'is played at', schedule)