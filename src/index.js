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
// await translateResearchProjectDefinitions()
// await translateResearchProjectDefinitionsDhayut()
await translateResearchProjectDefinitionsGizurean()
// await translateResearchProjectDefinitionsIkkuro()
// await translateResearchProjectDefinitionsQuameno()
