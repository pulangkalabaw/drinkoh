import random
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

# show all remaining cards
def remaining(request):
    rem_cards = request.session['rem_cards']
    return JsonResponse(rem_cards, safe=False)

# show all drawed cards
def drawed(request):
    drawed_cards = request.session['drawed_cards']
    return JsonResponse(drawed_cards, safe=False)

# setup cards
def init(request):
    all_cards = [
        { 'id': 1, 'm': 'You drink 1 shot!'},
        { 'id': 2, 'm': 'Everybody will drink 2 shots!'},
        { 'id': 3, 'm': 'Pick a person to drink 2 shots!'},
        { 'id': 4, 'm': 'If you\'re not single, you\'ll drink 2 shots! or else everyone (except one) will drink 1 shot'},
    ]

    request.session['all_cards'] = all_cards
    request.session['rem_cards'] = all_cards
    request.session['drawed_card'] = []
    request.session['drawed_cards'] = []

    return redirect('start')

# start the game
def start(request):

    all_cards = request.session['all_cards']
    rem_cards = request.session['rem_cards']
    drawed_card = request.session['drawed_card']
    drawed_cards = request.session['drawed_cards']

    return render(request, 'app/index.html',{
        'all_cards': all_cards,
        'rem_cards': rem_cards,
        'drawed_card': drawed_card,
        'drawed_cards': drawed_cards,
    })

# draw a card
def draw(request):

    all_cards = request.session['all_cards']
    rem_cards = request.session['rem_cards']
    drawed_card = request.session['drawed_card']
    drawed_cards = request.session['drawed_cards']
    rem_cards_counts = len(request.session['rem_cards']) - 1

    # count the rem cards first
    if rem_cards_counts < 0: # if its has no more rem all_cards

        # return to start
        return redirect('start')

    # random
    rand = random.randint(0, rem_cards_counts)

    # save this card to drawed_card (object)
    drawed_card = rem_cards[rand]

    # add this random card to drawed cards (array)
    drawed_cards.append(drawed_card)

    # delete drawed card (object) to drawed_cards (array)
    del rem_cards[rand]

    # save all session
    request.session['all_cards'] = all_cards
    request.session['rem_cards'] = rem_cards
    request.session['drawed_card'] = drawed_card
    request.session['drawed_cards'] = drawed_cards

    # return redirect('start')
    return JsonResponse({
        'status': 200,
        'message': len(rem_cards)
    }, safe=False)
