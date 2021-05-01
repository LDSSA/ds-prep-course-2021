# TODO: check that they reset the total weight
# TODO: check that the arguments are the right type

from io import StringIO
import sys
import inspect
import hashlib


def _hash(s):
    return hashlib.blake2b(bytes(s, encoding='utf8'), digest_size=5).hexdigest()


class Fruit:
    def __init__(self, name, price_per_unit, days_until_expired, nr_units=1):
        self.name = name
        self.nr_units = nr_units
        self.price_per_unit = price_per_unit
        self.days_until_expired = days_until_expired

    def calculate_price(self):
        return self.nr_units * self.price_per_unit


def get_fruits():
    apples = Fruit(name='apples',
                   price_per_unit=1,
                   nr_units=10,
                   days_until_expired=25)

    bananas = Fruit(name='bananas',
                    price_per_unit=2,
                    nr_units=6,
                    days_until_expired=7)

    oranges = Fruit(name='oranges',
                    price_per_unit=3,
                    nr_units=2,
                    days_until_expired=20)

    return apples, bananas, oranges


class Basket:
    def __init__(self):
        self.content = []

    def add_item(self, item):
        self.content.append(item)

    def remove_item(self, item):
        self.content.remove(item)

    def check_for_items_close_to_expire(self, n_days):
        for item in self.content:
            if item.days_until_expired <= n_days:
                print('The item {0} will expire in {1} days'.format(
                    item.name, item.days_until_expired))

    def check_total_price(self):
        total_price = 0
        for item in self.content:
            total_price += item.calculate_price()
        print('The total price is {0}'.format(total_price))

    def examine_basket(self):
        self.check_total_price()
        for item in self.content:
            print('- {0} {1} (total price {2})'.format(
                item.nr_units, item.name, item.calculate_price()))


class Toiletpaper:
    def __init__(self, name, price_per_unit, thickness, days_until_expired, nr_units=1):
        self.name = name
        self.thickness = thickness
        self.price_per_unit = price_per_unit
        self.nr_units = nr_units
        self.days_until_expired = days_until_expired

    def calculate_price(self):
        return self.price_per_unit


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout


def exercise_1_grading(pears, tangerines):
    for f in [pears, tangerines]:
        assert isinstance(f, Fruit)
    assert pears.price_per_unit == 3
    assert pears.name == 'pears'
    assert pears.nr_units == 4
    assert pears.days_until_expired == 14

    assert tangerines.price_per_unit == 6
    assert tangerines.name == 'tangerines'
    assert tangerines.nr_units == 2
    assert tangerines.days_until_expired == 2


def exercise_2_grading(calculate_price_of_all_fruits):
    apples, bananas, oranges = get_fruits()
    source = inspect.getsource(calculate_price_of_all_fruits)
    assert "return" in source, 'Did you forget to return?'
    assert ".calculate_price()" in source, 'We want you to use the .calculate_price method. Maybe you did the multiplication by hand instead?'
    assert "28" not in source, 'No answers in the function please. Sneaky sneaky.'

    assert calculate_price_of_all_fruits(
        [apples, bananas]), 'Tried running, but got nothing back. Are you returning anything?'

    error = "The total price seems wrong, maybe test it with some fruits from exercise 1?"
    assert calculate_price_of_all_fruits([apples, bananas, oranges]) == 28, error


def exercise_3_grading(my_basket, toilet_paper):
    assert isinstance(my_basket, Basket), 'Where is my_basket? Why is not a Basket?'
    assert isinstance(toilet_paper, Toiletpaper), 'Did you instanciate the toilet paper?'
    assert toilet_paper.thickness == 'Double leaf', 'How thick is this toilet paper?'

    total_value_in_basket = sum([item.calculate_price() for item in my_basket.content])
    assert total_value_in_basket <= 35, 'The basket is too expensive!'
    assert total_value_in_basket >= 30, 'The basket is not expensive enough!'

    for item in my_basket.content:
        if item.days_until_expired < 8:
            raise ValueError('There is something in your basket that will expire soon!')

    with Capturing() as output:
        my_basket.examine_basket()
    fruit_options = ['apples', 'pears', 'oranges', 'tangerines', 'bananas']
    assert sum([fruit in ''.join(output) for fruit in fruit_options]) >= 3, 'Not enough types of fruit!'
    assert Toiletpaper in [type(item) for item in my_basket.content], 'Forgot the toiletpaper? Big mistake...'


