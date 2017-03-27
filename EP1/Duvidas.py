Professor, tive um problema com uma url do film_flow. Caso eu coloque o trecho abaixo nas linhas
abaixo de onde eu defino os urls pra albuns_list, fala que tem problema de sintaxe

	#film_flow/musics/
    url(r'^musics/$', views.show_musics, name = 'musics_list'),