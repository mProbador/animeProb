import utils
import charts
import read_anime
import collections



if __name__ == '__main__':
    data = read_anime.ani_csv('./my_proyect2/anime.csv')
    animes, ratings = utils.get_rating_ani(data)
    charts.generate_pie_chart(animes, ratings)
    charts.generat_bar_chart(animes, ratings)