###############################
# From here on it's obsolete  #
###############################

import inspect


def exercise_4_grading(Item, chair, vase, pillow):
    # tests for the Item class
    assert hasattr(Item, '__init__'), 'What about the __init__?'

    # is the signature correct?
    sig = str(inspect.signature(Item.__init__))
    assert 'self' in sig, 'missing a self somewhere'
    assert ('name' in sig) and ('weight' in sig) and ('fragile' in sig), 'The __init__ signature has problems'
    assert 'broken' not in sig, 'Do you really need to pass broken every time there is a new Item?'

    # does it have the right attributes?
    source = inspect.getsource(Item.__init__).replace(" ", "")
    for attribute in ['name', 'weight', 'fragile', 'broken']:
        assert 'self.%s=' % attribute in source, 'What about the %s?' % attribute

    # did they create the right students?
    assert chair.weight + vase.weight + pillow.weight == 19, 'Are their weights correct?'


def exercise_5_grading(BasicBox):
    # tests for the Item class
    assert hasattr(BasicBox, '__init__'), 'What about the __init__?'

    # is the signature correct?
    sig = inspect.signature(BasicBox.__init__).parameters.keys()
    assert 'self' in sig, 'missing a self somewhere'
    assert ('weight_limit' in sig) and ('name' in sig), 'The __init__ signature has problems'
    # checking for the things that should not get passed
    for attribute in ['contents', 'weight', 'broken']:
        assert attribute not in sig, 'Do you really need to pass %s every time there is a new Item?' % attribute

    # does it have the right attributes?
    source = inspect.getsource(BasicBox.__init__).replace(" ", "")
    for attribute in ['name', 'contents', 'weight_limit', 'weight', 'broken']:
        assert 'self.%s=' % attribute in source, 'What about the %s?' % attribute

    # checking the method
    assert hasattr(BasicBox, 'add_item'), 'do you have a method to add items?'
    sig = inspect.signature(BasicBox.add_item)
    assert set(sig.parameters.keys()) == {'self', 'item'}, 'The method signature seems wrong'

    # checking that the box actually does what is expected
    test_item_1 = 'test 1, in reality this would be an item, not text'
    test_item_2 = 'test 2, in reality this would be an item, not text'

    test_box = BasicBox(name='my test box', weight_limit=1)
    test_box.add_item(test_item_1)
    test_box.add_item(test_item_2)
    assert len(test_box.contents) == 2
    assert test_box.contents[1] == test_item_2


class Item:
    def __init__(self, name, weight, fragile):
        self.name = name
        self.weight = weight
        self.fragile = fragile
        self.broken = False


