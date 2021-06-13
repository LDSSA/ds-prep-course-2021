import numpy as np


def test_exercise_2_I(read_cities):
    cities_locations_data = read_cities('cities_locations_large.csv')

    assert len(cities_locations_data) == 15

    assert 'Barcelona' in cities_locations_data
    barcelona = cities_locations_data['Barcelona']
    assert barcelona['idx'] == 10
    assert barcelona['country'] == 'Spain'
    np.testing.assert_almost_equal(barcelona['lat'], 41.3833, decimal=3)
    np.testing.assert_almost_equal(barcelona['lng'], 2.1834, decimal=3)

    assert 'Ottawa' in cities_locations_data
    ottawa = cities_locations_data['Ottawa']
    assert ottawa['idx'] == 2
    assert ottawa['country'] == 'Canada'
    np.testing.assert_almost_equal(ottawa['lat'], 45.4167, decimal=3)
    np.testing.assert_almost_equal(ottawa['lng'], -75.7, decimal=3)


def test_exercise_2_II(create_dist_matrix):
    cities_locations_data = {
        'Andorra la Vella': {'idx': 0, 'lat': 42.5, 'lng': 1.5165, 'country': 'Andorra'},
        'Toronto': {'idx': 1, 'lat': 43.7, 'lng': -79.42, 'country': 'Canada'},
        'Ottawa': {'idx': 2, 'lat': 45.4167, 'lng': -75.7, 'country': 'Canada'},
        'Paris': {'idx': 3, 'lat': 48.8667, 'lng': 2.3333, 'country': 'France'},
        'Lyon': {'idx': 4, 'lat': 45.77, 'lng': 4.83, 'country': 'France'},
        'Rome': {'idx': 5, 'lat': 41.896, 'lng': 12.4833, 'country': 'Italy'},
        'Milan': {'idx': 6, 'lat': 45.47, 'lng': 9.205, 'country': 'Italy'},
        'Lisbon': {'idx': 7, 'lat': 38.7227, 'lng': -9.1449, 'country': 'Portugal'},
        'Porto': {'idx': 8, 'lat': 41.15, 'lng': -8.62, 'country': 'Portugal'},
        'Madrid': {'idx': 9, 'lat': 40.4, 'lng': -3.6834, 'country': 'Spain'},
        'Barcelona': {'idx': 10, 'lat': 41.3833, 'lng': 2.1834, 'country': 'Spain'},
        'Washington': {'idx': 11, 'lat': 38.9047, 'lng': -77.0163, 'country': 'United States'},
        'Atlanta': {'idx': 12, 'lat': 33.7627, 'lng': -84.4225, 'country': 'United States'},
        'Harare': {'idx': 13, 'lat': -17.8178, 'lng': 31.0447, 'country': 'Zimbabwe'},
        'Bulawayo': {'idx': 14, 'lat': -20.17, 'lng': 28.58, 'country': 'Zimbabwe'}
    }

    dists = create_dist_matrix(cities_locations_data)

    assert type(dists) == np.ndarray
    assert dists.shape == (15, 15)

    for i in range(dists.shape[0]):
        assert dists[i][i] == 0
        
    np.testing.assert_almost_equal(dists[7][13], 7531.40, decimal=1)
    np.testing.assert_almost_equal(dists[4][8], 1201.40, decimal=1)


def test_exercise_2_III(furthest_cities):
    np.random.seed(23)
    dists = np.random.rand(10, 10) * 1000
    for i in range(dists.shape[0]):
        dists[i][i] = 0
        for j in range(dists.shape[1]):
            if j > i:
                dists[i][j] = dists[j][i]

    idx_1, idx_2 = furthest_cities(dists)
    assert idx_1 == 5
    assert idx_2 == 6


def test_exercise_3_II(battle, Pokemon):
    charmander = Pokemon(name='Charmander', max_health=25, speed=5)
    charmander.level = 6
    squirtle = Pokemon(name='Squirtle', max_health=30, speed=10)
    squirtle.level = 5

    np.random.seed(23)
    winner, loser = battle(charmander, squirtle)

    assert winner.name == "Squirtle"
    assert loser.name == "Charmander"
    assert winner.hp == 6
    assert loser.hp == 0
