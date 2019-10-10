/**
 * 反转字符串
 *
 * 'chenyuan' ---> 'nauynehc'
 */

const reverseString = str => {
  const strLength = str.length
  let result = ''

  for (let i = strLength - 1; i > -1; i--) {
    result += str[i]
  }

  return result
}

a = 'chenyuan, hello0, world'

console.log(a)

console.log(reverseString(a))
