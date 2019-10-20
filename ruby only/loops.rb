# while loops
# a = 1
# while a <= 8
#   puts a
#   a += 1
# end
# guessing game while loops

# word = "shazam"
# guess = ""
# guessCount = 0
# guessLimit = 3
# guessout = false
# while guess != word and !guessout
#   if guessCount < guessLimit
#   puts "enter your guess: "
#   guess = gets.chomp()
#   guessCount += 1
#   else
#     guessout = true
#   end
# end
# if guessout
#   puts "loser"
# else
#   puts "congrats you got it! "
#
# end

secretCode = "pink"
guess = ""
guessCount = 0
guessLimit = 3
guessout = false
while guess != secretCode and !guessout
  if guessCount < guessLimit
    puts "what is the secretCode:"
    guess = gets.chomp()
    guessCount +=1
  else
    guessout = true
  end
end
if guessout
  puts "loser"
else
  puts "bingo!"

end
