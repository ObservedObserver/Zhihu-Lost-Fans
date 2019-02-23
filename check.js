const fs = require('fs')
const args = global.process.argv.slice(2)
const lastRecord = args[0].split('=')[1]
const currentRecord = args[1].split('=')[1]
const data1 = JSON.parse(fs.readFileSync(currentRecord).toString())

let map1 = new Map()
data1.forEach(item => {
  map1.set(item.id, item)
})

const data2 =  JSON.parse(fs.readFileSync(lastRecord).toString())

data2.forEach(item => {
  if (!map1.has(item.id)) {
    const {
      url_token,
      is_followed,
      type,
      url,
      name,
      articles_count,
      headline,
      answer_count,
      is_org,
      follower_count,
      id,
      is_following,
      gender
    } = item
    console.table({
      url_token,
      is_followed,
      type,
      url,
      name,
      articles_count,
      headline,
      answer_count,
      is_org,
      follower_count,
      id,
      is_following,
      gender
    })
  }
})
