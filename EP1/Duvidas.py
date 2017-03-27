Professor, tive um problema com uma url do film_flow. Caso eu coloque qualquer trecho abaixo de 
qualquer uma das declarações de url dos details, tenho syntax error

    
    url(r'^albuns/(?P<album_id>[0-9]+)', views.album_detail, name = 'album_detail')

    ou 

    url(r'^musics/(?P<music_id>[0-9]+)', views.music_detail, name = 'music_detail')

já tentei tirar nome, espaçamento e nada da certo, então fiquei sem o music_detail mesmo.
Caso eu comente as linhas abaixo da sentença que vier primeiro, o problema é resolvido.