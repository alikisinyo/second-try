ismale = true
istall = true
# ruby doesnt use colons after an if statement block
if ismale or istall
  puts "You are a tall male"
elsif ismale and !istall
  puts "you are a short male"
elsif !ismale and istall
  puts "you are not male but are tall"
else
  puts "you either not male or not tall or both"
end
