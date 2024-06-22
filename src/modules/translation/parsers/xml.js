import parser from 'xml2js'
import fs from 'fs/promises'
import * as u from '../../../utils/index.js'
// import { translate } from 'free-translate'
// import puppeteer from 'puppeteer'

const SEPARATOR = '|'

export default function (path) {
    return async function (content) {
        const json = await parser.parseStringPromise(content)
        const data = u.path(path, json).filter(Boolean)
        const [key] = path.slice(-1)
        const text = data.join(SEPARATOR)
        await fs.writeFile(`src/translation-batch/${path}.xml`, text)

        try {
            const itemsTranslated = await fs.readFile('src/translation-batch/translation.data', { encoding: 'utf-8' })
            const textTranslated = itemsTranslated
                .split(SEPARATOR)
                .reduce((acc, item, index) => acc.replace(`<${key}>${text.split(SEPARATOR)[index]}</${key}>`, `<${key}>${item.trim()}</${key}>`), content)
            return textTranslated
        } catch (error) { }

        return ''
        // const translated = await translate(text, { from: 'en', to: 'pt-BR' })
        //         const browser = await puppeteer.launch({ headless: false })
        //         const page = await browser.newPage()
        //         await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36");
        //         await page.goto('https://chatgpt.com/')
        //         const query = `Traduza o seguinte texto, mantendo a estrutura delimitada por vírgulas, e me traga a resposta em um bloco de código, traduzir ship para nave:
        // ${text.slice(100)}`
        //         await page.waitForSelector('#prompt-textarea')
        //         await u.sleep(3000)
        //         await page.$eval('#prompt-textarea', function (element, query) {
        //             element.innerHTML = query
        //             console.log({ query })
        //         }, query)
        //         await page.click('button[data-testid=send-button]')
        //         return ''
    }
}