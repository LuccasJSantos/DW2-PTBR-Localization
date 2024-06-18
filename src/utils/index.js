import * as R from 'ramda'

export const sleep = (ms) => {
    return new Promise((resolve) => setTimeout(() => resolve(), ms))
}

export const path = (pathList, object) => {
    if (pathList.length === 0 || object === undefined) {
        return object
    }

    const [key] = pathList

    if (Array.isArray(object[key])) {
        return object[key].flatMap(item => path(pathList.slice(1), item))
    }

    return path(pathList.slice(1), object[pathList[0]])
}