function fibMaster() {
    let cache = {}
    return function fib(n) {
  
      if (cache[n]) {
        return cache[n]
      }
      else {
        if (n < 2) {
          cache[n] = n      
        }
  
        else{
        cache[n] = fib(n - 1) + fib(n - 2)
        // console.log('cache: ',cache)      
        }
        return cache[n]
      }
      
    }
  }
  
  
  const result = fibMaster()
  const fibResult = result(2000)
  console.log(fibResult)