def exercise_6_grading(Box):
    # tests for the Item class
    assert hasattr(Box, '__init__'), 'What about the __init__?'

    # is the signature correct?
    sig = inspect.signature(Box.__init__).parameters.keys()
    assert 'self' in sig, 'missing a self somewhere'
    assert ('weight_limit' in sig) and ('name' in sig), 'The __init__ signature has problems'
    # checking for the things that should not get passed
    for attribute in ['contents', 'weight', 'broken']:
        assert attribute not in sig, 'Do you really need to pass %s every time there is a new Item?' % attribute

    # does it have the right attributes?
    source = inspect.getsource(Box.__init__).replace(" ", "")
    for attribute in ['name', 'contents', 'weight_limit', 'weight', 'broken']:
        assert 'self.%s=' % attribute in source, 'What about the %s?' % attribute

    # checking add_item
    assert hasattr(Box, 'add_item'), 'do you have a method to add items?'
    sig = inspect.signature(Box.add_item)
    assert set(sig.parameters.keys()) == {'self', 'item'}, 'The add_item signature seems wrong'

    # checking calculate_total_weight
    assert hasattr(Box, 'calculate_total_weight'), 'do you have a method to calculate total weight?'
    sig = inspect.signature(Box.calculate_total_weight)
    assert set(sig.parameters.keys()) == {'self'}, 'The calculate_total_weight signature seems wrong'
    source = inspect.getsource(Box.calculate_total_weight).replace(" ", "")
    assert "self.contents" in source, "you need to use self.contents inside calculate_total_weight"

    # checking break_all_fragile_items
    assert hasattr(Box, 'break_all_fragile_items'), 'do you have a method to break all fragile items?'
    sig = inspect.signature(Box.break_all_fragile_items)
    assert set(sig.parameters.keys()) == {'self'}, 'The break_all_fragile_items signature seems wrong'
    source = inspect.getsource(Box.break_all_fragile_items).replace(" ", "")
    assert "self.contents" in source, "you need to use self.contents inside break_all_fragile_items"

    test_box = Box(name='my test box', weight_limit=8)
    test_item_1 = Item(name='test1', weight=4, fragile=True)
    test_item_2 = Item(name='test2', weight=3, fragile=False)
    test_box.add_item(test_item_1)
    test_box.add_item(test_item_2)
    test_box.break_all_fragile_items()
    assert test_item_1.broken, "Does not seem to break fragile items"
    assert not test_item_2.broken, "Breaks objects which aren't fragile!"

    # checking check_if_weight_limit_exceeded
    assert hasattr(Box, 'check_if_weight_limit_exceeded'), 'do you have a method to check_if_weight_limit_exceeded?'
    sig = inspect.signature(Box.check_if_weight_limit_exceeded)
    assert set(sig.parameters.keys()) == {'self'}, 'The check_if_weight_limit_exceeded signature seems wrong'
    source = inspect.getsource(Box.check_if_weight_limit_exceeded).replace(" ", "")
    assert "self.calculate_total_weight()" in source, "you need to use self.calculate_total_weight() inside check_if_weight_exceeded"
    assert "self.break_all_fragile_items()" in source, "you need to use self.break_all_fragile_items() inside check_if_weight_exceeded"

    test_box = Box(name='my test box', weight_limit=8)
    test_item_1 = Item(name='test1', weight=4, fragile=True)
    test_item_2 = Item(name='test2', weight=3, fragile=False)
    test_item_3 = Item(name='test3', weight=2, fragile=True)  # passes the weight limit here

    test_box.add_item(test_item_1)
    test_box.check_if_weight_limit_exceeded()
    assert not test_box.broken
    test_box.add_item(test_item_2)
    test_box.check_if_weight_limit_exceeded()
    assert not test_box.broken
    test_box.add_item(test_item_3)
    # it should not break before we check
    assert not test_box.broken
    test_box.check_if_weight_limit_exceeded()
    # now it should be broken!
    assert test_box.broken

    # now that the box has broken, did the right items break?
    assert test_item_1.broken
    assert not test_item_2.broken
    assert test_item_3.broken


# Player
def exercise_7_validate_Player(Player):
    # tests for the Item class
    assert hasattr(Player, '__init__'), 'What about the __init__?'

    # is the signature correct?
    sig = inspect.signature(Player.__init__).parameters.keys()
    assert 'self' in sig, 'missing a self somewhere'
    assert ('name' in sig) and ('salary' in sig) and ('accuracy' in sig), 'The __init__ signature has problems'

    # does it have the right attributes?
    source = inspect.getsource(Player.__init__).replace(" ", "")
    for attribute in ['name', 'salary', 'accuracy']:
        assert 'self.%s=' % attribute in source, 'What about the %s?' % attribute

    # checking add_item
    assert hasattr(Player, 'attempt_to_score'), 'do you have a method to attempt_to_score?'
    sig = inspect.signature(Player.attempt_to_score)
    assert set(sig.parameters.keys()) == {'self'}, 'The attempt_to_score signature seems wrong'

    test_player_1 = Player(name='test1', salary=1, accuracy=0)
    test_player_2 = Player(name='test1', salary=1, accuracy=5)
    test_player_3 = Player(name='test1', salary=1, accuracy=100)

    nr_scores_player_1 = 0
    nr_scores_player_2 = 0
    nr_scores_player_3 = 0

    for _ in range(1000):
        if test_player_1.attempt_to_score():
            nr_scores_player_1 += 1

        if test_player_2.attempt_to_score():
            nr_scores_player_2 += 1

        if test_player_3.attempt_to_score():
            nr_scores_player_3 += 1

    assert nr_scores_player_1 == 0, "A player with accuracy 0 is scoring points"
    assert 0 < nr_scores_player_2 < 1000, "A player with accuracy 5 should both fail and miss shots"
    assert nr_scores_player_3 == 1000, "A player with ridiculously good accuracy should never miss"


