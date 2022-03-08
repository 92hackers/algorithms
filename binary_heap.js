/**
 * Binary Heap
 *
 * Construct a min-heap.
 */

function BinaryHeap(nums) {
  this.arr = nums
  this.size = nums.length
}

BinaryHeap.prototype.upAdjust = function() {
  let childIndex = this.size - 1
  let parentIndex = childIndex - 1 >> 1
  const cacheChildValue = this.arr[childIndex]

  while (parentIndex > -1 && cacheChildValue <= this.arr[parentIndex]) {
    this.arr[childIndex] = this.arr[parentIndex]
    childIndex = parentIndex
    parentIndex = childIndex - 1 >> 1
  }

  this.arr[childIndex] = cacheChildValue
}

// Move big values down of the heap.
BinaryHeap.prototype.downAdjust = function(nodeIndex) {
  const size = this.size
  const arr = this.arr
  let parentIndex = nodeIndex
  const cacheParentValue = arr[parentIndex]
  let childIndex = 2 * parentIndex + 1

  while (childIndex < size) {
    // Compare left child with right child
    const rightChildIndex = childIndex + 1
    if (rightChildIndex < size && arr[rightChildIndex] < arr[childIndex]) {
      childIndex = rightChildIndex
    }
    if (cacheParentValue <= arr[childIndex]) { // The parent node has already been the smallest item compared to it's children
      break
    }
    arr[parentIndex] = arr[childIndex]
    parentIndex = childIndex
    childIndex = 2 * parentIndex + 1
  }

  arr[parentIndex] = cacheParentValue
}

BinaryHeap.prototype.buildHeap = function() {
  for (let i = this.size- 2 >> 1; i > -1; i--) {
    this.downAdjust(i)
  }
}

function main() {
  const nums = [1, 19, 89, 23, 0, -111, 222, 99, 777, 3, 9, 45, 20, 8, 4, 921, 23, 17, 19, 23, 97, 59, 91, 100, 200, 300, 400, 545, -10000]
  console.log('before: ', nums)
  const binaryHeap = new BinaryHeap(nums)
  binaryHeap.upAdjust()
  // binaryHeap.buildHeap()
  console.log('after heap built: ', nums, nums.length)
}

main()
