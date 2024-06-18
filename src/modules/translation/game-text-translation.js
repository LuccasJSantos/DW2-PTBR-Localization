import { translate } from 'free-translate'

const NEW_LINE_PLACEHOLDER = '. Apple here. '
const NEW_LINE_PLACEHOLDER_REPLACER = '. Apple aqui. '
const BATCH_SIZE = 10

export default async function (text) {
    const lines = text.split(/\n/)
    const pairs = lines
        .map(line => line.split(';'))
    // .filter(pair => pair[0] === '' ? ['', ''] : pair)
    // .slice(0, 100)
    // const normalizedText = pairs.reduce((acc, pair) => `${acc}${pair[1]}${NEW_LINE_PLACEHOLDER}`, '')
    // const translation = await translate(normalizedText, { from: 'en', to: 'pt' })
    // const parsed = translation.replaceAll(NEW_LINE_PLACEHOLDER_REPLACER, '\n')
    // return parsed
    const translation = []
    for (let i = 0; i < Math.floor(pairs.length / BATCH_SIZE); i += BATCH_SIZE) {
        const payload = pairs.slice(i, (i + 1) * BATCH_SIZE)
        const promises = payload.map(item => translate(item, { from: 'en', to: 'pt' }))
        const responses = await Promise.allSettled(promises)
        console.log(`[game-text]: sending ${BATCH_SIZE} items of batch #${i}`)
        translation.push(responses)
    }
    return translation.join('\n')
}