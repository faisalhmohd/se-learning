import math

def crossOfPrimeNumbers(primeNumber, primeNumbers):
  loopIndex = primeNumber * primeNumber
  while loopIndex < len(primeNumbers):
    primeNumbers[loopIndex] = False
    loopIndex += primeNumber

def getNextPrime(prime, primeNumbers):
  next = prime + 1
  while (next < len(primeNumbers) and not primeNumbers[next]):
    next += 1

  return next

def sieveOfEratosthenes(number):
  primeNumbers = []

  for n in range(number + 1):
    if n < 2:
      primeNumbers.append(False)
    else:
      primeNumbers.append(True)

  prime = 2

  while prime <= math.sqrt(number):
    crossOfPrimeNumbers(prime, primeNumbers)
    prime = getNextPrime(prime, primeNumbers)

  return primeNumbers

print(sieveOfEratosthenes(12))