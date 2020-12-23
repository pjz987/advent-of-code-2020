from parse_input import parse_string

player1_raw = parse_string('43input.txt').split('\n\n')[0]
player2_raw = parse_string('43input.txt').split('\n\n')[1]

class Player:
  def __init__(self, raw_player_info):
    self.name = raw_player_info.split('\n')[0].strip(':')
    raw_deck = raw_player_info.split('\n')[1:]
    self.deck = [int(card) for card in raw_deck][::-1]
  
  def draw(self):
    return self.deck.pop()

  def collect(self, player_card, opponent_card):
    deck = [opponent_card, player_card]
    deck.extend(self.deck)
    self.deck = deck
  
  def check_deck(self):
    if len(self.deck) == 0:
      return True
  
  def score(self):
    count = 0
    for i, card in enumerate(self.deck):
      count += card * (i + 1)
    return count

player1 = Player(player1_raw)
player2 = Player(player2_raw)

winner = None

while True:
  card1 = player1.draw()
  card2 = player2.draw()

  if card1 > card2:
    player1.collect(card1, card2)
    winner = player1 if player2.check_deck() else None
  elif card2 > card1:
    player2.collect(card2, card1)
    winner = player2 if player1.check_deck() else None

  if winner:
    break

print(winner.score())