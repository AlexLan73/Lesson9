"""
Урок #9 - "Игра в дурака"

Дмитрий, доброе время суток))
С наступившим новым годом, здоровье и всех благ)))
Задача интересная )  
Попробовал: генератор, всякие фильтры,
Три заветных слова ))) применительно к class (как в видео)
Сравнение class...
try: - разные
Но задача ОЧЕНЬ большая + если делать хорошо нужно писать логику игры- 
а это очень долго.
Дмитрий, учусь на двух курсах + работа 
Сделал: Колода, перемешать колоду, выдвть с помощью генератора, 
выбрать с чего ходить, сделать "Бой карт" если бьешь карты списываются если нет 
переходят на руки
Без козырей.

"""

import OneGames as og
import copy


if __name__ == "__main__":
    deck= og.Deck()
    ls= deck.mix_deck()

    human=og.OneGrunt()
    human.add(dd=deck.read_carf(3))
    comp=og.OneGrunt()
    comp.add(dd= deck.read_carf(20))

    comp_cards=og.ComparCards()
    b,  card_ = comp_cards.betters(d0= human.deck, d1= comp.deck)
    if b:
        # Побили карты можно заменить(удалить карты из двух рук)
         comp.deck=copy.deepcopy(card_)
    else:
        # Не побили нужно добавить карты в одни руки и удалить из других
        comp.add(dd= human.deck)    
    b,  card_= comp_cards.better(d0= human.deck, d1= comp.deck)
    if b:
        comp.sub(card_.id)

    x0= og.ComparCard(d0= human.deck) == og.ComparCard(d0= comp.deck)
    x1= og.ComparCard(d0= human.deck) < og.ComparCard(d0= comp.deck)
    x2= og.ComparCard(d0= human.deck) > og.ComparCard(d0= comp.deck)

    games= og.OneGames(False, human, comp)
    games.run() # не доделал
