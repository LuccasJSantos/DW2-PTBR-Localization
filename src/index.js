import * as translate from './modules/translate.js'
import xmlParser from './modules/translation/parsers/xml.js'

const translateResearchProjectDefinitions = async function () {
    const parser = xmlParser(['ArrayOfResearchProjectDefinition', 'ResearchProjectDefinition', 'Name'])
    const translation = await translate.file('game-data/original/ResearchProjectDefinitions.xml', { parser })
    return translation
}

const translateResearchProjectDefinitionsDhayut = async function () {
    const parser = xmlParser(['ArrayOfResearchProjectDefinition', 'ResearchProjectDefinition', 'Name'])
    const translation = await translate.file('game-data/original/ResearchProjectDefinitions_Dhayut.xml', { parser })
    return translation
}

const translateResearchProjectDefinitionsGizurean = async function () {
    const parser = xmlParser(['ArrayOfResearchProjectDefinition', 'ResearchProjectDefinition', 'Name'])
    const translation = await translate.file('game-data/original/ResearchProjectDefinitions_Gizurean.xml', { parser })
    return translation
}

const translateResearchProjectDefinitionsIkkuro = async function () {
    const parser = xmlParser(['ArrayOfResearchProjectDefinition', 'ResearchProjectDefinition', 'Name'])
    const translation = await translate.file('game-data/original/ResearchProjectDefinitions_Quameno.xml', { parser })
    return translation
}

const translateResearchProjectDefinitionsQuameno = async function () {
    const parser = xmlParser(['ArrayOfResearchProjectDefinition', 'ResearchProjectDefinition', 'Name'])
    const translation = await translate.file('game-data/original/ResearchProjectDefinitions_Quameno.xml', { parser })
    return translation
}

const translateGameEvents = async function () {
    const parser = xmlParser(['ArrayOfGameEvent', 'GameEvent', 'TriggerActions', 'GameEventAction', 'Description'])
    const translation = await translate.file('game-data/original/GameEvents.xml', { parser })
    return translation
}

const translateComponentDefinifitions = async function () {
    const parser = xmlParser(['ArrayOfComponentDefinition', 'ComponentDefinition', 'Name'])
    const translation = await translate.file('game-data/original/ComponentDefinitions.xml', { parser })
    return translation
}

const translateGovernments = async function () {
    const nameParser = xmlParser(['ArrayOfGovernment', 'Government', 'Name'])
    const leaderParser = xmlParser(['ArrayOfGovernment', 'Government', 'LeaderTitle'])
    const empireAdjectivesParser = xmlParser(['ArrayOfGovernment', 'Government', 'EmpireNameAdjectives', 'string'])
    const empireNounsParser = xmlParser(['ArrayOfGovernment', 'Government', 'EmpireNameNouns', 'string'])

    await translate.file('game-data/original/Governments.xml', { parser: nameParser })
    await translate.file('game-data/mod/Governments.xml', { parser: leaderParser })
    await translate.file('game-data/mod/Governments.xml', { parser: empireAdjectivesParser })
    await translate.file('game-data/mod/Governments.xml', { parser: empireNounsParser })
}

// await translateGovernments()
// await translateComponentDefinifitions()
// await translateGameEvents()
// await translateResearchProjectDefinitions()
// await translateResearchProjectDefinitionsDhayut()
// await translateResearchProjectDefinitionsGizurean()
// await translateResearchProjectDefinitionsIkkuro()
// await translateResearchProjectDefinitionsQuameno()
