import os
from lxml import etree as ET
from xml.etree import ElementTree as ETree

source_path = 'game-data/mod'
original_path = 'game-data/original'
target_path = 'game-data/transposition'
transposition_config = [
    { "name": "ArmyTemplate", "key": "ArmyTemplateId", "properties": ["Name"]},
    { "name": "Artifact", "key": "ArtifactId", "properties": ["Name", "Description"]},
    { "name": "ColonyEventDefinition", "key": "ColonyEventDefinitionId", "properties": ["Name", "Description"]},
    { "name": "ComponentDefinition", "key": "ComponentId", "properties": ["Name"]},
    { "name": "CreatureType", "key": "CreatureTypeId", "properties": ["Name", "Description"]},
    { "name": "FleetTemplate", "key": "FleetTemplateId", "properties": ["Name", "Description"]},
    { "name": "GameEvent", "key": "Name", "properties": ["Title", "Description", "TriggerActions/GameEventAction/Description", "TriggerActions/GameEventAction/MessageTitle", "TriggerActions/GameEventAction/ChoiceButtonText", "PlacementActions/GameEventAction/Description", "PlacementActions/GameEventAction/MessageTitle"]},
    { "name": "Government", "key": "GovernmentId", "properties": ["Name", "Description", "LeaderTitle"]},
    { "name": "OrbType", "key": "OrbTypeId", "properties": ["Name"]},
    { "name": "PlanetaryFacilityDefinition", "key": "PlanetaryFacilityDefinitionId", "properties": ["Name"]},
    { "name": "Race", "key": "RaceId", "properties": ["Name", "Description", "FeatureExplanations/string"]},
    { "name": "ResearchProjectDefinition", "key": "ResearchProjectId", "properties": ["Name", "DiplomacyFactors/EmpireIncidentFactor/Description"]},
    { "name": "Resource", "key": "ResourceId", "properties": ["Name", "Description"]},
    { "name": "ShipHull", "key": "ShipHullId", "properties": ["Name"]},
    { "name": "SpaceItemDefinition", "key": "SpaceItemDefinitionId", "properties": ["Name"]},
    { "name": "TroopDefinition", "key": "TroopDefinitionId", "properties": ["Name"] }
]

file_names = os.listdir(source_path)

# For each config
for config in transposition_config:
    source_files = [name for name in file_names if config.get("name") in name]

    # For each file available for that particular config (based on config 'name' prop)
    for src_file in source_files:
        print(f"transpose {src_file}.")

        src_root = ET.parse(f"{source_path}/{src_file}")
        orig_root = ET.parse(f"{original_path}/{src_file}")

        source_items = src_root.xpath(config.get('name'))
        original_items = orig_root.xpath(config.get('name'))

        # For each source item of that config 'name' (source item = translated (mod))
        for src_item in source_items:
            key_item_find = src_item.xpath(config.get('key'))
            orig_item_find = orig_root.xpath(f""".//{config.get('name')}[{config.get('key')}[text()="{key_item_find[0].text}"]]""")

            if len(key_item_find) == 0 or len(orig_item_find) == 0:
                continue

            key_item = key_item_find[0]
            orig_item = orig_item_find[0]

            properties = config.get('properties')

            # For each property defined in the config
            for prop in properties:
                src_prop = src_item.xpath(prop)
                orig_prop = orig_item.xpath(prop)

                if len(src_prop) == 0 or len(orig_prop) == 0:
                    continue

                # For each element matched within that prop
                for i, elem in enumerate(src_prop):
                    if len(orig_prop) - i <= 0:
                        continue

                    orig_prop[i].text = elem.text

        orig_root.write(f"{target_path}/{src_file}", encoding="utf-8", xml_declaration=True)