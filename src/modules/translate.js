import fs from 'fs/promises'

export async function file(filename, { parser }) {
    const file = await fs.readFile(filename, { encoding: 'utf-8' })
    const translated = await parser(file)

    const [path, fname] = filename.split(/\/(?=\w+\.\w+)/)
    await fs.writeFile(`${path.replace('original', 'mod')}/${fname}`, translated)
    return translated
}
