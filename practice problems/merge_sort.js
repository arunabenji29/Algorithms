const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

function mergeSort(array) {
  if (array.length === 1) {
    return array
  }
  let left = array.slice(0, (Math.floor(array.length / 2)))
  console.log(left)
  let right = array.slice((Math.floor(array.length / 2)),)
  console.log(right)
  return merge(mergeSort(left), mergeSort(right))
}

function merge(left, right) {
    console.log('left : ',left)
    console.log('right : ',right)
  let sortedArray = []
  let i = 0
  let j = 0
  while(i < left.length || j < right.length ){
      console.log('merge: inside while')
      console.log('i : ',i)
      console.log('j : ',j)
      console.log('left[i] : ',left[i])
      console.log('right[j] : ',right[j])
    if(left[i] < right[j]){
        sortedArray.push(left[i])
        i=i+1
      }
      else if(left[i] > right[j]){
        sortedArray.push(right[j])
        j=j+1
      }
      else if(i===left.length ){
        sortedArray = sortedArray.concat(right.slice(j,))
        console.log('inside while: if: i===left.length : right slice',right.slice(j,))
        console.log('inside while: if: i===left.length : ',sortedArray)
        break
      }
      else if(j===right.length){
        sortedArray = sortedArray.concat(left.slice(i,))
        console.log('inside while: if: j===right.length : left slice',left.slice(i,))
        console.log('inside while: if: j===right.length : ',sortedArray)
        break
      }
      console.log('inside while: sortedArray : ',sortedArray)
  }
  console.log('sortedArray : ',sortedArray)
  return sortedArray
}

const answer = mergeSort(numbers)
console.log(answer)