def exercise_7_validate_Team(Team, Player):
    # tests for the Item class
    assert hasattr(Team, '__init__'), 'What about the __init__?'

    # is the signature correct?
    sig = inspect.signature(Team.__init__).parameters.keys()
    assert 'self' in sig, 'missing a self somewhere'
    assert ('name' in sig) and ('budget' in sig), 'The __init__ signature has problems'

    # does it have the right attributes?
    source = inspect.getsource(Team.__init__).replace(" ", "")
    for attribute in ['name', 'budget', 'players', 'wins', 'games_played', 'points_in_game']:
        assert 'self.%s=' % attribute in source, 'What about the %s attribute?' % attribute

    # checking hire_player
    assert hasattr(Team, 'hire_player'), 'do you have a method to hire a player?'
    sig = inspect.signature(Team.hire_player)
    assert set(sig.parameters.keys()) == {'self', 'player'}

    # attempt to hire player with budget
    test_team = Team(name='test_team', budget=10)
    player = Player(name='test', accuracy=1, salary=7)
    test_team.hire_player(player)
    assert player in test_team.players

    # attempt to hire multiple players with budget
    test_team = Team(name='test_team', budget=10)
    player_1 = Player(name='test 1', accuracy=1, salary=5)
    player_2 = Player(name='test 2', accuracy=1, salary=5)
    test_team.hire_player(player_1)
    test_team.hire_player(player_2)
    assert player_1 in test_team.players
    assert player_2 in test_team.players

    # attempt to hire player without budget
    test_team = Team(name='test_team', budget=10)
    player = Player(name='test', accuracy=1, salary=12)
    test_team.hire_player(player)
    assert player not in test_team.players

    # attempt to hire players with enough budget for just the first one
    test_team = Team(name='test_team', budget=10)
    player_1 = Player(name='test 1', accuracy=1, salary=6)
    player_2 = Player(name='test 2', accuracy=1, salary=6)
    test_team.hire_player(player_1)
    test_team.hire_player(player_2)
    assert player_1 in test_team.players
    assert player_2 not in test_team.players

    # checking fire_player
    test_team = Team(name='test_team', budget=20)
    player_1 = Player(name='test 1', accuracy=1, salary=6)
    player_2 = Player(name='test 2', accuracy=1, salary=6)
    test_team.hire_player(player_1)
    test_team.hire_player(player_2)
    test_team.fire_player(player_1)
    assert player_1 not in test_team.players
    assert player_2 in test_team.players
    assert test_team.budget == 14

    # checking reset_points
    assert hasattr(Team, 'reset_points'), 'do you have a method to reset_points?'
    sig = inspect.signature(Team.reset_points)
    assert set(sig.parameters.keys()) == {'self'}

    test_team = Team(name='test_team', budget=20)
    assert test_team.points_in_game == 0
    test_team.points_in_game = 5
    assert test_team.points_in_game == 5
    test_team.reset_points()
    assert test_team.points_in_game == 0

    # checking all_players_attempt_to_score
    assert hasattr(Team, 'all_players_attempt_to_score'), 'do you have a method all_players_attempt_to_score?'
    sig = inspect.signature(Team.all_players_attempt_to_score)
    assert set(sig.parameters.keys()) == {'self'}

    source = inspect.getsource(Team.all_players_attempt_to_score).replace(" ", "")
    assert "self.reset_points()" in source

    test_player_1 = Player(name='test1', salary=1, accuracy=100)
    test_player_2 = Player(name='test1', salary=1, accuracy=100)
    test_player_3 = Player(name='test1', salary=1, accuracy=0)
    test_team = Team(name='test_team', budget=20)
    test_team.hire_player(test_player_1)
    test_team.hire_player(test_player_2)
    test_team.hire_player(test_player_3)
    test_team.all_players_attempt_to_score()
    assert test_team.points_in_game == 2
    test_team.fire_player(test_player_2)
    test_team.all_players_attempt_to_score()
    assert test_team.points_in_game == 1


