"""
Notes
Ranges are in euclidian distance
"""

# General constants
BOARD_WIDTH = 40
BOARD_HEIGHT = 40
MIN_ELEVATION = -20
MAX_ELEVATION = 20
TIME_LIMIT = 0.1

## Buildings

# HQ constants
RED_HQ_LOCATION = (5, 5)
BLUE_HQ_LOCATION = (35, 35)
HQ_HEALTH = 200
HQ_MAX_SPAWNS = 1
HQ_SENSE_RANGE = 36
HQ_SPAWN_RADIUS = 2
HQ_OIL_PRODUCTION = 8

# Refinery constants
REFINERY_HEALTH = 50
REFINERY_COST = 40
REFINERY_PRODUCTION = 5
REFINERY_SENSE_RANGE = 25

# Turrets constants
TURRET_HEALTH = 50
TURRET_COST = 15
TURRET_DAMAGE = 10
TURRET_ATTACK_COST = 3
TURRET_ATTACK_RANGE = 13
TURRET_SENSE_RANGE = 25
TURRET_AOE = 0

# Barracks constants
BARRACKS_HEALTH = 50
BARRACKS_COST = 25
BARRACKS_MAX_SPAWNS = 3
BARRACKS_SPAWN_RADIUS = 2
BARRACKS_SENSE_RANGE = 8

# Walls constants
WALL_HEALTH = 40
WALL_COST = 2

## Troops constants

# Builders constants
BUILDER_HEALTH = 75
BUILDER_COST = 10
BUILDER_SPAWN_RADIUS = 2
BUILDER_MAX_SPAWNS = 1
BUILDER_SPEED = 8
BUILDER_SENSE_RANGE = 20

# Tank constants
TANK_HEALTH = 75
TANK_COST = 10
TANK_DAMAGE = 30
TANK_ATTACK_COST = 5
TANK_ATTACK_RANGE = 2
TANK_SPEED = 2
TANK_SENSE_RANGE = 25
TANK_AOE = 0

# Gunner constants
GUNNER_HEALTH = 20
GUNNER_COST = 5
GUNNER_DAMAGE = 10
GUNNER_ATTACK_COST = 2
GUNNER_ATTACK_RANGE = 5
GUNNER_SPEED = 2
GUNNER_SENSE_RANGE = 36
GUNNER_AOE = 0

# Grenade launcher constants
GRENADER_HEALTH = 10
GRENADER_COST = 5
GRENADER_SPEED = 2
GRENADER_SENSE_RANGE = 25
# Stun grenade constants
GRENADER_STUN_TURNS = 2
GRENADER_STUN_COST = 10
GRENADER_STUN_AOE = 2
GRENADER_STUN_RANGE = 5
# Damage grenade constants
GRENADER_DAMAGE_COST = 4
GRENADER_DAMAGE_AOE = 2
GRENADER_DAMAGE_DAMAGE = 8
GRENADER_DAMAGE_RANGE = 5

# Blockchain constants
BLOCKCHAIN_BYTE_COUNT = 5
BLOCKCHAIN_MIN_NUM_SIZE = 0
BLOCKCHAIN_MAX_NUM_SIZE = 255
