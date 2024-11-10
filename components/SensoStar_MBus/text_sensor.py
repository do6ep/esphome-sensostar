import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor
from esphome.const import (
	CONF_STATUS,
)

from . import SensoStarComponent, CONF_SENSOSTAR_ID

TYPES = [
    CONF_STATUS,
]

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_SENSOSTAR_ID): cv.use_id(SensoStarComponent),
		cv.Optional(CONF_STATUS): text_sensor.text_sensor_schema(),
    }
).extend(cv.COMPONENT_SCHEMA)


async def setup_conf(config, key, hub):
    if sensor_config := config.get(key):
        sens = await text_sensor.new_text_sensor(sensor_config)
        cg.add(getattr(hub, f"set_{key}_text_sensor")(sens))


async def to_code(config):
    hub = await cg.get_variable(config[CONF_SENSOSTAR_ID])
    for key in TYPES:
        await setup_conf(config, key, hub)