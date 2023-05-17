from mrjob.job import MRJob
from mrjob.step import MRStep
from dateutil.parser import parse


class MovieAnalysis(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
        ]

    def mapper(self, _, line):
        row = line.strip().split(",")

        user = None
        movie = None
        rating = None
        genre = None
        date = None

        try:
            user = int(row[0])
            movie = int(row[1])
            rating = int(row[2])
            genre = row[3]
            date = parse(row[4])
        except:
            pass
        else:
            yield (f"user-nummovies-score-{user}", (1, rating))
            yield (f"movie-numusers-score-{movie}", (1, rating))
            yield ("minmax-daymovies", (row[4], 1))
            yield ("extreme-score-day", (row[4], rating))
            yield ("extreme-score-genre", (genre, rating))

    def reducer(self, key, values):
        if key.startswith("user-nummovies-score-"):
            num_movies = 0
            acc_rating = 0

            for count, rating in values:
                num_movies += count
                acc_rating += rating

            yield key, (num_movies, acc_rating / num_movies)

        if key.startswith("movie-numusers-score-"):
            num_users = 0
            acc_rating = 0

            for count, rating in values:
                num_users += count
                acc_rating += rating

            yield key, (num_users, acc_rating / num_users)

        if key == "minmax-daymovies":
            days = {}

            for date, count in values:
                if date in days:
                    days[date] += count
                else:
                    days[date] = count

            max_day = max(days, key=days.get)
            min_day = min(days, key=days.get)

            yield "max-daymovies", max_day
            yield "min-daymovies", min_day

        if key == "extreme-score-day":
            days = {}

            for date, rating in values:
                if date in days:
                    days[date].append(rating)
                else:
                    days[date] = [rating]

            worst_day = min(days, key=lambda d: sum(days[d]) / len(days[d])) if days else None
            best_day = max(days, key=lambda d: sum(days[d]) / len(days[d])) if days else None

            if worst_day is not None:
                yield "worst-score-day", (worst_day, sum(days[worst_day]) / len(days[worst_day]))
            if best_day is not None:
                yield "best-score-day", (best_day, sum(days[best_day]) / len(days[best_day]))

        if key == "extreme-score-genre":
            genres = {}

            for genre, rating in values:
                if genre in genres:
                    genres[genre].append(rating)
                else:
                    genres[genre] = [rating]

            worst_genre = min(genres, key=lambda g: sum(genres[g]) / len(genres[g])) if genres else None
            best_genre = max(genres, key=lambda g: sum(genres[g]) / len(genres[g])) if genres else None

            if worst_genre is not None:
                yield "worst-score-genre", (worst_genre, sum(genres[worst_genre]) / len(genres[worst_genre]))
            if best_genre is not None:
                yield "best-score-genre", (best_genre, sum(genres[best_genre]) / len(genres[best_genre]))


if __name__ == '__main__':
    MovieAnalysis.run()
