# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\midi-remote-scripts\APC40_MkII\__init__.py
from _Framework.Capabilities import CONTROLLER_ID_KEY, PORTS_KEY, NOTES_CC, SCRIPT, SYNC, REMOTE, controller_id, inport, outport
from APC40_MkII_Mod import APC40_MkII_Mod

def create_instance(c_instance):
    return APC40_MkII_Mod(c_instance)


def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=2536, product_ids=[41], model_name='Akai APC40 MkII'),
     PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT, REMOTE]), outport(props=[SYNC, SCRIPT, REMOTE])]}