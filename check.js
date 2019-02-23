const fs = require('fs')

const data1 = JSON.parse(fs.readFileSync('[fans-data]2019-02-23 22:14:39.json').toString())
console.log(data1.length)
let map1 = new Map()
data1.forEach(item => {
  map1.set(item.id, item)
})

const data2 =  JSON.parse(fs.readFileSync('a').toString())
console.log(data2.length)

data2.forEach(item => {
  if (!map1.has(item.id)) {
    console.log(item)
  }
})
