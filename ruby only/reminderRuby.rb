# puts "hello world"
#
# geting imput from the user
# puts "what is your name"
# name = gets.chomp()
# puts ("welcome " + name)
# # madlib game
# puts "what is your favourite color"
# color = gets.chomp()
# puts "what is your favourite feelings"
# feelings = gets.chomp()
# puts "what is your favourite celebrity"
# celebrity = gets.chomp()
#
# puts ("roses are " + color)
# puts (feelings + " are bloom")
# puts ("so is " + celebrity)
#
# hashes (dictionaries)
# places =
# {
#   :Mombasa =>"MSA",
#   :Nairobi => "NRB",
#   :Isiolo => "ISL",
#   :Nanyuki => "NYK"
# }
# puts places[:Mombasa]
#
# puts "enter first number: "
# num1 = gets.chomp().to_f
# puts "enter operator type: "
# opt = gets.chomp()
# puts "enter first second number: "
# num2 = gets.chomp().to_f
#
# if opt == "+"
#   print (num1 + num2)
# elsif opt == "*"
#   print (num1 * num2)
# elsif opt == "/"
#   print (num1 / num2)
# elsif opt == "-"
#   print (num1 - num2)
# elsif opt == "^"
#   print (num1 ** num2)
# else
#   print "invalid operator"
# end
#
# def weekdays(day)
#   dayName = ""
#
#   case day
#   when "mon"
#     dayName = "monday"
#   when "tue"
#     dayName = "tuesday"
#   when "wed"
#     dayName = "wednesday"
#   when "thur"
#     dayName = "thursday"
#   when "fri"
#     dayName = "friday"
#
#   end
# end
#
# puts weekdays("mon")
#
# def max(num1, num2, num3)
#   if num1 >= num2 and num1 >= num3
#     return num1
#   elsif num2 >= num1 and num2 >= num3
#       return num2
#   else
#         return num3
#   end
# end
#
# puts max(1,2,3)
#
# def min(num1, num2, num3)
#   if num1 <= num2 and num1 <= num3
#     return num1
#   elsif num2 <= num1 and num2 <= num3
#       return num2
#   else
#         return num3
#   end
# end
#
# puts min(1,2,3)
#
# word = "shazam"
# guess = ""
# guessCount = 0
# guessLimit = 3
# guessout = false
# while guess !=word and !guessout
#   if guessCount < guessLimit
#     puts "enter the secret word"
#     guess = gets.chomp()
#     guessCount += 1
#   else
#     guessout = true
#   end
# end
# if guessout
#   puts "loser!"
# else
#   puts "shazam! you got it"
# end
