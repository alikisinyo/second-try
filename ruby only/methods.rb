def sayhi(name = "no name", age = -1)
  puts ("Hello " + name + " you are " + age.to_s)
end

sayhi("Ali", 73)
# trial text
def goodmorning(name = "no name")
  puts ("Goodmorning " + name)
end

goodmorning("Ali")
# return values
def cube(num)
  return num * num * num
end
puts cube(3)
