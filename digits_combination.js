/**
 * 穷举一个数字的组成的全部排列组合形式，例如：
 * 123,
 * 132,
 * 213,
 * 231,
 * 312,
 * 321.
 */

function digitsCombination(num) {
  if (num < 10) { // one bit number.
    return num
  }

  const numsStr = '' + num
  const map = Object.create(null)
  for (let item of numsStr) {
    const restChars = numsStr.split(item)
    let allChars = ''
    for (let chars of restChars) {
      allChars += chars
    }
    map[item] = digitsCombination(allChars)
  }
  return map
}

function deepIterate(tree) {
  let str = ''
  Object.keys(tree).forEach((key) => {
    const value = tree[key]
    str += key
    if (typeof value === 'string') {
      str += value
    } else {
      str += deepIterate(value)
    }
  })
  console.log(str)
  return str
}

const tree = digitsCombination(987643)
const result = deepIterate(tree)

// console.log(result)