def exercise_8_validate_League(League, Team, Player):
    # tests for the Item class
    def test_item_class(League):
        assert hasattr(League, '__init__'), 'What about the __init__?'
        # is the signature correct?
        sig = inspect.signature(League.__init__).parameters.keys()
        assert 'self' in sig, 'missing a self somewhere'
        assert ('name' in sig), 'The __init__ signature has problems'

        # does it have the right attributes?
        source = inspect.getsource(League.__init__).replace(" ", "")
        for attribute in ['name', 'teams', 'games']:
            assert 'self.%s=' % attribute in source, 'What about the %s attribute?' % attribute

    def test_add_team(League, Team, Player):
        assert hasattr(League, 'add_team'), 'do you have a method to add a team?'
        sig = inspect.signature(League.add_team)
        assert set(sig.parameters.keys()) == {'self', 'team'}

        # test that an acceptable team will work
        test_player = Player(name='test', salary=1, accuracy=0)
        test_team = Team(name='test_team', budget=20)
        for _ in range(5):
            test_team.hire_player(test_player)
        test_league = League('test')
        test_league.add_team(test_team)
        assert len(test_league.teams) == 1
        test_league.add_team(test_team)
        assert len(test_league.teams) == 2

        # test that teams that are too small and too large won't be accepted
        test_player = Player(name='test', salary=1, accuracy=0)
        test_team_1 = Team(name='test_team', budget=20)
        test_team_2 = Team(name='test_team', budget=20)
        test_team_3 = Team(name='test_team', budget=20)
        for _ in range(5):
            test_team_1.hire_player(test_player)
        for _ in range(7):
            test_team_2.hire_player(test_player)
        for _ in range(3):
            test_team_3.hire_player(test_player)
        test_league = League('test')
        test_league.add_team(test_team_1)
        assert len(test_league.teams) == 1
        test_league.add_team(test_team_2)
        assert len(test_league.teams) == 1
        test_league.add_team(test_team_3)
        assert len(test_league.teams) == 1

    # checking declare_game_winner
    def test_declare_winner(League, Team):
        assert hasattr(League, 'declare_game_winner'), 'do you have a method to declare a winner of a game?'
        sig = inspect.signature(League.declare_game_winner)
        assert set(sig.parameters.keys()) == {'self', 'team_1', 'team_2'}

        # check team 1 wins
        test_team_1 = Team(name='test_team', budget=20)
        test_team_2 = Team(name='test_team', budget=20)
        test_team_1.points_in_game = 7
        test_team_2.points_in_game = 5
        test_league = League('test')
        test_league.declare_game_winner(test_team_1, test_team_2)
        assert test_team_1.wins == 1
        test_league.declare_game_winner(test_team_1, test_team_2)
        assert test_team_1.wins == 2
        test_team_2.points_in_game = 10
        test_league.declare_game_winner(test_team_1, test_team_2)
        assert test_team_1.wins == 2
        assert test_team_2.wins == 1

        # check draw
        test_team_1 = Team(name='test_team', budget=20)
        test_team_2 = Team(name='test_team', budget=20)
        test_team_1.points_in_game = 5
        test_team_2.points_in_game = 5
        test_league = League('test')
        test_league.declare_game_winner(test_team_1, test_team_2)
        assert test_team_1.wins == 0
        assert test_team_2.wins == 0

        # check run_game

    def test_run_game(League, Team, Player):

        # check the actual source
        source = inspect.getsource(League.run_game).replace(" ", "")
        assert ".all_players_attempt_to_score()" in source
        assert "self.declare_game_winner" in source

        # running a unit test
        test_team_1 = Team(name='test_team', budget=1000)
        test_team_2 = Team(name='test_team', budget=1000)
        test_team_3 = Team(name='test_team', budget=1000)
        test_player = Player(name='test', accuracy=5, salary=1)
        test_league = League('test')

        for team in [test_team_1, test_team_2, test_team_3]:
            for _ in range(5):
                # we need to hire 5 players, or they won't be able to join the league
                team.hire_player(test_player)
            # add the team to the league
            test_league.add_team(team)
        for _ in range(1000):
            test_league.run_game(test_team_1, test_team_2)

        assert 0 < test_team_1.wins < 1000
        assert 0 < test_team_2.wins < 1000
        assert test_team_1.games_played == 1000
        assert test_team_3.games_played == 0
        assert test_team_3.wins == 0

    test_item_class(League)
    test_add_team(League, Team, Player)
    test_declare_winner(League, Team)
    test_run_game(League, Team, Player)
